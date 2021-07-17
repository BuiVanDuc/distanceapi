export FLASK_ENV=development
#export FLASK_ENV=testing
#export FLASK_ENV=stage
export FLASK_APP=app_factory.py
#flask db init --multidb
flask db init
flask db migrate
flask db upgrade