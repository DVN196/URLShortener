#!/usr/bin/env python

from app.models import Code
import string

digits = string.digits + string.ascii_lowercase
base = len(digits)
max_value = base ** 6


def encode(num):
    code = ""
    while num != 0:
        code = digits[num % base] + code
        num = num // base
    return code


def code_generator():
    i = Code.query.count() + 1
    j = 1
    code = encode(i)
    while Code.query.filter_by(code=code).first() is not None:
        i += j
        i = i % max_value
        j += 1
        code = encode(i)
    return code
