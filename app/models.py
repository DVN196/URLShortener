#!/usr/bin/env python

from app import db


class URL(db.Model):
    __tablename__ = "url"
    id = db.Column(db.Integer, primary_key=True)
    URL = db.Column(db.String(), unique=True)
    access = db.Column(db.Integer, default=1)
    shorten_URL = db.relationship('Shorten_URL', backref='real_URL', lazy='dynamic')

    # def create_short_URL(self):
    #     i = id
    #     sURL = encode(id)
    #     while Shorten_URL.query.filter_by(code=sURL).first is not None:
    #         i += 1
    #         sURL = encode(id)
    #     return sURL


class Shorten_URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(), unique=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))

    def __repr__(self):
        return self.code
