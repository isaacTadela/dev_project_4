from flask import Flask, request
from db_connector import insert, select, update, delete
import os
import signal
import pymysql

app = Flask(__name__)

# Use CRUD ops on users table
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        result = insert(user_id, user_name)
        
        if result==1:
            return {'status': 'ok', 'user_added': user_name}, 200 # status code
        elif result==2:
            return {'status': 'error', 'reason': 'id already exists'}, 500
        elif result==3:
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
        else:
            return {'status': 'error', 'reason': 'unknown'}, 500
    elif request.method == 'GET':
        result = select(user_id)
        
        if result not in {2, 3, 4}:
            return {'status': 'ok', 'user_name': result}, 200 # status code
        elif result == 2:
            return {'status': 'error', 'reason': 'no such id'}, 500
        elif result == 3:
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
        else:
            return {'status': 'error', 'reason': 'unknown'}, 500

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        result = update(user_id, user_name)
        
        if result == 1:
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        elif result == 2:
            return {'status': 'error', 'reason': 'no such id'}, 500
        elif result == 3:
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
        else:
            return {'status': 'error', 'reason': 'unknown'}, 500

    elif request.method == 'DELETE':
        result = delete(user_id)

        if result == 1:
            return {'status': 'ok', 'user_deleted': user_id}, 200 # status code
        elif result == 2:
            return {'status': 'error', 'reason': 'no such id'}, 500
        elif result == 3:
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
        else:
            return {'status': 'error', 'reason': 'unknown'}, 500


# Stop the server with http request
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


# Home page
@app.route('/')
def home():
    return 'Welcome to the flask server within docker, ' \
           'you can go to "/users/user_id" to search a user in database.'


app.run(host='0.0.0.0', debug=True, port=5000)