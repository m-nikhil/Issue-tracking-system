from flask.ext.sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt

db = SQLAlchemy()

class user(db.Model):
   username = db.Column(db.String(30),primary_key=True)
   pwhash = db.Column(db.String(300),nullable=False)
   active = db.Column(db.Boolean, nullable=False, default=False)
   roles = db.relationship('Role',backref='user',lazy='dynamic')
   def __init__ (self, username, password, active=False):
   #  self.pwhash = bcrypt.encrypt(password)
      self.pwhash = password
      self.username = username
      self.active = active

   @property
   def is_authenticated(self):
      return True

   @property
   def is_active(self):
      return self.active

   @property
   def is_anonymous(self):
      return False

   def get_id(self):
      return unicode(self.username)

   def verify_password(self, in_password):
    #  return bcrypt.verify(in_password, self.pwhash)
      return in_password == self.pwhash

class Role(db.Model):
   rolename = db.Column(db.String(60),primary_key=True)
   username = db.Column(db.String(30),db.ForeignKey('user.username'),primary_key=True)

# temporary daabase
def load_db(db):
   db.drop_all() 
   db.create_all()
   db.session.add_all(
         [user('admin', 'a',True),
          user('proj', 'p',True),
          user('team', 't',True),
          user('client', 'c',True)]) 
   db.session.commit()
   db.session.add_all(
         [Role(rolename='administrator',username='admin'),
         Role(rolename='project manager',username='proj'),
         Role(rolename='team member',username='team'),
         Role(rolename='client',username='client')])
   db.session.commit()


