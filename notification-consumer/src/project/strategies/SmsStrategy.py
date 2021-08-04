from project.strategies.Strategy import Strategy
from project.services.RequestLimiter import RequestLimiter
import os

class SmsStrategy(Strategy):

    def send_notification(self, notification, users):
        limiter = RequestLimiter()
        limiter.limit('sms_limiter', os.getenv('SMS_LIMITER'))

        mobiles = map(lambda user: user['mobile'], users)
        # send(mobiles,notification)
