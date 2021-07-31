from http import HTTPStatus
from flask import abort


class ValidationService:
    @staticmethod
    def validate(validation_schema, data):
        errors = validation_schema.validate(data)
        if errors:
            abort(HTTPStatus.BAD_REQUEST, str(errors))
