from flask import request, make_response, jsonify, abort
from project.models.User import User, UserSchema, CreateUserInputSchema
from project.services.UserService import UserService
from project.services.ValidationService import ValidationService
from http import HTTPStatus


class UserController:

    def __init__(self):
        self.user_service = UserService()

    def index(self):
        users = self.user_service.get_all()
        return make_response(users, HTTPStatus.OK)

    def store(self):
        ValidationService.validate(CreateUserInputSchema(), request.form)
        self.user_service.save(request.form)
        return make_response(jsonify({"message": "User created successfully "}), HTTPStatus.CREATED)

    def show(self, user_id):
        user = self.user_service.get_by_id(user_id)
        return make_response(user, HTTPStatus.OK)
