from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/450px-No_image_available.svg.png"


# class Pet(db.Model):

#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, 
#                    primary_key = True,
#                    autoincrement=True)
#     name = db.Column(db.String(50),
#                      nullable=False,
#                      unique=True)
#     species = db.Column(db.String(30),
#                         nullable=True)
#     hunger = db.Column(db.Integer, nullable=False, default=20)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    image_url = db.Column(db.Text, nullable = False,
                           default = default_image)
    
    posts = db.relationship('Post', backref='user', cascade="all, delete-orphan")
    

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @property
    def read_datetime(self):
        """Returns Formatted DateTime"""

        return self.created_at.strftime("%m/%d/%Y, %H:%M")
        

    