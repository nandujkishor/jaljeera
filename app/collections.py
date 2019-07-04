# Events module

from flask import Flask, jsonify
from app import app, db

def list():
    coll = Collections.query.all()
     return jsonify(coll)

def get(id):
    return "Event"

def create():
    return "Event created"

def update(id):
    return "Event updated"

def delete(id):
    return "Event deleted"