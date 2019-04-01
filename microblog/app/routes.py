from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kirill'}
    posts = [
        {
            'author': {'username': 'Bob'},
            'body': 'Need more beer'
        },
        {
            'author': {'username': 'Tim'},
            'body': 'I like apples'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)