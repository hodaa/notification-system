from project.strategies.Strategy import Strategy
import smtplib
import os


class EmailStrategy(Strategy):
    def send_notification(self, notification, users):
        receivers = map(lambda user: user['email'], users)
        sender = os.getenv('EMAIL_SENDER')
        message = notification['body']

        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.sendmail(sender, receivers, message)
        except smtplib.SMTPException:
            print("Error: unable to send email")
