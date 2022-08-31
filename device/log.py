import logging
import os
import sys
from datetime import datetime
from logging import FileHandler, Logger

log_filename = os.path.dirname(os.path.realpath(__file__)) + \
               '/logs/device_error_log-' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'


def initialize_logger(logger: Logger, filename: str = 'logs/device_error.log',
                      encoding: str = 'utf-8') -> Logger or None:
    if filename is None:
        return None

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(message)s', '%H:%M:%S')

    fh = FileHandler(filename, encoding=encoding)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler(stream=sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


log = initialize_logger(Logger(__name__), log_filename)
