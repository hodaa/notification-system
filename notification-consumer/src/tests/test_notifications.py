from project.models import db
from project import create_app
from project.models.UserNotification import UserNotification

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


def test_get_notifications_empty(client):
    response = client.get('/api/v1/notifications/1')
    assert UserNotification.query.count() == 0
    assert response.status_code == 200


def test_get_notifications_exists(client):
    notif1 = UserNotification(user_id=1, title="Promcode", body="This is your promocode")
    notif2 = UserNotification(user_id=1, title="Pick Off", body="Pick off point is")
    db.session.add_all([notif1, notif2])
    db.session.flush()
    response = client.get('/api/v1/notifications/1')
    assert UserNotification.query.count() >= 0
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result == {u'notifications': [{u'title': u'Promcode', 'id': 1, u'body': u'This is your promocode'},
                                         {u'title': u'Pick Off', 'id': 2, u'body': u'Pick off point is'},
                                         ]}
