import os
from models import db
from project.models import User

# Data to initialize database with
PEOPLE = [
    {'name': 'hoda', 'email': 'hoda.hussin@gmail.com', 'mobile': '01069642842'},
    {'name': 'heba', 'email': 'hoda2.hussin@gmail.com', 'mobile': '010369642842'},
    {'name': 'sayed', 'email': 'hoda3.hussin@gmail.com', 'mobile': '010469642842'},

]

# Delete database file if it exists currently
if os.path.exists('swvl.db'):
    os.remove('swvl.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = User(name=person['name'], email=person['email'], mobile=person['mobile'])
    db.session.add(p)

db.session.commit()
