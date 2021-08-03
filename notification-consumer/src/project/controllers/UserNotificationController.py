from flask import  make_response
from project.repositories.UserNotificationRepository import UserNotificationRepository
from http import HTTPStatus


class UserNotificationController:

    def __init__(self):
        self.__notification_repo = UserNotificationRepository()

    def index(self, user_id):
        notifications = self.__notification_repo.get_by_user_id(user_id)
        return make_response(notifications, HTTPStatus.OK)
