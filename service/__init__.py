from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'app': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'app'
        }
    },
    'flask.app': {
        'level': 'INFO',
        'handlers': ['wsgi']
    },
    'root': {
        'level': 'INFO',
    }
})

app = Flask(__name__)

import service.api
