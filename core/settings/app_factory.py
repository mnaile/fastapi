import os
import logging
from logging.config import dictConfig

from core.settings.settings import Base
from core.settings.devsettings import DevSettings
from core.settings.prodsettings import ProdSettings


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
log_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        "simpleFormatter":{
            "format": '%(asctime)s %(name)s - %(levelname)s:%(message)s'
        },
        "normalFormatter": {
            "format": "%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s"
        },
        "detailedFormatter":{
            "format": "%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s   call_trace=%(pathname)s L%(lineno)-4d"
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'fileHandler': {
            'level': 'DEBUG',
            'filename': 'logfile.log',
            'class': 'logging.FileHandler',
            'formatter': 'simpleFormatter'
        },
        "consoleHandler":{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'normalFormatter',
            "stream": "ext://sys.stdout"

        },
        "detailedConsoleHandler":{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'detailedFormatter',
            "stream": "ext://sys.stdout"

        }
    },
    'loggers': {
        '': {
            'handlers': ['fileHandler',"detailedConsoleHandler","consoleHandler", "default"],
            'level': 'INFO',
            'propagate': True
        },
    }
}
dictConfig(log_dict)
logger = logging.getLogger(__name__)


def get_settings():
    settings = os.environ.get("settings")

    if settings == "dev":
        return DevSettings()

    elif settings == "prod":
        return ProdSettings

    raise Exception("Please export settings either dev, test or prod")

settings = get_settings()


