#!/usr/bin/env python

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError, Length
from app.models import Code
import re

msg = {'URL': 'Not a valid URL',
       'Code length': 'The code must contain 1-6 character',
       'Code character': 'The code can only contain\
 lower case character and digits',
       'Code unique': 'This code is already used'}


class GetCustomURLForm(FlaskForm):
    url = StringField(
        'URL',
        validators=[DataRequired(),
                    URL(require_tld=False, message=msg['URL'])])
    customcode = StringField(
        'Code',
        validators=[DataRequired(),
                    Length(min=1, max=6, message=msg['Code length'])])
    submit = SubmitField('Submit')

    def validate_customcode(self, customcode):
        if re.match("^[\da-z]+$", customcode.data) is None:
            raise ValidationError(msg['Code character'])
        c = Code.query.filter_by(code=customcode.data).first()
        if c is not None:
            raise ValidationError(msg['Code unique'])


class GetURLForm(FlaskForm):
    url = StringField(
        'URL',
        validators=[DataRequired(),
                    URL(require_tld=False, message=msg['URL'])])
    submit = SubmitField('Get code')
