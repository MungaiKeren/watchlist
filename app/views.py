from flask import render_template
from app import app

# views
@app.route('/')
def index():
    '''
    view root function that returns the index page and gets its data
    '''
    title = 'Home - welcome to the best movie review website'
    message = 'Hello World'
    return render_template('index.html',title = title, message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)