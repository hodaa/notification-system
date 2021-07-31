from datetime import datetime
from project import db
from project.models import ma


class UserNotification(db.Model):
    __tablename__ = 'user_notification'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    # notification_id = db.Column(db.Integer())
    title = db.Column(db.String(120))
    body = db.Column(db.String(225))
    provider = db.Column(db.String(120))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class UserNotificationSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id", "title", "body")

