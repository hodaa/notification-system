from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('api/v1/notifications/<user_id>', 'list all notifications for specific user')

model = namespace.model('Notification', {
    'id': fields.Integer(
        readonly=True,
        description='Notification identifier'
    ),
    'title': fields.String(
        required=True,
        description='Notification  title'
    ),
    'body': fields.String(
        required=True,
        description='Notification Body'

    ),
})


@namespace.route('')
class Notifications(Resource):
    """Get Notifications list and create new ones"""

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(model)
    def get(self):
        """List with all the notifications"""
        return model
