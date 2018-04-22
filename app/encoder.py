#!/usr/bin/env python

from app.models import Shorten_URL

digits = "0123456789abcdefghijklmnopqrstuvwxyz"
base = len(digits)


def encode(num):
    code = ""
    while num != 0:
        code = digits[num % base] + code
        num = num // base
    return code


def code_generator():
    i = len(Shorten_URL.query.all()) + 1
    j = 1
    code = encode(i)
    while Shorten_URL.query.filter_by(code=code).first() is not None:
        i += j
        j += 1
        code = encode(i)
    return code
