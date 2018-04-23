#!/usr/bin/env python

from app import db
from datetime import datetime


class URL(db.Model):
    __tablename__ = "url"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True)
    codes = db.relationship('Code', backref='url', lazy='dynamic')
    hits = db.relationship('Hit', backref='url', lazy='dynamic')

    def __repr(self):
        return self.url
    
    def total_hit(self):
        return len(self.hits.all())


class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))
    code = db.Column(db.String(), unique=True)

    def __repr__(self):
        return self.code


class Hit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return str(self.timestamp.strftime("%Y-%m-%d %H:%M"))
