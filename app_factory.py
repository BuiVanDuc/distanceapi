import os
# import create_app & db from app/__init__.py in root project directory
from app import create_app, db
from flask_migrate import Migrate

# this part will refer to config.py
app = create_app(os.getenv("FLASK_ENV") or "default")

# will be used to run migration later
migrate = Migrate(app, db)
