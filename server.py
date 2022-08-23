
import database.User as user
from flask import Flask, request, abort, jsonify, send_file,redirect
# from flask_socketio import SocketIO
import json
from flask_cors import CORS
from flask_socketio import SocketIO, emit
#pip install eventlet
#跨服務域需要使用cors

app = Flask(__name__)
async_mode = None
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
name_space = '/websocket'

@app.route('/')
def hi():
    return "hi"


@app.route('/home')
def show_user():
    data = user.show_data()
    return data

@app.route('/delete/<sid>')
def delete_user(sid):
    return user.delete_data(sid)
    

@app.route('/add',methods=['POST','GET'])
def insert_user():
    json_data = request.get_json()
    print(request.get_json())
    std_id = json_data.get('studentid')
    std_name = json_data.get('studentname')
    std_class = json_data.get('class')
    year = json_data.get('year')
    return user.insert_data(std_id,std_name,std_class,int(year))


@app.route('/showone/<sid>')
def show_one_user(sid):
    data = user.show_one_data(sid)
    return data

@app.route('/update',methods=['POST','GET'])
def update_user():
    json_data = request.get_json()
    print(request.get_json())
    std_id = json_data.get('studentid')
    std_name = json_data.get('studentname')
    std_class = json_data.get('class')
    year = json_data.get('year')
    return user.update_data(std_id,std_name,std_class,int(year))


if __name__ == "__main__":
    # #nfc = subprocess.Popen(["python", "main"])
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
    # app.run()
    