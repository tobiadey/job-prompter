# Gunicorn production settings

# Expose to the world
bind = "0.0.0.0:8000"

# Use async workers
worker_class = "gevent"

# Recommended at least the number of CPUs
# Come back to this
workers = 3

# Gunicorn logging to stdout
accesslog = "-"
errorlog = "-"

# Include output from the application
capture_output = True
