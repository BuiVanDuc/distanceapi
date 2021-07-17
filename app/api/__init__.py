from flask import Blueprint

api = Blueprint('api_webservice', __name__)

from .distance import views
