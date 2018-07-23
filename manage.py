from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from py_web import create_app
from py_web.config import DevConfig
from py_web.database import db
from py_web.models import User




app = create_app(DevConfig)

manager = Manager(app)
migrate=Migrate(app,db)

manager.add_command('runserver', Server())
manager.add_command('db',MigrateCommand)

@manager.shell
def make_context():
    return dict(app=app,db=db,User=User)

if __name__ == '__main__':
    manager.run()
