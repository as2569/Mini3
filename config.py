import os
from flask import Flask, session

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'secret'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	TEMPLATES_AUTO_RELOAD = True

	num1s = ''
	num2s = ''
	num1i = 0
	num2i = 0
	numResult = 0
	operand = None
	step = 0

