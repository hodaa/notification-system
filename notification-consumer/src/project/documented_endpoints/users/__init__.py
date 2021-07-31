from flask_restplus import Namespace, Resource, fields

namespace = Namespace('api/v1/users', 'list all users')

user_model = namespace.model('User', {
    'id': fields.Integer(
        readonly=True,
        description='User identifier'
    ),
    'name': fields.String(
        required=True,
        description='user name'
    ),
    'email': fields.String(
        required=True,
        description='user email'
    ),
    'mobile': fields.String(
        required=True,
        description='user mobile'
    ),
})

hello_world_example = {'message': 'Hello World!'}
user_example = {'message': 'user created successfully!'}


@namespace.route('')
class User(Resource):

    @namespace.marshal_list_with(user_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        return hello_world_example

    @namespace.response(200, 'User Created successfully')
    def post(self):
        return {'message': 'User created Successfully!'}


@namespace.route('/<int:user_id>')
class entity(Resource):
    '''Read, update and delete a specific entity'''

    @namespace.response(404, 'User not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(user_model)
    def get(self, user_id):
        '''Get entity_example information'''

        return user_example
