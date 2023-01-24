import sqlite3


def get_user_title(query):

    with sqlite3.connect('netflix.db') as conn:
        curs = conn.cursor()

    curs.execute(query)

    for row in curs.fetchall():
        result_dict = {"title": row[0],
                       "country": row[1],
                       "release_year": row[2],
                       "genre": row[3],
                       "description": row[4]}
        return result_dict


def get_user_years(query):
    with sqlite3.connect('netflix.db') as conn:
        curs = conn.cursor()
    result = []
    curs.execute(query)
    for item in curs.fetchall():
        result.append({"title": item[0], "release_year": item[1]})
    return result


def get_user_rating(query):
    with sqlite3.connect('netflix.db') as conn:
        curs = conn.cursor()
    result = []
    curs.execute(query)
    for item in curs.fetchall():
        result.append({"title": item[0], "rating": item[1], "description": item[2]})
    return result


def get_user_genre(user_genre):
    with sqlite3.connect('netflix.db') as conn:
        curs = conn.cursor()
    result = []
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{user_genre}%'
        ORDER BY release_year DESC 
        LIMIT 10"""
    curs.execute(query)
    for item in curs.fetchall():
        result.append({"title": item[0], "description": item[1]})
    return result


def user_query(user_type:str, user_year:str, user_genre:str):
    with sqlite3.connect('netflix.db') as conn:
        curs = conn.cursor()
    result = []
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE netflix.type = '{user_type}' 
        AND release_year = '{user_year}' 
        AND listed_in LIKE '%{user_genre}%' 
        LIMIT 10"""
    curs.execute(query)
    for item in curs.fetchall():
        result.append({"title": item[0], "description": item[1]})
    return result

#print (user_query('Movie', '1997', 'Dramas'))

