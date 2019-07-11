# Events module

from flask import Flask, jsonify
from app import app, db
from app.models import Events

def list():
    events = Events.query.all()
    return jsonify(events)
   
def get(id):
    event = Event.query.filter_by(id=id).first()
    return jsonify(event)

def create():
    event = Event()

def update(id):
    return "Event updated"

def delete(id):
    return "Event deleted"