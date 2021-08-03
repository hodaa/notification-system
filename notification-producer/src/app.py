import os
#
from dotenv import load_dotenv
from project import create_app
from project.models import db
# load env vars
env_path = os.getcwd() + '/.env'
load_dotenv(dotenv_path=env_path, verbose=True, override=True)

config_name = os.getenv('ENVIRONMENT')
app = create_app(config_name)

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(host='0.0.0.0')
