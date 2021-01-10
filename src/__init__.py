from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from src.config import BaseConfig


# config

app = Flask(__name__)
app.config.from_object(BaseConfig)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from src.models.user import User
from src.models.pointer import Pointer

@app.route('/', methods=['GET'])
def index():    
    return 'I am working'

@app.route('/api/register', methods=['POST'])
def register():
    json_data = request.json
    user = User(
        email=json_data['email'],
        password=json_data['password']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'this user is already registered'
    db.session.close()
    return jsonify({'result': status})


@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(
            user.password, json_data['password']):
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'status': True})
    else:
        return jsonify({'status': False})


@app.route('/api/getareapointers', methods=['GET'])
def getAreaPointers():
            longSize = 0.005
            latSize = 0.02
            userLong = float(request.args.get('long'))
            userLat = float(request.args.get('lat'))

            if userLong and userLat: 
                pointersQuery = Pointer.query.filter((Pointer.longitude >= userLong - longSize) & (Pointer.longitude <= userLong + longSize) & (Pointer.latitude >= userLat - latSize) & (Pointer.latitude <= userLat + latSize))

                return jsonify([i.serialize for i in pointersQuery.all()])
            else:
                return badRequest('Location params cannot be empty')

@app.route('/api/addPointer', methods=['POST'])
def addPointer():
    json_data = request.json
    pointer = Pointer(
        description=json_data['description'],
        longitude=json_data['longitude'],
        latitude = json_data['latitude'],
        created_by = json_data['created_by']
    )
    try:
        db.session.add(pointer)
        db.session.commit()
        status = 'success'
    except Exception as e:
        status = 'Failed to add pointer'
        print(e)
    db.session.close()
    return jsonify({'result': status})


def unauthorized():
    response = jsonify({'message':'please log in'})
    return response, 401

def badRequest(message):
    response = jsonify({'message':message})
    return response, 404