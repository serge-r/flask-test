from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm
import opnssl

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname': 'Serge'}

	posts = [ 
		{
			'author': {'nickname': 'John'},
			'body': 'Hi everyone'
		},
		{
			'author': {'nickname':'Not Johnn'},
			'body': 'By everyone'
		}
	]

	return render_template ('index.html',
				title='Home Flask COOL',
				user=user,
				posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % 
				(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')

	return render_template('login.html',
							title='Home Flash - Login',
							form=form)

@app.route('/certs')
def certs():
	indexFile = app.config['OPNSSL_INDEX']
	certs = opnssl.parseIndex(indexFile)

	return render_template('certs.html',
							title='Active certs',
							certs=certs)
