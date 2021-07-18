from flask import Blueprint

api = Blueprint('distance_api', __name__, url_prefix='/api')

from .distance import views
