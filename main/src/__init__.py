from flask import Flask

myapp_obj = Flask(__name__)

from src.routes import routes