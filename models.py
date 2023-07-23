from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


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
    image_url = db.Column(db.String(1000), nullable = False,
                           default = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/450px-No_image_available.svg.png")