#!/usr/bin/env bash

flask db init
flask db migrate -m "url table"
flask db upgrade
flask db migrate -m "shorten_url table"
flask db upgrade
