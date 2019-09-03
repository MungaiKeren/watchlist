from flask import render_template
from app import app

# views
@app.route('/')
def index():
    '''
    view root function that returns the index page and gets its data
    '''
    return render_template('index.html')