from app import app

from flask import render_template, url_for

@app.route('/')
@app.route('/index')
# @app.route('/index/<name>', methods=['GET'])
def index(name=''):
    hobbies = ['Programming', 'Snowboarding', 'Photography', 'Traveling', 'Video Games']
    return render_template('index.html', title='Home',name='Welcome',hobbies=hobbies)

@app.route('/about_me')
# @app.route('/about_me/<name>', methods=['GET'])
def about_me():
    description = 'My name is Josh hall and I am a Python/C# web developer.  I want to continue to grow in my knowledge of computer languages so that I can be useful in any position that the job needs from me.'
    return render_template('about_me.html', name='About Me', title='About Me', description=description)
