from project.strategies import Strategy
from project.repositories.UserNotificationRepository import UserNotificationRepository



class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def add_notification(self, provider, notification, users) -> None:
        repo = UserNotificationRepository()
        repo.add_bulk(provider, notification, users)
        self._strategy.send_notification(notification, users)
