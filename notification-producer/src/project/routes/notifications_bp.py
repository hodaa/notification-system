from project.routes import notifications_bp
from project.controllers.NotificationController import NotificationController

controller = NotificationController()
notifications_bp.route('', methods=['POST'])(controller.store)
notifications_bp.route('', methods=['GET'])(controller.index)
notifications_bp.route('/send', methods=['POST'])(controller.send)
