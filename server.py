"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
import crud
from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def index():
    """View homepage"""
    
    return render_template("homepage.html")

@app.route('/movies')
def view_all_movies():
    """View a list of all of the movies"""

    movies = crud.get_movies()

    # print(movies)

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie_info(movie_id):
    """Show movie information"""

    movie = crud.get_movie_info(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def view_all_users():
    """View a list of all of the users"""

    users = crud.get_users()

    # print(movies)

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user_info(user_id):
    """Show user information"""

    user = crud.get_user_info(user_id)

    return render_template('user_details.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
