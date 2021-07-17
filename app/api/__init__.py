from flask import Blueprint

api = Blueprint('api_find_distance', __name__)

from .distance import views
