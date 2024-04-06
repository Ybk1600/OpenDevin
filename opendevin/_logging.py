import logging, os, sys
from time import strftime
import traceback

# Set up logging
logging.basicConfig(level=logging.INFO)

#def log_uncaught_exceptions(ex_cls, ex, tb):
#    logging.error(''.join(traceback.format_tb(tb)))
#    logging.error('{0}: {1}'.format(ex_cls, ex))

#sys.excepthook = log_uncaught_exceptions
