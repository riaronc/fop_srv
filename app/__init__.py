import logging
import sys

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

cors = CORS(app)
db = SQLAlchemy(app=app)

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(pathname)s/%(funcName)s: %(message)s')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

root.addHandler(handler)

from app.api import api_bp as api_bp_v1

app.register_blueprint(api_bp_v1, url_prefix='/api/v1')

# from app import errors
