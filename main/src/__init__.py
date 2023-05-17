from flask import Flask #import flask for init

myapp_obj = Flask(__name__) #initialize flask application as myapp_obj to be used in other backend pythonn files

from src import routes #import routes for myapp_obj
