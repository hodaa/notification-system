from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def send_notification(self, notification, users):
        pass
