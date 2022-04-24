from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class cars(db.Model):

    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    colour = db.Column(db.String(32))
    year = db.Column(db.String(8))
    desc = db.Column(db.String(512))
    transmission = db.Column(db.String(32))
    car_type = db.Column(db.String(32))
    price = db.Column(db.Float())
    photo = db.Column(db.String(128))

    def __init__(self, user_id, desc, make, model, price, colour, year, transmission, car_type, photo):
            self.user_id = user_id
            self.desc = desc
            self.make = make
            self.model = model
            self.price = price
            self.colour = colour
            self.year = year
            self.transmission = transmission
            self.car_type = car_type
            self.photo = photo


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)

    def to_dict(self):
        return dict(id=self.id)

class favourites(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())


    def __init__(self, car_id, user_id):
            self.car_id = car_id
            self.user_id = user_id


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)

class users(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(128))
    email = db.Column(db.String(128),unique=True)
    location = db.Column(db.String(512))
    biography = db.Column(db.String(512))
    date_joined = db.Column(db.Date())
    photo = db.Column(db.String(128))
               #(self, user_id, desc, make, model, price, colour, year, transmission, car_type, photo):
    def __init__(self, username, password, name, email, location, biography, date_joined, photo):
            self.username = username
            self.password = generate_password_hash(password, method='pbkdf2:sha256')
            self.name = name
            self.email = email
            self.location = location
            self.biography = biography
            self.date_joined = date_joined
            self.photo = photo


    @classmethod
    def authenticate(cls, usrnm, passw):
        username = usrnm
        password = passw
        
        if not username or not password:
            return None

        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, username=self.username,email=self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
