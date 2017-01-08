from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from .app import db

class Mountain(db.Model):
    __tablename__ = 'mountain'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
