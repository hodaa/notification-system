from project.routes import users_bp
from project.controllers.UserNotificationController import UserNotificationController

controller = UserNotificationController()
users_bp.route('<int:user_id>', methods=['GET'])(controller.index)



