from flask import jsonify, abort, json
from project.models.Notification import Notification, NotificationSchema
from project.services.UserService import UserService
from project.models import db
import pika


class NotificationService:

    def get_by_id(self, id):
        data = Notification.query.get(id)
        schema = NotificationSchema()
        return schema.dump(data)

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
        provider = data.getlist('provider')  # sms or email or pushnotification

        # provider = {"user": "hoda", "name": "hoda", "provider": ["sms", "em"], "users": [{'id': 1}, {"id": 2}]}
        # provider = {"user": "hoda", "name": "hoda", "pr": json.dumps(prov), "users": [{'id': 1}, {"id": 2}]}
        # msg = '{"users": "' + json.dumps(users) + '","provider": "' + json.dumps(provider) + '","notification": "' + json.dumps(notification_obj) + '"}'

        msg = {
                "users": json.dumps(users), "provider": json.dumps(provider),
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
        print(" [x] Sent 'Hello World!'")
        connection.close()
