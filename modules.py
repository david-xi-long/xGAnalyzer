from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from . import database
from flask_login import LoginManager, login_manager
import mysql.connector as connector
import decimal
import subprocess as sub
import nltk
from . import database
import sys
from statsbombpy import sb


app = Flask(__name__, template_folder='../html')

db_connection = None
db_cursor = None

try:
    db_connection = connector.connect(user=database.user,
                                      password=database.password,
                                      host=database.host,
                                      database=database.name)
except connector.Error as err:
    print("ERROR")

db_cursor = db_connection.cursor(buffered=True)

get_user_sql = "SELECT username, userid FROM users WHERE username = %s AND password = %s"
get_league_sql = "SELECT name, tournament_id FROM tournaments"
get_team_sql = "SELECT team_name, team_id FROM teams WHERE tournament_id = %s"
get_result_sql = "SELECT home_goals,away_goals FROM new_stats WHERE (home_team_id = %s AND away_team_id = %s) OR " \
                 " (away_team_id = %s AND home_team_id  = %s)"
get_record_sql = "SELECT hometeam_id, awayteam_id, xG_graph FROM new_games WHERE hometeam_id = %s OR awayteam_id = %s"
get_game2_sql = "SELECT * FROM games WHERE hometeam_id = %s AND awayteam_id = %s"


def get_user(a, b):
    db_cursor.execute(get_user_sql, (a, b))
    result = []
    for res in db_cursor.fetchall():
        if res is None:
            return None
        result.append([res[1], res[0]])
    return result


def get_league():
    db_cursor.execute(get_league_sql)
    result = []
    for res in db_cursor.fetchall():
        if res is None:
            return None
        result.append({"leagueid": res[1], "name": res[0]})
    return result


def get_team(a):
    db_cursor.execute(get_team_sql, (a,))
    result = []
    for res in db_cursor.fetchall():
        if res is None:
            return None
        result.append({"teamid": res[1], "name": res[0]})
    return result


def get_record(a):
    db_cursor.execute(get_record_sql, (a, a))
    result = []
    for res in db_cursor.fetchall():
        if res is None:
            return None
        result.append([res[0], res[1], res[2]])
    return result


def get_result(a, b):
    db_cursor.execute(get_result_sql, (a, b, a, b))
    result = []
    for res in db_cursor.fetchall():
        if res is None:
            return None
        result.append([res[0], res[1]])
    return result