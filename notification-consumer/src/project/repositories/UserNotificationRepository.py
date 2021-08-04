from project.models.UserNotification import UserNotification, UserNotificationSchema
from flask import jsonify
from project.models import db
from project.database import db_session
from project.models.UserNotification import UserNotification


class UserNotificationRepository:
    def get_by_user_id(self, user_id):
        data = UserNotification.query.where(UserNotification.user_id == user_id).all()
        schema = UserNotificationSchema(many=True)
        return jsonify({"notifications": schema.dump(data)})

    def store(self, user_id, title, body, provider):
        notify = UserNotification(user_id=user_id, title=title, body=body, provider=provider)
        db.session.add(notify)
        return db.session.commit()

    def add_bulk(self, provider, notification, users):
        data = []
        for user in users:
            data.append({
                'user_id': user['id'],
                'title': notification['title'],
                'body': notification['body'],
                'provider': provider
            })
        db_session.bulk_insert_mappings(UserNotification, data)
        db_session.commit()
