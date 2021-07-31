from datetime import datetime
from project.enums.Provider import Provider
from project.models import db, ma
from marshmallow.validate import Length
from marshmallow import Schema, fields, validates, ValidationError, validate
from enum import IntEnum, unique


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    # pet_category = db.Column(db.String(50), nullable=False)

    # create a handler id column establishing a relationship with the foreign key class table
    # handler_id = db.Column(db.Integer, db.ForeignKey('pethandler.handler_id'), nullable=False)


class NotificationSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id", "title", "body")


class CreateNotificationInputSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=60))
    body = fields.Str(required=True)


# class SendNotificationInputSchema(Schema):
#     notification_id = fields.Integer(required=True)
#     consumers = fields.Integer(required=False)
#     # providers = fields.Dict(keys=fields.String(), values=fields.Integer)
#     providers = fields.MultiDict(fields.String(), required=True)
#
#     # Provider.value
#     # providers = fields.Str(validate=validate.OneOf(["1", "2", "3"]))
#     #
#     @validates('providers')
#     def validate_valid(self, value):
#         if value < 1:
#             raise ValidationError(type(value))

    # {'providers': ['6']}
    #     # for item in value['providers']:
    #     #     try:
    #     #         Provider(item)
    #     #     except:
    #     #         raise ValidationError('Quantity must be greater than 0.')
    #
    #     # raise ValidationError(value)
    #     # # return Provider(value).name
    #     # # if isinstance(Provider(value),IntEnum):
    #     # #     raise ValidationError('Quantity must be greater than 0.')
