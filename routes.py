from flask import Flask, render_template,redirect,flash,abort,url_for,request, session
from login_form import loginform
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.principal import Principal, Permission, Identity, AnonymousIdentity
from flask.ext.principal import RoleNeed, UserNeed, identity_loaded, identity_changed
from models import db, user

from models import load_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nikhil'  #need to be changed

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@127.0.0.1/test'

db.init_app(app)

with app.test_request_context():
   load_db(db)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(username):
	return user.query.get(username)

principal = Principal()
principal.init_app(app)

administrator_permission = Permission(RoleNeed('administrator'))
team_member_permission = Permission(RoleNeed('team member'))
project_manager_permission = Permission(RoleNeed('project manager'))
client_permission = Permission(RoleNeed('client'))

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
	identity.user = current_user

	if hasattr(current_user, 'roles'):
		for role in current_user.roles:
			identity.provides.add(RoleNeed(role.rolename))

# ----------------------------------Home-----------------------------------
@app.route('/')
def home():
	return render_template('home/pages/home.html')

@app.route('/client login/')
@login_required
@client_permission.require(http_exception=403)
def clientLogin():
	return render_template('home/pages/client login.html')

@app.route('/project manager login/')
@login_required
@project_manager_permission.require(http_exception=403)
def projectManagerLogin():
	return render_template('home/pages/project manager login.html')

@app.route('/team member login/')
@login_required
@team_member_permission.require(http_exception=403)
def teamMemberLogin():
	return render_template('home/pages/team member login.html')

@app.route('/administrator login/')
@login_required
@administrator_permission.require(http_exception=403)
def adminstratorLogin():
	return render_template('home/pages/administrator login.html')

# -------------------------------------------------------------------------

@app.route("/login",methods=['GET','POST'])
def login():
		form = loginform()

		if request.method == 'GET':
			return render_template('login.html',form=form)

	
	
		username = form.username.data
		password = form.password.data
	
		user_accessed = user.query.filter_by(username=username).first()
	
		if user_accessed is None:
			flash(u'Username is incorrect')  # to log incorrect username
			return redirect(url_for('login'))
	
		if not user_accessed.verify_password(password):
			flash(u'Password is incorrect')  # to log incorrect password
			return redirect(url_for('login'))
		
		if not user_accessed.active:
			flash(u'Your account is inactive')  # to log inactive user
			return redirect(url_for('login'))
	
		login_user(user_accessed)

		identity_changed.send(app, identity=Identity(user_accessed.username))
		return redirect(url_for('home'))

@app.route("/logout")
@login_required
def logout():
	logout_user()

	for key in ('identity.name', 'identity.auth_type'):
		session.pop(key, None)

	identity_changed.send(app, identity=AnonymousIdentity())
	return redirect(url_for('home'))

@app.errorhandler(403)
def unauthorized(e):
    session['redirected_from'] = request.url
    flash('You have no permissions to access this page')
       # Google "Flask message flashing fails across redirects" to fix this
    return redirect(url_for('login'))



if __name__ == '__main__':
	app.run(debug = True)
	app.config['SQLALCHEMY_ECHO'] = True


