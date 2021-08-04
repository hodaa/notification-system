from project.strategies.EmailStrategy import EmailStrategy
from project.strategies.SmsStrategy import SmsStrategy
from project.strategies.PushNotificationStrategy import PushNotificationStrategy
import redis
from datetime import timedelta
import os


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
r = redis.from_url(os.getenv('REDIS_URL'))


factory.register('EMAIL', EmailStrategy)
r.setex("email_limiter", timedelta(minutes=1), value=0)

factory.register('SMS', SmsStrategy)
r.setex("sms_limiter", timedelta(minutes=1), value=0)

factory.register('PUSH_NOTIFICATION', PushNotificationStrategy)
r.setex("push_limiter", timedelta(minutes=1), value=0)
