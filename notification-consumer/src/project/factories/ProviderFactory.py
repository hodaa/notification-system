from project.strategies.EmailStrategy import EmailStrategy
from project.strategies.SmsStrategy import SmsStrategy
from project.strategies.PushNotificationStrategy import PushNotificationStrategy


class ProviderFactory:

    def __init__(self):
        self._creators = {}

    def register(self, provider, creator):
        self._creators[provider] = creator

    def get(self, provider):
        creator = self._creators.get(provider)
        if not creator:
            raise ValueError(provider)
        return creator()


factory = ProviderFactory()
factory.register('EMAIL', EmailStrategy)
factory.register('SMS', SmsStrategy)
factory.register('PUSH_NOTIFICATION', PushNotificationStrategy)
