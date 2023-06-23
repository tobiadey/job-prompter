import sys
import os
import logging
from job_prompter import create_app

# Initialise logging - has to be done before other libraries do it
#   Notice: LOG_LEVEL value has to be a NAME of the eligible logging levels according to:
#   https://docs.python.org/3/howto/logging.html#logging-levels
logging.basicConfig(stream=sys.stdout, level=os.environ.get("LOG_LEVEL", logging.INFO))

application = create_app()
