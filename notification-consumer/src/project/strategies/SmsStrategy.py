from project.strategies.Strategy import Strategy
from project.repositories.UserNotificationRepository import UserNotificationRepository
import logging


class SmsStrategy(Strategy):

    def send_notification(self, notification, users):
        tokens = map(lambda user: user['mobile'], users)
        logging.info(list(tokens))
        # mobile = user['mobile']
        # logging.info(mobile)
