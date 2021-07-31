from threading import Thread
from project.factories.ProviderFactory import ProviderFactory

# from flask_mail import Message

# from app import app
# from app import mail


class MailService:
    def send(self, users, notification):
        # print("I am smes")
        return "I am EMAIL"
    # def send_async_email(self ,app, msg):
    #     with app.app_context():
    #         try:
    #             mail.send(msg)
    #         except ConnectionRefusedError:
    #             raise InternalServerError("[MAIL SERVER] not working")
    #
    # def send_email(self, subject, sender, recipients, text_body, html_body):
    #     msg = Message(subject, sender=sender, recipients=recipients)
    #     msg.body = text_body
    #     msg.html = html_body
    #     Thread(target= self.send_async_email, args=(app, msg)).start()


factory = ProviderFactory()
factory.register('EMAIL', MailService)