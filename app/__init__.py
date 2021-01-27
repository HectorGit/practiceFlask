from flask import Flask 

app = Flask(__name__)

from app import routes #imported at the bottom not at the top of the file !