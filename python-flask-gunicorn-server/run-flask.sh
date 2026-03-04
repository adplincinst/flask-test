#!/bin/sh

gunicorn --access-logformat '%(L)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s' --access-logfile -  --workers 1 --threads 3 --bind 0.0.0.0:5009 wsgi:APP


