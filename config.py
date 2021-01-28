
import os

class Config(object):
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/h_practice' 
    API_ROUTE = os.environ.get('API_ROUTE') or 'http://localhost:5001' #make sure hector-practice-api is running on localhost:5001
    FLASK_CONFIG =  os.environ.get('FLASK_CONFIG') or 'localhost'
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
