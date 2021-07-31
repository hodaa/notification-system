from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('api/v1/notifications', 'list all notifications')

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


@namespace.route('/send')
class Notification(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(model)
    @namespace.doc(params={
        'notification_id': {'in': 'formData'},
        'consumers': {'in': 'formData'},
        'providers': {'in': 'formData'}

    })
    def post(self):
        """Send  Notification"""

        return {'message': 'Notification sent successfully !'}


@namespace.route('')
class Notifications(Resource):
    """Get Notifications list and create new ones"""

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(model)
    def get(self):
        """List with all the notifications"""
        return model

    @namespace.response(500, 'Internal Server error')
    @namespace.doc(params={
        'title': {'in': 'formData', 'description': 'Notification title'},
        'body': {'in': 'formData', 'description': 'Notification Message body'}
    })
    @namespace.marshal_with(model, code=201)
    def post(self):
        """Create a new notification"""
        return {'message': 'Notification created successfully !'}, HTTPStatus.CREATED
