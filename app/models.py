from . import db

class Cars(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Cars'

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

class Favourites(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Favourites'

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

class Users(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    location = db.Column(db.String(512))
    biography = db.Column(db.String(512))
    date_joined = db.Column(db.Date())
    photo = db.Column(db.String(128))

    def __init__(self, username, password, name, email, location, biography, date_joined, photo):
            self.username = username
            self.password = password
            self.name = name
            self.email = email
            self.location = location
            self.biography = biography
            self.date_joined = date_joined
            self.photo = photo


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
