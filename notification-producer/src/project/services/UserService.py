from project.models.User import User, UserSchema
from flask import request, make_response, jsonify, abort
from project.models.User import User, UserSchema, CreateUserInputSchema
from project.models import db
import random, string


class UserService:

    def get_users_by_id(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        schema = UserSchema(many=True)
        return schema.dump(users)

    def get_all(self):
        all_users = User.query.all()
        schema = UserSchema(many=True)
        data = schema.dump(all_users)
        return jsonify({"users": schema.dump(data)})

    def get_by_id(self, user_id):
        user = User.query.get(user_id)
        schema = UserSchema()
        return jsonify({"users": schema.dump(user)})

    def save(self, data):
        name = data["name"]
        email = data["email"]
        mobile = data["mobile"]
        token = self.generateRandomString()

        user = User(name=name, email=email, mobile=mobile, token=token)
        db.session.add(user)
        db.session.commit()

    def generateRandomString(self, stringLength=50):
        """Generate a random string of token """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
