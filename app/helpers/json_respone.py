from flask import jsonify


class JsonReponse:
    @classmethod
    def error(self, status_code, message):
        return jsonify({"status": "error", "message": message, "status_code": status_code})

    @classmethod
    def ok(self, status_code):
        return jsonify({"code": status_code, "status": "ok", "message": "success"})
