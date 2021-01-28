from app import app #means to get the app flask intance from the /app package
#from flask import render_template, jsonify #what other flask things do we need ?
from flask import render_template, flash, redirect, url_for, request, jsonify, \
make_response, session, Response
import requests
import json #why is this not in the requirements.txt file ???
#how do we get Jinja2?

# ------------------------------- GLOBAL VARIABLES --------------------------

API_URL = app.config['API_ROUTE']

# ------------------------------- GLOBAL VARIABLES --------------------------


@app.route('/')
def index():
    return "Hello, World!" #here usually we would return some sort of a template, and possibly pass it some data if necessary 

@app.route('/index')
def simple_test():
    users = [{'username':'Hector'}, {'username':'Sergio'}]
    return render_template('index.html', users=users, title='Home')

@app.route('/friend')
def friend():
    #in the flask app we have an api_handlers.py file, where this is streamlined, but at this moment i just want to try if i can make it work just like this ... 
    url = API_URL + '/read_friend' #not sure if this is the route that actually exists ? 
    # we can make another endpoint in the api 
    data = {
        'first_name': 'jordie'
    }
    r = requests.get(url, data=data)
    friend = r.json() #not sure if this would work
    if r.status_code == 200:
        #flash(r.json()['message'], 'success')
        print('was able to retrieve friend from API')
        print(friend) #expect to print form in json ...
    else:
        #flash(r.json()['message'], 'danger')
        print('unable to retrieve friend from API')
        print('r: ', r)
    return render_template('friend.html', friend = friend)

@app.route('/friends')
def friends():
    #in the flask app we have an api_handlers.py file, where this is streamlined, but at this moment i just want to try if i can make it work just like this ... 
    url = API_URL + '/read_all_friends' #not sure if this is the route that actually exists ? 
    # we can make another endpoint in the api 
    r = requests.get(url)
    friends = r.json() #not sure if this would work
    if r.status_code == 200:
        #flash(r.json()['message'], 'success')
        print('was able to retrieve friend from API')
        print(friends) #expect to print form in json ...
    else:
        #flash(r.json()['message'], 'danger')
        print('unable to retrieve friend from API')
        print('r: ', r)
    return render_template('friends.html', friends = friends)