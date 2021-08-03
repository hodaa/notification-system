from project.models import db
from project import create_app
from project.models.UserNotification import UserNotification
# from project.services.SmsSeervice import SmsService
from flask import json

import random
import string
import os
import tempfile
import pytest


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


app = create_app('testing')
app.app_context().push()


@pytest.fixture
def client(request):
    db_fd, db_path = tempfile.mkstemp()
    with app.test_client() as client:
        with app.app_context():
            # init_db()
            db.create_all()

        yield client

    def teardown():
        print("teardown")
        # db.drop_all()

    request.addfinalizer(teardown)

    os.close(db_fd)
    os.unlink(db_path)


# def test_post_notifications(client):
#     response = client.post('api/v1/notifications', data=dict(title='Promocode',
#                                                              body="This is your promocode"
#                                                              )
#                            )
#
#     result = json.loads(response.data)
#     assert Notification.query.count() > 0
#     assert response.status_code == 201
#     assert 'Notification created successfully' in result['message']
#
#
# def test_get_users(client):
#     Notification.query.delete()
#     notif1 = Notification(title="Promcode", body="This is your promocode")
#     notif2 = Notification(title="Pick Off", body="Pick off point is")
#     db.session.add_all([notif1, notif2])
#     db.session.flush()
#     response = client.get('/api/v1/notifications')
#     assert Notification.query.count() > 0
#     assert response.status_code == 200
#     result = json.loads(response.data)
#     assert result == {u'notifications': [{u'title': u'Promcode', 'id': 1, u'body': u'This is your promocode'},
#                                          {u'title': u'Pick Off', 'id': 2, u'body': u'Pick off point is'},
#                                          ]}
#     db.session.rollback()


def test_get_notifications_empty(client):
    # Notification.query.delete()
    # notif1 = Notification(title="Promcode", body="This is your promocode")
    # notif2 = Notification(title="Pick Off", body="Pick off point is")
    # db.session.add_all([notif1, notif2])
    # db.session.flush()
    response = client.get('/api/v1/notifications/1')
    assert UserNotification.query.count() == 0
    assert response.status_code == 200
    # result = json.loads(response.data)
    # assert result == []
    # db.session.rollback()

#
# def test_send_sms():
#     smsObj= SmsService()
#     smsObj.send()

