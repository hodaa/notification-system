from datetime import datetime

from marshmallow.validate import Length, Email
from project import db
from project.models import ma
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    mobile = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(225))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id", "name", "email", "mobile", 'token')


class CreateUserInputSchema(Schema):
    name = fields.Str(required=True, validate=Length(max=60))
    email = fields.Str(required=True, validate=Email(), unique=True)
    mobile = fields.Int(required=True)
