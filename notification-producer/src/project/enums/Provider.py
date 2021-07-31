from enum import Enum, unique


@unique
class Provider(Enum):
    SMS = 1
    EMAIL = 2
    PUSH_NOTIFICATION = 3
