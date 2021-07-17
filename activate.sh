#!/bin/bash
#this is our main entry
export FLASK_APP=app_factory.py

#you can remove this in deployment server
#it's useful so we can see any change from our code directly when developing
export FLASK_ENV=development

#running the app
flask run