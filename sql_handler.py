import sqlite3
from sqlite3 import Error
import os 

"""
Things to remember:
    How to deal with restricted players when updating database
    If the match wasn't recent. Don't add pp/rank
"""

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    

def start_sql():
    "Creates sql"
    
    conn = create_connection(r"pythonsqlite.db")
    sql_user_table = """CREATE TABLE IF NOT EXISTS users (
                            username text NOT NULL,
                            osu_id text NOT NULL,
                            country text NOT NULL,
                            pp integer NOT NULL,
                            rank_world integer NOT NULL,
                            rank_country integer NOT NULL,
                            date_updated text NOT NULL
                        )"""

    sql_opponent_table = """CREATE TABLE IF NOT EXISTS opponents (
                            username text NOT NULL,
                            osu_id text NOT NULL,
                            country text NOT NULL,
                            badges integer NOT NULL,
                            pp integer,
                            rank_world integer,
                            rank_country integer,
                            date text,
                            team_name text,
                            tourney_name text NOT NULL,
                            my_score integer NOT NULL,
                            their_score integer NOT NULL,
                            win text NOT NULL,
                            mode integer NOT NULL
                        )"""

    if conn is not None:
        create_table(conn,sql_user_table)
        create_table(conn,sql_opponent_table)

    return conn

def add_data(conn,info,values):
    conn.cursor().execute(info,values)
    conn.commit()

def show_data(c, command):
    c.execute(command)
    print(c.fetchone())

def close_connection(conn):
    conn.close()
    print("Database closed")

"""
conn.fetchone() -> Will fetch the next row in table, else returns NONE
conn.fetchmany(num) -> Will fetch the amount of rows in list else returns []
conn.fetchall() -> Will fetch REMAINING rows
"""
        
        
