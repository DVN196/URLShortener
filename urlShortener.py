#!/usr/bin/env python

from app import app, db
from app.models import URL, Code, Hit


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'URL': URL, 'Code': Code, 'Hit': Hit}
