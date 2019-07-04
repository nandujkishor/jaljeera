from app import app, db
import datetime

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(600), nullable=False) # Max 600 characters
    tagline = db.Column(db.String(200)) # Max 200 characters
    cat = db.Column(db.Integer, nullable=False, db.Foreignkey('events_cat.id'))
    organiser = db.Column(db.String(20), nullable=False)
    collection = db.Column(db.Integer, db.Foreignkey('collections.id'))

class Cats(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    desc = db.Column(db.Text)

class Collections(db.Model):
    # Group of events One to Many relation
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Tags(db.Model):
    # Many to Many relationship
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.Text)

class TagstoEvents(db.Model):
    # One to Many for tag to events: P1 of of many to many
    tagid = db.Column(db.Integer, primary_key=True, db.Foreignkey('tags.id'))
    eid = db.Column(db.Integer, primary_key=True, db.Foreignkey('events.id'))

class EventstoTags(db.Model):
    # One to Many for tag to events: P1 of of many to many
    eid = db.Column(db.Integer, primary_key=True, db.Foreignkey('events.id'))
    tagid = db.Column(db.Integer, primary_key=True, db.Foreignkey('tags.id'))
