from app import app #means to get the app flask intance from the /app package
#from flask import render_template, jsonify #what other flask things do we need ?
from flask import render_template, flash, redirect, url_for, request, jsonify, \
make_response, session, Response
import requests
import json #why is this not in the requirements.txt file ???
#how do we get Jinja2?

# ------------------------------- GLOBAL VARIABLES --------------------------

# API_URL = app.config['API_ROUTE']

# ------------------------------- GLOBAL VARIABLES --------------------------


@app.route('/')
@app.route('/index')
def index():
    return render_template('index/index.html') #here usually we would return some sort of a template, and possibly pass it some data if necessary 

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/applications')
def applications():
    return render_template('applications/applications.html')

@app.route('/blog')
def blog():
    return render_template('blog/blog.html')

@app.route('/contact')
def contact():
    return render_template('contact/contact.html')

@app.route('/join')
def join():
    return render_template('join/join.html')

@app.route('/technology')
def technology():
    return render_template('technology/technology.html')

# @app.route('/simple_test')
# def simple_test():
#     users = [{'username':'Hector'}, {'username':'Sergio'}]
#     return render_template('other/simple_test.html', users=users, title='Home')

# @app.route('/friend')
# def friend():
#     url = API_URL + '/read_friend'
#     data = {
#         'first_name': 'jordie'
#     }
#     r = requests.get(url, data=data)
#     friend = r.json() 
#     if r.status_code == 200:
#         print('was able to retrieve friend from API')
#         print(friend) 
#     else:
#         print('unable to retrieve friend from API')
#         print('r: ', r)
#     return render_template('other/friend.html', friend = friend)

# @app.route('/friends')
# def friends():
#     url = API_URL + '/read_all_friends' 
#     r = requests.get(url)
#     friends = r.json() 
#     if r.status_code == 200:
#         print('was able to retrieve friend from API')
#         print(friends) 
#     else:
#         print('unable to retrieve friend from API')
#         print('r: ', r)
#     return render_template('other/friends.html', friends = friends)