import imp
import os
from flask import Flask, request

app = Flask(__name__)

app.config.from_pyfile(os.path.join(".", "config/server_config.cfg"), silent=False)

from app import routes