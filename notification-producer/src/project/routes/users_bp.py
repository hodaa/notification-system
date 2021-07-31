from project.routes import users_bp
from project.controllers.UserController import UserController

controller = UserController()
users_bp.route('', methods=['GET'])(controller.index)
users_bp.route('', methods=['POST'])(controller.store)
users_bp.route('<int:user_id>', methods=['GET'])(controller.show)



