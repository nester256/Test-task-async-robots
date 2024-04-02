""" Defines a function to initialize and configure loggers for the application. """
import logging


def init_logger(name: str) -> None:
    """
    Initializes and configures a logger with specified settings.

    Args:
    - name (str): Name of the logger.
    """
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.debug('logger was initialized')


api_logger = logging.getLogger('API')
