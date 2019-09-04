from flask import render_template
from app import app
from .request import get_movies

# views
@app.route('/')
def index():
    '''
    view root function that returns the index page and gets its data
    '''
    # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    upcoming_movie = get_movies('upcoming')
    print(upcoming_movie)
    now_showing_movie = get_movies('now_playing')
    print(now_showing_movie)
    title = 'Home - welcome to the best movie review website'
    return render_template('index.html',title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)