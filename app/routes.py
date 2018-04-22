#!/usr/bin/env python

from app import app, db
from flask import render_template, redirect, url_for
from app.forms import GetURLForm, GetCustomURLForm
from app.models import URL, Code, Entry
from sqlalchemy.sql.expression import func
from app.encoder import code_generator

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetURLForm()
    if form.validate_on_submit():
        u = URL.query.filter_by(url=form.url.data).first()
        if u is None:
            u = URL(url=form.url.data)
            db.session.add(u)
            c = Code(code=code_generator(), url=u)
            db.session.add(c)
            db.session.commit()
        else:
            c = u.codes.order_by(func.length(Code.code)).first()
        return render_template("index.html", title="Index",
                               form=form, code=c.code)
    return render_template("index.html", title="Index", form=form)



@app.route('/custom_code', methods=['GET', 'POST'])
def custom_code():
    form = GetCustomURLForm()
    if form.validate_on_submit():
        u = URL.query.filter_by(url=form.url.data).first()
        if u is None:
            u = URL(url=form.url.data)
            db.session.add(u)
        c = Code(code=form.customcode.data, url=u)
        db.session.add(c)
        db.session.commit()

        return render_template("custom.html", title="Custom URL",
                               form=form, code=c.code)

    return render_template("custom.html", title="Custom URL", form=form)

@app.route('/<code>')
def goto(code):
    c = Code.query.filter_by(code=code).first()
    if c is not None:
        u = URL.query.get(c.url_id)
        e = Entry(url=u)
        db.session.add(e)
        db.session.commit()
        return redirect(u.url)
    return redirect(url_for('index'))

# TODO: implement statistic

@app.route('/stats_all')
def stat_all():
    return ""

@app.route('/stats/<int:url_id>')
def stat(url_id):
    return ""