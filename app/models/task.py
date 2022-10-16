from sqlalchemy import func

from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False)
    is_done = db.Column(db.Boolean, server_default="false", nullable=False)
    is_paid = db.Column(db.Boolean, server_default="false", nullable=False)
    priority = db.Column(db.Text)

    fk_fop_id = db.Column(db.Integer, db.ForeignKey('fops.id'), nullable=False)
    fk_fop = db.relationship('Fop')

    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"{self.id = }, {self.name}, {self.is_done}"

    def to_dict(self, exclude_keys: tuple = ()):
        exclude_keys = ('fk_fop', ) + exclude_keys
        result = vars(self)

        for key in exclude_keys:
            result.pop(key, None)
        return result
