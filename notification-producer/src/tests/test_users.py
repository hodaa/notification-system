from project.models import db
from project import create_app
from project.models.User import User
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

    request.addfinalizer(teardown)

    os.close(db_fd)
    os.unlink(db_path)


def test_hello(client):
    response = client.get('/')
    assert b'I am producer notifications service!' in response.data


def test_post_users(client):
    response = client.post('api/v1/users', data=dict(name='hoda',
                                                     email=random_char(7) + "@gmail.com",
                                                     mobile='010101010',
                                                     )
                           )

    result = json.loads(response.data)
    assert User.query.count() > 0
    assert response.status_code == 201
    assert 'User created successfully' in result['message']


def test_get_users(client):
    User.query.delete()
    user1 = User(name="Demo User1", email="test1@gmail.com", mobile="010101010")
    user2 = User(name="Demo User2", email="test2@gmail.com", mobile="01010661010")
    db.session.add_all([user1, user2])
    db.session.flush()
    response = client.get('/api/v1/users')
    assert User.query.count() > 0
    assert response.status_code == 200
    # result = json.loads(response.data)
    # assert result == {u'users': [{u'name': u'Demo User1', u'email': u'test1@gmail.com', u'mobile': u'010101010'},
    #                              {u'name': u'Demo User2', u'email': u'test2@gmail.com', u'mobile': u'01010661010'}
    #                              ]}
    db.session.rollback()


