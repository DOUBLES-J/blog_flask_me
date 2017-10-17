from flask_script import Manager
from app import create_app
import os
from flask_migrate import Migrate, MigrateCommand
from app import db

app = create_app(os.environ.get('config_name') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
