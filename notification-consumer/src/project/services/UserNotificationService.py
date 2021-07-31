from project.models.UserNotification import UserNotification,UserNotificationSchema
from flask import jsonify
from project.models import db

class UserNotificationService:

    def get_by_user_id(self, user_id):
        data = UserNotification.query.get(user_id)
        schema = UserNotificationSchema()
        return jsonify({"users": schema.dump(data)})

    def store(self):

        notify = UserNotification(user_id=user_id, provider=provider, title=title, body=body)
        db.session.add(notify)
        return db.session.commit()