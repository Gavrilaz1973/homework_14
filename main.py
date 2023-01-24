from flask import Flask, jsonify
from utils import get_user_title, get_user_years, get_user_rating, get_user_genre


app = Flask(__name__)


@app.route('/movie/<title>')
def get_by_title(title):
    query = f"""
    SELECT title, country, release_year, listed_in, description
    FROM netflix 
    WHERE title = '{title}'"""
    return jsonify(get_user_title(query))


@app.route('/movie/<year_1>/to/<year_2>')
def get_by_years(year_1, year_2):
    query = f"""
        SELECT title, release_year
        FROM netflix 
        WHERE release_year BETWEEN '{year_1}' AND '{year_2}'
        LIMIT 100"""
    return get_user_years(query)


@app.route('/rating/<user_rating>')
def get_by_rating(user_rating):
    param_rating = str()
    if user_rating == 'children':
        param_rating = '= "G"'
    elif user_rating == 'family':
        param_rating = 'LIKE "%G%"'
    elif user_rating == 'adult':
        param_rating = 'LIKE "%%"'
    query = f"""
        SELECT title, rating, description
        FROM netflix 
        WHERE rating {param_rating}
        LIMIT 10"""
    return get_user_rating(query)


@app.route('/genre/<genre>')
def get_by_genre(genre):
    return jsonify(get_user_genre(genre))


if __name__ == '__main__':
    app.run()

