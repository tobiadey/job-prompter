# Gunicorn development settings

# Bind to localhost only
bind = "127.0.0.1:5000"

# Use async workers
worker_class = "gevent"

# Gunicorn logging to stdout
accesslog = "-"
errorlog = "-"

# Include output from the application
capture_output = True

# Reload code on changes
reload = True

# Environment variables
env = "FLASK_DEBUG = 1"
