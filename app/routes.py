from app import app #means to get the app flask intance from the /app package
from flask import render_template #what other flask things do we need ?

#how do we get Jinja2?

@app.route('/')
def index():
    return "Hello, World!" #here usually we would return some sort of a template, and possibly pass it some data if necessary 

@app.route('/index')
def simple_test():
    users = [{'username':'Hector'}, {'username':'Sergio'}]
    return render_template('index.html', users=users, title='Home')