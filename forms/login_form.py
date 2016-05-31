from wtforms import Form, stringField, PasswordField
from wtforms.valdators import InputRequired, Length

class loginform(object):
	username = StringField(u'User Name: ',valdators=[InputRequired(),Length(max=30)])
	password = PasswordField(u'Password: ',valdators=[Length(min=4,max=16)])


		
		