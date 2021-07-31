import pika, json
from project.factories.ProviderFactory import ProviderFactory
from project.services.MailService import MailService
from project.services.SmsService import SmsService
from project.services.PushNotificationService import PushNotificationService


class QueueConnectorService:

    def start_rmq_connection(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        #
        channel.queue_declare(queue='notifications')

        def callback(ch, method, properties, body):
            bd = body.decode('utf8')
            data = json.loads(bd)
            providers = json.loads(data['providers'])
            users = json.loads(data['users'])
            notification = json.loads(data['notification'])
            factory = ProviderFactory()
            factory.register('EMAIL', MailService)
            factory.register('SMS', SmsService)
            factory.register('EMAIL', PushNotificationService)
            for provider in providers:
                obj = factory.get(provider)
                re = obj.send(notification, users)
                # app.logger.info(re)

        channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
        # app.logger.info(' [*] Waiting for messages.')
        channel.start_consuming()
