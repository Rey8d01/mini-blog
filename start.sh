#!/bin/sh
python -m startup
export FLASK_APP=main && flask openapi write ./tmp/openapi.json
gunicorn main:app -b 0.0.0.0:80 -w 2 --log-level error --access-logfile - --max-requests 500
