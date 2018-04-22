#!/usr/bin/env python

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Optional, ValidationError
from app.models import Shorten_URL


class GetCustomURLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL(require_tld=False, message="Not a valid URL")])
    customcode = StringField('Code', validators=[DataRequired()])
    submit = SubmitField('Get code')

    def validate_customcode(self, customcode):
        code = Shorten_URL.query.filter_by(code=customcode.data).first()
        if code is not None:
            raise ValidationError('This code is already used')

        
class GetURLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL(require_tld=False, message="Not a valid URL")])
    submit = SubmitField('Get code')
