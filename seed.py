from models import User, db
from app import app

# Create All tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
j = User(first_name="John", last_name="Hall")
a = User(first_name="Abby", last_name="Hall")
r = User(first_name="Robin", last_name="Howard")
t = User(first_name="Talleshay", last_name="Carter")
k = User(first_name="Keyshun", last_name="Howard")

users = (j,a,r,t,k)

#Add objects to seesion, so they'll persist
db.session.add_all(users)

#Commit to save to database
db.session.commit()