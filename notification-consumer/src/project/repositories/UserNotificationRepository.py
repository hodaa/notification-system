from project.models.UserNotification import UserNotification, UserNotificationSchema
from flask import jsonify


from project import create_app
from project.models import db

app = create_app('development')
app.app_context().push()


class UserNotificationRepository:
    def get_by_user_id(self, user_id):
        data = UserNotification.query.get(user_id)
        schema = UserNotificationSchema()
        return jsonify({"users": schema.dump(data)})

    def store(self, user_id, title, body, provider):
        notify = UserNotification(user_id=user_id, title=title, body=body, provider=provider)
        db.session.add(notify)
        return db.session.commit()
