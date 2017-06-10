from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir))
app = Flask(__name__)
app.config['DEBUG'] = True

info_form = """<style>
            .error {{ color: red;}}
            </style>
             <form action="/" >
             <h1>Sign up</h1>
                <label>Username</label>
                    <input name="username" type="text" value='{username}' />
                    <p class="error">{username_error}</p>
                <label>Password</label>
                    <input type="text" name="password" value='{password}' />
                    <p class="error">{password_error}</p>
                <label>Verify Password</label>
                    <input type="text" name="verify" value='{verify}' />
                    <p class="error">{verify_error}</p>
                <label for="email">E-mail (Optional)</label>
                    <input type="text" name="email" value='{email}' />
                    <p class="error">{email_error}</p>
                <input type="submit"/>
             </form>
          </html>
             """





@app.route('/')
def display_info_form():
    return info_form.format(username='', username_error='', password='', password_error='',
        verify='', verify_error='', email='', email_error='')




@app.route('/', methods=['POST'])
def validate_info_form():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username < 3:
        username_error = 'Not a valid username'
        username = ''
    else:
        if username.strip() == ' ':
            username_error = "Not a valid username"
            username_error = ''


    if not username_error:
        return "success"
    else:
        return info_form.format(username_error=username_error)


"""
@app.route('/valid-info', methods=['POST'])
def valid_info():



    if password < 3 or password > 20:
        error
    if password != verify:
        error
    if username or password or verify or email == "":
        error
    if username or password or verify or email == " ":
        error
    if email and email < '@.' or email == " ":
        error
"""
app.run()
