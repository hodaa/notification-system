

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


