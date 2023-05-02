import psycopg2
from configparser import ConfigParser


def config(filename = 'snake_db.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    try:
        params = config()
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def create_tables():
    sql = """
    CREATE TABLE users_score (
    user_name CHARACTER VARYING(30) PRIMARY KEY,
    user_score SERIAL,
    user_level SERIAL
);
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
       conn.close()


def is_username_exist(username):
    sql = """
    SELECT * FROM users_score WHERE user_name = %s
    """
    conn = None
    is_exist = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, ))
        is_exist = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return is_exist


def get_scores_by_name(id):
    sql = """
    SELECT * FROM users_score WHERE user_name = %s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (id, ))
        data = cur.fetchone()
        for line in data:
            print(line)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_scores(user_name, score, level):
    conn = None
    sql = """
    INSERT INTO users_score (user_name, user_score, user_level)
    VALUES (%s, %s, %s);
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, score, level))
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_username(username):
    sql = """
    INSERT INTO users_score (user_name)
    VALUES (%s) ;
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username,))
        data = cur.fetchone()
        for line in data:
            print(line)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def update(username, score, lvl):
    sql = """
    UPDATE users_score 
    SET user_score = %s , user_level = %s
    WHERE user_name = %s;
    """
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (score, lvl, username))

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    