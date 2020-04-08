from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from flask  import current_app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from flask import request
from app.calculator import Calculator

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template('index.html', title='Home Page')

@app.route('/calculator')
def calculator():
	session['step'] = 0
	session['num1s'] = ''
	session['num2s'] = ''
	session['num1i'] = 0
	session['num2i'] = 0
	session['numResult'] = 0
	session['operand'] = 0
	return render_template('calculator.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
	display = ''
	buttonType = request.form['buttonType']
	buttonValue = request.form['buttonValue']
	if buttonType == 'd':
		if session['step'] == 0:
			session['num1s'] = session['num1s'] + buttonValue
			display = request.form['display'] + buttonValue
		if session['step'] == 1:
			session['num2s'] = session['num2s'] + buttonValue
			display = request.form['display'] + buttonValue
	if buttonType == 'o':
#		if session['step'] == 0:
#			session['num1i'] = int(session['num1s'])
		#if session['step'] == 2:
		#	session['num2i'] = int(session['num2s'])
		session['step'] = 1
		session['operand'] = buttonValue
		display = request.form['display'] + " " + session['operand'] + " "
	if buttonType == "=":
		if session['step'] == 1:
			num1i = int(session['num1s'])
			num2i = int(session['num2s'])
			if session['operand'] == "+":
				calc = Calculator()
				numResult = calc.add(num1i, num2i)
				#numResult = calc.add(session['num1i'], session['num2i'])
			#display = request.form['display'] + " " + str(numResult)
			display = str(numResult)
		else:
			display = request.form['display']

	#result = request.form['display'] + buttonValue
	#result = display
	return display

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(url_for(next_page))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('You are registered')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)
