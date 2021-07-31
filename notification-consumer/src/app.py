import logging
import  threading
from project import create_app
from project.services.QueueConnectorService import QueueConnectorService
from project.models import db


app = create_app('development')

# logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    db.create_all(app=app)
    connector = QueueConnectorService()
    thread_1 = threading.Thread(target=connector.start_rmq_connection)
    thread_1.start()
    thread_1.join(0)
    app.run(port=4000, host='0.0.0.0')
    # connector.start_rmq_connection()
    # app.run(port=4000)
