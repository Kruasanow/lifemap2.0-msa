from flask import Flask, url_for, render_template, make_response, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db, Events, Users
from flask_restful import Api, Resource, reqparse
from f import is_valid_email, is_valid_phone ,is_valid_username, is_valid_name, is_valid_birthday, is_valid_sex
from datetime import datetime

app = Flask(__name__)
CORS(app) 

load_dotenv()
DBUSER = os.getenv("DBUSER")
DBUSERPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DB = os.getenv("DB")
SECRETKEY = os.getenv("SECRETKEY")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DBUSER}:{DBUSERPASSWORD}@{DBHOST}:{DBPORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRETKEY

db.init_app(app)
api = Api(app)

    
class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        names = data.get('names')
        sname = data.get('sname')
        email = data.get('email')
        passwords = data.get('passwords')
        secrets = data.get('secrets')
        tg = data.get('tg')
        birthday = data.get('birthday')
        sex = data.get('sex')
        phone = data.get('phone')

        if is_valid_birthday(birthday) == False:
            return make_response(jsonify({'message':'bad birthday'}),419)
        if is_valid_email(email) == False:
            return make_response(jsonify({'message':'bad email'}),419)
        if is_valid_name(names) == False:
           return make_response(jsonify({'message':'bad names'}),419)
        if is_valid_username(username) == False:
            return make_response(jsonify({'message':'bad username'}),419)
        if is_valid_name(sname) == False:
            return make_response(jsonify({'message':'bad sname'}),419)
        if is_valid_sex(sex) == False:
            return make_response(jsonify({'message':'bad sex'}),419)
        if is_valid_phone(sex) == False:
            return make_response(jsonify({'message':'bad phone'}),419)
        

        now = datetime.now()
        try:
            user = Users(
                username=username,
                names=names,
                sname=sname,
                email=email,
                passwords=passwords,
                secrets=secrets,
                tg=tg,
                birthday=birthday,
                roles=0,
                register_date=now.strftime("%d/%m/%Y %H:%M:%S"),
                sex=sex,
                phone=phone
            )
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify({'success':'registred'}),200)
        except Exception as e: # добавить ответ под разные ошибки
            return make_response(jsonify({'message':f'error - {e}'}),411)
        
class Login(Resource):
    def post(self):
        data = request.get_json()

        login = data.get('login')
        password = data.get('password')

        from_db_logins = Users.query.all()
        for item in from_db_logins:
            if login in [item.username, item.tg, item.email, item.phone]:
                if password == item.passwords:
                    return make_response(jsonify({'message':'login success'}),200)
                
        return make_response(jsonify({'message':'bad login'}),423)
    
class AddMemoryPlace(Resource):
    def post(self):
        data = request.get_json()  
        try:
            event = Events(
                locations = data.get('location'),
                coordinates_latitude = data.get('latitude'),
                coordinates_longitude = data.get('longitude'),
                img_ways = data.get('img'),
                descriptions = data.get('description'),
                short_description = data.get('short'),
                story = data.get('story'),
                privates = data.get('privates'),
                email = data.get('email') # Должен буду держать в сессии
            )

            db.session.add(event)
            db.session.commit()
            return make_response(jsonify({'message':'event added'}),200)
        except Exception as e:
            return make_response(jsonify({'message':f'error - {e}'}),400)

class DelEvent(Resource):
    def delete(self):
        data = request.get_json()
        name = data.get('description')
        email = data.get('email')

        try:
            event = Events.query.filter_by(email=email, descriptions=name).first()
            if event:
                db.session.delete(event)
                db.session.commit()
                return make_response(jsonify({'message':'event deleted'}),200)
            else:
                return make_response(jsonify({'message':'event did not found'}),400)
        except Exception as e:
            return make_response(jsonify({'message':f'error - {e}'}),400)
        
class ChangeEvent(Resource):
    def put(self):
        data = request.get_json()

        try:
            changes = Events.query.filter_by(descriptions=data.get('name')).first()
            for i, j in data.items():
                if hasattr(changes, i):
                    setattr(changes, i, j)
            db.session.commit() # разные поля обновил
            return make_response(jsonify({'message':'data changed', 'data':data}))
        except Exception as e:
            return make_response(jsonify({'message':f'error - {e}'}))
         
class DelAcc(Resource):
    def delete(self):
        data = request.get_json()
        username = data.get('username')
        passwords = data.get('passwords')
        secrets = data.get('secrets')

        try:
            users = Users.query.filter_by(username=username, passwords=passwords, secrets=secrets).first()
            if users:
                db.session.delete(users)
                db.session.commit()
                return make_response(jsonify({'message':'user deleted'}),200)
            else:
                return make_response(jsonify({'message':'user did not found'}),400)
        except Exception as e:
            return make_response(jsonify({'message':f'error - {e}'}),400)

class ChangeAcc(Resource):
    def put(self):
        data = request.get_json()

        try:
            changes = Users.query.filter_by(username=data.get('username')).first()
            for i, j in data.items():
                if hasattr(changes, i):
                    setattr(changes, i, j)
            db.session.commit() # разные поля обновил
            return make_response(jsonify({'message':'data changed', 'data':data}))
        except Exception as e:
            return make_response(jsonify({'message':f'error - {e}'}))

class AddFriend(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        friends = data.get('friends')

        user_friends = Users.query.filter_by(username=username).first()

        if friends in user_friends.friends:
            return make_response(jsonify({'message':"user already exists"}))
        try:
            if user_friends.friends == None:
                user_friends.friends = friends
            else:
                user_friends.friends = f"{user_friends.friends},{friends}"

            db.session.add(user_friends)
            db.session.commit()

            return make_response(jsonify({'message':f'friends added - {user_friends.friends}'}))
        except Exception as e:
            return make_response(jsonify({'message':f"error - {e}"}))

class DelFriend(Resource):
    def delete(self):
        data = request.get_json()
        username = data.get('username')
        deleted_friend = data.get('friend')

        user = Users.query.filter_by(username=username).first()

        if not user:
            return make_response(jsonify({'message': 'User not found'}), 404)

        user_friends = user.friends

        if not user_friends:
            return make_response(jsonify({'message': 'User has no friends'}), 400)

        list_friends = user_friends.split(',')

        if deleted_friend not in list_friends:
            return make_response(jsonify({'message': 'Friend not found in user\'s friend list'}), 400)

        try:
            list_friends.remove(deleted_friend)
            user.friends = ','.join(list_friends)

            db.session.commit()

            return make_response(jsonify({'new friends': list_friends}), 200)
        except Exception as e:
            return make_response(jsonify({'message':f"{e}"}))


api.add_resource(Register,'/api/register')
api.add_resource(Login,'/api/login')
api.add_resource(AddMemoryPlace,'/api/addevent')
api.add_resource(DelEvent, '/api/delevent')
api.add_resource(ChangeEvent, '/api/changeevent')
api.add_resource(DelAcc, '/api/delacc')
api.add_resource(ChangeAcc, '/api/changeacc')
api.add_resource(AddFriend, '/api/addfriend')
api.add_resource(DelFriend, '/api/delfriend')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)