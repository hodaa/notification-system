from project import create_app
from project.models import db
import threading
from project.services.QueueWorkerService import QueueWorkerService


app = create_app()

if __name__ == '__main__':
    queue = QueueWorkerService()
    queue_thread = threading.Thread(target=queue.start_rmq_connection)
    queue_thread.start()
    queue_thread.join(0)

    db.create_all(app=app)
    app.run(host='0.0.0.0')
