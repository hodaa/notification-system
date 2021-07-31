from flask import request, make_response, jsonify
from project.services.UserNotificationService import UserNotificationService
from http import HTTPStatus


class UserNotificationController:

    def __init__(self):
        self.__notification_service = UserNotificationService()

    def index(self, user_id):
        user = self.__notification_service.get_by_user_id(user_id)
        return make_response(user, HTTPStatus.OK)
