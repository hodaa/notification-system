from project.strategies.Strategy import Strategy
from project.services.RequestLimiter import RequestLimiter
import smtplib
import os



class EmailStrategy(Strategy):

    def send_notification(self, notification, users):

        limiter = RequestLimiter()
        limiter.limit('email_limiter', os.getenv('EMAIL_LIMITER'))

        receivers = map(lambda user: user['email'], users)
        sender = os.getenv('EMAIL_SENDER')
        message = notification['body']

        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.sendmail(sender, receivers, message)
        except smtplib.SMTPException:
            print("Error: unable to send email")
