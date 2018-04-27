#!/usr/bin/env python

from app import db
from datetime import datetime, timedelta


class URL(db.Model):
    __tablename__ = "url"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True)
    codes = db.relationship('Code', backref='url', lazy='dynamic')
    hits = db.relationship('Hit', backref='url', lazy='dynamic')

    def __repr__(self):
        return self.url
   
    def daily_hits(self):
        return self.hits.\
            filter(Hit.timestamp > datetime.utcnow() - timedelta(1)).\
            order_by(Hit.timestamp.desc())


class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))
    code = db.Column(db.String(), unique=True)
    hits = db.relationship('Hit', backref='code', lazy='dynamic')

    def __repr__(self):
        return self.code


class Hit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))
    code_id = db.Column(db.Integer, db.ForeignKey('code.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return str(self.timestamp.strftime("%Y-%m-%d %H:%M"))
