from flask import Flask, request, jsonify
from models import db, Event

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///events.db"

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------- Command ----------
@app.route("/commands", methods=["POST"])
def create_event():

    data = request.get_json()

    event = Event(
        event_type=data["event_type"],
        data=data["data"]
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({
        "message": "Event Stored"
    })


# ---------- Query ----------
@app.route("/events")
def get_events():

    events = Event.query.all()

    return jsonify([
        {
            "id": event.id,
            "event_type": event.event_type,
            "data": event.data
        }
        for event in events
    ])


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)
