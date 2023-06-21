"""
Default configuration variables
"""

import os
import sys
from importlib import import_module

# Configuration is loaded in the following order:
#
# config/default.py – defaults loaded first
# config/environment.py – environment specific overrides (depending on FLASK_ENV)
# config/local.py – local overrides not in version control (if present)

FLASK_ENV = os.environ.get("FLASK_ENV", "development")


def import_star(module_name):
    new_module = import_module(module_name)
    config = sys.modules[__name__]

    for attr in dir(new_module):
        if not attr.startswith("_"):
            value = getattr(new_module, attr)
            setattr(config, attr, value)


# Load default config
import_star("job_prompter.config.default")

# Load per-environment config overrides
import_star("job_prompter.config.{}".format(FLASK_ENV))

# Load local overrides (if present and only in development)
if FLASK_ENV == "development":
    try:
        import_star("job_prompter.config.local")
    except ImportError:
        pass
