#!/usr/bin/env python

from app import app, db
from app.models import URL, Shorten_URL

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'URL': URL, 'Shorten_URL': Shorten_URL}
