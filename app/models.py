from app import db


class Profile(db.Model):
    __tablename__ = "distance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.Float, nullable=False)
    update_time = db.Column(db.Float, nullable=False)
    traversed = db.Column(db.Boolean, nullable=False)
    age_history = db.Column(db.ARRAY(db.Integer), nullable=False)
    processed_age = db.Column(db.Integer, nullable=False)
    gender_history = db.Column(db.ARRAY(db.Integer), nullable=False)
    processed_gender = db.Column(db.Integer, nullable=False)
    id_history = db.Column(db.ARRAY(db.String(64)), nullable=False)
    processed_id = db.Column(db.String(255), nullable=False)

    def __init__(self, create_time, update_time, traversed, age_history, processed_age, gender_history, processed_gender,
                 id_history, processed_id):
        self.create_time = create_time
        self.update_time = update_time
        self.traversed = traversed
        self.age_history = age_history
        self.processed_age = processed_age
        self.gender_history = gender_history
        self.processed_gender = processed_gender
        self.id_history = id_history
        self.processed_id = processed_id

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
