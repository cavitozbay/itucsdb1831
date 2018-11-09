import psycopg2 as dbapi2
from user import User
from game import Game

dsn = """user=khxcpxyuayifiy password=a71d836a4a3e8c9d4030a8bd40ffec8d7e43202bf75ece49c4635701c10cd21f
host=ec2-54-247-124-154.eu-west-1.compute.amazonaws.com port=5432 dbname=dd7j2nqkjb2bs9"""

def communicate_with_db(statement):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()
    return cursor

def insert_user(user4insert):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = """INSERT INTO USERS (NAME, PASSWORD) VALUES (%s, %s)"""
    data = (user4insert.get_user_name(), user4insert.get_pw(),)
    cursor.execute(statement, data)
    connection.commit()
    cursor.close()
    connection.close()


def query_user_name(user_name):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement ="""SELECT * FROM USERS WHERE NAME=%s"""
    user_name = (user_name, )
    cursor.execute(statement, user_name)
    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        return None
    print(cursor)
    user_id, name, password = cursor.fetchone()
    user = User(name, password, user_id)
    cursor.close()
    connection.close()
    return user

def get_user(user_id):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = """SELECT * FROM USERS WHERE USER_ID=%s"""
    data = (user_id, )
    cursor.execute(statement, data)
    if cursor != None:
        user_id, name, password = cursor.fetchone()
        userch = User(name, password, user_id)
    else:
        userch = None
    cursor.close()
    connection.close()
    return userch

# -------------------------------------------------------
    
def add_game(game):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = "INSERT INTO GAMES (TITLE, GENRE, AGE_RESTRICTION, PRICE) VALUES (%s, %s, %d, %f)"
    data = (game.title, game.genre, game.age_restriciton, game.price)
    cursor.execute(statement, data)
    connection.commit()
    cursor.close()
    connection.close()

def get_game(game_id):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = "SELECT * FROM GAMES WHERE GAME_ID=%s"
    cursor.execute(statement, [game_id])
    if cursor != None:
        game_id, title, genre, rating, age_restriction, price = cursor.fetchone()
        game = Game(title, genre, rating, age_restriction, price)
    else:
        game = None
    cursor.close()
    connection.close()
    return game

def get_games():
    games = []
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = "SELECT * FROM GAMES"
    cursor.execute(statement)
    for row in cursor:
        title = row[1]
        genre = row[2]
        rating = row[3]
        age_restriction = row[4]
        price = row[5]
        game_ = Game(title, genre, rating, age_restriction, price)
        games.append(game_)
    return games
