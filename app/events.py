# Events module

from flask import Flask, jsonify
from app import app

def list():
    # events = Events.query.all()
    # return jsonify(events)
    return "Hello"

def get(id):
    return "Event"

def create():
    return "Event created"

def update(id):
    return "Event updated"

def delete(id):
    return "Event deleted"