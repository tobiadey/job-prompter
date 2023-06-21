import os

# Disabled for performance and to avoid deprecation messages
SQLALCHEMY_TRACK_MODIFICATIONS = False

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
