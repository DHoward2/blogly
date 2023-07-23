from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petdog1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')

@app.route('/users')
def user_listings():
    """Show list of users"""

    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users', methods=['POST'])
def user_form():
    """Form to add new user"""
    

    new_user = User(first_name=request.form["first_name"], 
                    last_name=request.form["last_name"], 
                    image_url=request.form["image_url"] or None)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/{new_user.id}")

@app.route('/users/<int:user_id>')
def user_details(user_id):
    """Show user Details"""

    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)

@app.route('/users/<int:user_id>/edit')
def user_edit_form(user_id):
    """Show user edit page"""
    user = User.query.get_or_404(user_id)
    return render_template('user_edit.html',user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def user_edit(user_id):
    """User edit Form"""
    user = User.query.get_or_404(user_id)

    user.first_name=request.form["first_name"]
    user.last_name=request.form["last_name"]
    user.image_url=request.form["image_url"]
    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user.id}")

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def user_delete(user_id):
    """Delete user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return redirect('/users')