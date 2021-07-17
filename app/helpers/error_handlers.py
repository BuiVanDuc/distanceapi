import flask
from sqlalchemy.exc import DatabaseError

error_handler = flask.Blueprint('error_handlers', __name__)


@error_handler.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@error_handler.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500


class BaseError(Exception):
    """Base Error Class"""

    def __init__(self, code=400, message='', status='', field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field

    def to_dict(self):
        return {'code': self.code,
                'message': self.message,
                'status': self.status,
                'field': self.field, }


class NotFoundError(BaseError):
    def __init__(self, message='Not found'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'NOT_FOUND'


class ServerError(BaseError):
    def __init__(self, message='Internal server error'):
        BaseError.__init__(self)
        self.code = 500
        self.message = message
        self.status = 'SERVER_ERROR'
