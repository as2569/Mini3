from app import login
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), index=True, unique=True)
	password = db.Column(db.String(100))

	def __repr__(self):
		return '<User {}'.format(self.username)

	def set_password(self, password):
		self.password = password

	def check_password(self, password):
		return self.password

class Record(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	record = db.Column(db.String(100))
	def __repr__(self):
		return 'Record {}'.format(self.record)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
