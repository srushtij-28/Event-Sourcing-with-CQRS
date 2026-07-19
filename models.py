from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    event_type = db.Column(
        db.String(50),
        nullable=False
    )

    data = db.Column(
        db.String(255),
        nullable=False
    )
