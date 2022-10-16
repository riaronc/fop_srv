from sqlalchemy import func

from app import db


class Fop(db.Model):
    __tablename__ = 'fops'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"{self.id = }, {self.name}"

    def to_dict(self, exclude_keys: tuple = ()):
        exclude_keys = () + exclude_keys
        result = vars(self)

        for key in exclude_keys:
            result.pop(key, None)
        return result
