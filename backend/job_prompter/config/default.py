import os

# Disabled for performance and to avoid deprecation messages
SQLALCHEMY_TRACK_MODIFICATIONS = False

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


SESSION_TYPE = "redis"
SESSION_PERMANENT = False

# Redis configuration
REDIS_CACHE_URL = "redis://localhost:6379"
REDIS_QUEUE_URL_PLATFORM = "redis://localhost:6379"
