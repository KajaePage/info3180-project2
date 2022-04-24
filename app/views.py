"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
import os
from flask import render_template, request, redirect, url_for, flash,jsonify
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app.forms import LoginForm,RegisterForm,CarForm
from app.config import Config
from app.models import users,cars,favourites
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from datetime import datetime,timedelta
import jwt
from functools import wraps
from sqlalchemy import or_,and_

blacklist = {}
def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, Config.SECRET_KEY)
            user = users.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/register', methods = ['POST'])
def register():
    print(request.headers.get('X-CSRF-TOKEN'))
    print('------ {0}'.format(request.form))
    form = RegisterForm()
    form.username.data = request.form.get("username")
    form.password.data = request.form.get("password")
    form.name.data = request.form.get("name")
    form.email.data = request.form.get("email")
    form.locat.data = request.form.get("location")
    form.bio.data = request.form.get("biography")
    date_reg = datetime.now()
    if(request.files['photo']):
        form.photo.data = request.files['photo']
    else:
        return jsonify(errors = form_errors(form))
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save(app.config['UPLOAD_FOLDER'] + '/' + filename)
        user = users(form.username.data,form.password.data,form.name.data,form.email.data,form.locat.data,form.bio.data,date_reg,filename)
        db.session.add(user)
        db.session.commit()  
    else:
        return jsonify(errors = form_errors(form))
    return jsonify(user = user.to_dict())


@app.route('/api/auth/login', methods = ['POST'])
def login():
    form = LoginForm()
    print(request.form)
    print(Config.SECRET_KEY)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            
            user = users.authenticate(username, password)
            if not user:
                return jsonify(errors = "Username or Password Incorrect", Authorization = False)
            else:
                # if(user.id in blacklist.keys()):
                #     return jsonify({ 'token': blacklist[user.id], 'message': 'Logged in Successfully', 'id': user.id})
                # else:
                token = jwt.encode({
                    'sub': user.username,
                    'iat':datetime.utcnow(),
                    'exp': datetime.utcnow() + timedelta(minutes=1540)},
                    Config.SECRET_KEY)
                print(token)
                return jsonify({ 'token': token.decode('UTF-8'), 'message': 'Logged in Successfully', 'id': user.id})
                
        else:
            return jsonify(errors = form_errors(form))


@app.route('/api/auth/logout', methods = ['POST'])
@token_required
def logout(user):
    print(user)
    return jsonify({'message': 'Logged out Successfully'})



@app.route('/api/cars', methods = ['POST'])
@token_required
def add_car(user):
    print(request.headers.get('X-CSRF-TOKEN'))
    print('------ {0}'.format(request.form))
    form = CarForm()
    form.make.data = request.form.get("make")
    form.model.data = request.form.get("model")
    form.colour.data = request.form.get("colour")
    form.transmission.data = request.form.get("transmission")
    form.year.data = request.form.get("year")
    form.price.data = request.form.get("price")
    form.car_type.data = request.form.get("car_type")
    form.desc.data = request.form.get("desc")
    if(request.files['photo']):
        form.photo.data = request.files['photo']
    else:
        return jsonify(errors = form_errors(form))
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save(app.config['UPLOAD_FOLDER'] + '/' + filename)
        car = cars(user.id,form.desc.data,form.make.data,form.model.data,form.price.data,form.colour.data,form.year.data,form.transmission.data,form.car_type.data,filename)
        db.session.add(car)
        db.session.commit()  
    else:
        return jsonify(errors = form_errors(form))
    return jsonify(car = car.to_dict(),message = "Car created Successfully!")

@app.route('/api/cars', methods = ['GET'])
def display_car():
    carl = cars.query.all()
    return jsonify(carlist = [i.to_dict() for i in carl])

@app.route('/api/cars/<car_id>', methods = ['GET'])
def carsf(car_id):
    car_id = request.args.get('id')
    cardata = cars.query.filter_by(id=car_id).first()
    return jsonify(messgae= "Car found", car_data=cardata.to_dict())


@app.route('/api/cars/<car_id>/favourite', methods = ['POST'])
@token_required
def carsfav(curr_user,car_id):
    try:
        carid = request.args.get('car_id')
        if favourites.query.filter(and_(favourites.car_id==carid, favourites.user_id==curr_user.id)).first():
            return jsonify(errors = ["Already in your favourites!"])
        fav = favourites(carid,curr_user.id)
        db.session.add(fav)
        db.session.commit()
        return jsonify(car = fav.to_dict(),message = "Car created Successfully!")
    except Exception as e:
        print(e)
        return jsonify(errors = ["Failed to add car to favourites"])

@app.route('/api/search', methods = ['GET'])
@token_required
def searchl(user):
    make = request.args.get('make')
    model = request.args.get('model')
    print(make)
    print(model)
    if model and not make:
        make = "ksdgwot939grfuwydwcdwjgdajda"
    elif make and not model:
        model = "ksdgwot939grfuwydwcdwjgdajda"
    elif not make and not model:
        make = ''
        model = ''
    try:
        res = cars.query.filter(or_(cars.model.like(model),cars.make.contains(make))).all()
        print(res)
        return jsonify(carlist = [i.to_dict() for i in res])
    except Exception as e:
        print(e)
    return None

@app.route('/api/users/<user_id>', methods = ['GET'])
@token_required
def userdatap(user,user_id):
     if request.method == 'GET':
         return jsonify(messgae= "User found", user_data=user.to_dict()) 



@app.route('/api/users/<user_id>/favourites', methods = ['GET'])
@token_required
def userfav(user,user_id):
     print('here')
     if request.method == 'GET':
         us = user.to_dict()
         print(us)
         favs = favourites.query.filter_by(user_id=us['id']).all()
         favdict = [i.to_dict() for i in favs]
         favcar=[]
         for f in favdict:
             favcar.append(cars.query.filter_by(id=f['cid']).first().to_dict())
             print(favcar)    
         return jsonify(messgae= "Favourites found",favdata=favcar) 
     return jsonify(errors = ['Error Uploading'])
###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")