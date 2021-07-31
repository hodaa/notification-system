from flask import Blueprint

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Api
from project.documented_endpoints.users import namespace as users_ns
from project.documented_endpoints.notifications import namespace as notifications_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='')

api_extension = Api(blueprint,
                    title='Notification service APIs',
                    version='1.0',
                    description='Notification service APIs',
                    doc='/doc/'
                    )

api_extension.add_namespace(users_ns)
api_extension.add_namespace(notifications_ns)
