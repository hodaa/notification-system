from flask import request, make_response, jsonify
from project.models.Notification import CreateNotificationInputSchema
from project.services.NotificationService import NotificationService
from project.services.ValidationService import ValidationService
from http import HTTPStatus


class NotificationController:

    def __init__(self):
        self.__notification_service = NotificationService()

    def index(self):
        result = self.__notification_service.get_all()
        return make_response(result, HTTPStatus.OK)

    def store(self):
        ValidationService.validate(CreateNotificationInputSchema(), request.form)
        self.__notification_service.save(request.form["title"], request.form["body"])

        return make_response(jsonify({"message": "Notification created successfully"}), HTTPStatus.CREATED)

    def send(self):
        msg = self.__notification_service.prepare_msg(request.form)
        self.__notification_service.send_to_rabbit(msg)
        return make_response(jsonify({"message": "notification sent successfully"}), HTTPStatus.OK)
