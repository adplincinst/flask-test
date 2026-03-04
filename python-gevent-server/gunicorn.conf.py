# gunicorn.conf.py
import multiprocessing

# 1. Server Socket
bind = "0.0.0.0:5009"

# 2. Worker Strategy
# Use 'gevent' for "implicit" asynchrony
worker_class = 'gevent'

# Number of worker processes (usually 2 x cores + 1)
workers = 3 # multiprocessing.cpu_count() * 2 + 1

# Maximum number of simultaneous clients per worker
worker_connections = 1000

# 3. Logging
accesslog = "-"  # Log to stdout
access_log_format = '%(t)s | PID:%(p)s | %(s)s | "%(r)s" %(L)ss'
errorlog = "-"
loglevel = "info"

# 4. Lifecycle
timeout = 30  # Should be greater than your longest sleep (10s)
keepalive = 2

