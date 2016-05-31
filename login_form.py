from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class loginform(Form):
	username = StringField(u'User Name: ',validators=[InputRequired(),Length(max=30)])
	password = PasswordField(u'Password: ',validators=[Length(min=1,max=16)])


		
