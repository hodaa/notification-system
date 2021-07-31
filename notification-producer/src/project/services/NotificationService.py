from flask import jsonify, json
from project.models.Notification import Notification, NotificationSchema
from project.services.UserService import UserService
from project.models import db
import pika
from project.enums.Provider import Provider
from marshmallow import ValidationError
import pprint
import sys


class NotificationService:

    def get_by_id(self, id):
        data = Notification.query.get(id)
        schema = NotificationSchema()
        return schema.dump(data)

    def get_by_id_obj(self, id):
        return Notification.query.get(id)

    def get_all(self):
        data = Notification.query.all()
        schema = NotificationSchema(many=True)

        return jsonify({"notifications": schema.dump(data)})

    def save(self, title, body):
        notify = Notification(title=title, body=body)
        db.session.add(notify)
        return db.session.commit()

    def prepare_msg(self, data):
        consumers = data.getlist('consumers')
        user_service = UserService()
        users = user_service.get_users_by_id(consumers)

        notification_id = data["notification_id"]
        notification = self.get_by_id(notification_id)
        providers = data.getlist('providers') # sms or email or pushnotification
        providers_list = []

        for provider in providers:
            try:
                Provider(int(provider))
                providers_list.append(Provider(int(provider)).name)
            except:
                raise ValidationError("This not valid Provider")

        msg = {
            "users": json.dumps(users), "providers": json.dumps(providers_list),
            "notification": json.dumps(notification)
        }
        return json.dumps(msg)


    def send_to_rabbit(self, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='notifications')

        channel.basic_publish(exchange='',
                              routing_key='notifications',
                              body=msg
                              )
        print("[x] Sent 'Hello World!'")
        connection.close()
