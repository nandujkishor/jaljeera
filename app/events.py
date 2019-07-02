# Events module

from flask import Flask, jsonify
from app import app, db

def list():
    events = Events.query.all()
    return jsonify(events)

def get():
    return "Event"

def create():
    return "Event created"

def update():
    return "Event updated"

def delete():
    return "Event deleted"