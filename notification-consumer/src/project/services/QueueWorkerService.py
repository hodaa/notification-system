import logging

import pika
import json
from project.strategies.Context import Context
from project.factories.ProviderFactory import factory
from project import make_celery
from project import create_app

app = create_app()
celery = make_celery(app)
from celery import Task


class QueueWorkerService(Task):

    def start_rmq_connection(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='notifications')

        def callback(ch, method, properties, body):
            bd = body.decode('utf8')
            data = json.loads(bd)
            providers = json.loads(data['providers'])
            users = json.loads(data['users'])
            notification = json.loads(data['notification'])

            if len(notification) > 0 and len(users) > 0:
                for provider in providers:
                    provider_obj = factory.get(provider)
                    context = Context(provider_obj)
                    context.add_notification(provider, notification, users)

        channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
