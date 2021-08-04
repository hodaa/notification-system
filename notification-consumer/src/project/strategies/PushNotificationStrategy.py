from project.strategies.Strategy import Strategy
from firebase_admin import messaging
from project.services.RequestLimiter import RequestLimiter
import os

class PushNotificationStrategy(Strategy):
    def send_notification(self, notification, users):
        limiter = RequestLimiter()
        limiter.limit('push_limiter', os.getenv('PUSH_LIMITER'))

        registration_tokens = map(lambda user: user['token'], users)

        # See documentation on defining a message payload.
        message = messaging.MulticastMessage(
            data=notification,
            tokens=registration_tokens,
        )
        response = messaging.send_multicast(message)
        # See the BatchResponse reference documentation
        # for the contents of response.
        print('{0} messages were sent successfully'.format(response.success_count))
