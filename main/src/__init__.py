#import flask for init
from flask import Flask

#initialize flask application as myapp_obj to be used in other backend pythonn files
myapp_obj = Flask(__name__)

#import routes for myapp_obj
from src import routes
