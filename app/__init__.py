from flask import Flask #, flash, redirect, url_for, session, request
from config import Config

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config) #I think this should work ? 
bootstrap = Bootstrap(app)

# app.jinja_env.globals.update(API_ROUTE=app.config['API_ROUTE'])
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

from app import routes #imported at the bottom not at the top of the file !