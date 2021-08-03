import logging
from project.strategies.Strategy import Strategy
from firebase_admin import messaging


class PushNotificationStrategy(Strategy):
    def send_notification(self, notification, users):
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
