#!/usr/bin/env python

from app import app, db
from flask import render_template, redirect, url_for
from app.forms import GetURLForm, GetCustomURLForm
from app.models import URL, Shorten_URL
from app.encoder import code_generator

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetURLForm()
    if form.validate_on_submit():
        url = URL.query.filter_by(URL=form.url.data).first()
        if url is not None:
            url.access += 1
            db.session.commit()
        else:
            url = URL(URL=form.url.data)
            db.session.add(url)
            s = Shorten_URL(code=code_generator(), real_URL=url)
            db.session.add(s)
            db.session.commit()
        code = Shorten_URL.query.filter_by(url_id=url.id).first()
        return render_template("index.html", title="Index",
                               form=form, code=code)
    return render_template("index.html", title="Index", form=form)



@app.route('/Custom', methods=['GET', 'POST'])
def custom():
    form = GetCustomURLForm()
    if form.validate_on_submit():
        url = URL.query.filter_by(URL=form.url.data).first()
        if url is not None:
            url.access += 1
        else:
            url = URL(URL=form.url.data)
            db.session.add(url)
        s = Shorten_URL(code=form.customcode.data, real_URL=url)
        db.session.add(s)
        db.session.commit()

        return render_template("custom.html", title="Custom URL",
                               form=form, code=s.code)

    return render_template("custom.html", title="Custom URL", form=form)

@app.route('/<code>')
def goto(code):
    s = Shorten_URL.query.filter_by(code=code).first()
    if s is not None:
        u = URL.query.get(s.url_id).URL
        return redirect(u)
    return redirect(url_for('index'))
