from models import User, db, Post
from app import app

# Create All tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

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

p = Post(title="My First Post", content="Hi, This is my first POST!!!", user_id=1)
p_1 = Post(title="My Second Post", content="Hi, This is my 2nd POST!!!", user_id=1)
p_2 = Post(title="My third Post", content="Hi, This is my 3rd POST!!!", user_id=1)
p2 = Post(title="My First Post", content="Hi, This is my first POST!!!", user_id=2)
p3 = Post(title="My First Post", content="Hi, This is my first POST!!!", user_id=3)
p4 = Post(title="My First Post", content="Hi, This is my first POST!!!", user_id=4)
p5 = Post(title="My First Post", content="Hi, This is my first POST!!!", user_id=5)

posts = (p,p_1,p_2,p2,p3,p4,p5)

db.session.add_all(posts)

db.session.commit()