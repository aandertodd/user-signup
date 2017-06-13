from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def display_info_form():
    template = jinja_env.get_template('base.html')
    return template.render()



@app.route('/', methods=['POST'])
def validate_info_form():

    template = jinja_env.get_template('base.html')
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    #Username verifier
    if ' ' in username or (len(username)) < 3 or (len(username)) > 20:
        username_error = 'Not a valid username'
        username = ''

    if ' ' in password or (len(password)) < 3 or (len(password)) > 20:
        password_error = 'Not a valid password'
        password = ''

    if verify != password:
        verify_error = 'Passwords do not match'
        verify = ''

    if email != '':
        if '@' not in email or '.' not in email:
            email_error = 'Not a valid e-mail'
            email = ''
    #success message
    if not username_error and not password_error and not verify_error and not email_error:
        welcome_user = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return template.render(username_error=username_error, password_error=password_error,
        verify_error=verify_error, email_error=email_error,
        username=username, password=password, verify=verify, email=email)

@app.route('/welcome')
def valid_info():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

app.run()
