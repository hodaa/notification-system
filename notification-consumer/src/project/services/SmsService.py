from project.services.Sender import Sender
from project.repositories.UserNotificationRepository import UserNotificationRepository
from flask import  Flask
app = Flask(__name__)

class SmsService(Sender):

    def send(self, notification, users):
        repo = UserNotificationRepository()
        for user in users:
            app.logger.info(user['id'])
            user_id = user['id'],
            title = notification['title']
            body = notification['body']
            provider = 'sms'
            repo.store(user_id, title, body, provider)

        return "I am sms provider"
