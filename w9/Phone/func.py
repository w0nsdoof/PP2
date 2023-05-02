from configparser import ConfigParser
import psycopg2 , csv
from psycopg2.extensions import AsIs

def config(filename = 'database.ini', section = 'postgresql'):
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
    conn = None
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
    CREATE TABLES users_phones (
    user_name VARCHAR(255) PRIMARY KEY NOT NULL,
    user_surname VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
    )
    """

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

def insert(name, surname, phone_number):
    check_sql = """
    SELECT user_name, user_surname FROM users_phones 
    WHERE user_name = %s AND user_surname = %s;
    """

    insert_sql = """
    INSERT INTO users_phones
    (user_name, user_surname, phone_number)
    VALUES
    (%s, %s, %s);
    """

    update_sql = """
    UPDATE users_phones SET phone_number = %s
    WHERE user_name = %s AND user_surname = %s;
    """

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(check_sql, (name, surname))
        is_exist = cur.fetchone()

        if is_exist:
            print("Username already exists, phone number updated")
            cur.execute(update_sql, (phone_number, name, surname))
        else:
            print("Inserted")
            cur.execute(insert_sql, (name, surname, phone_number))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

def delete(name, surname):
        sql = """
        DELETE FROM users_phones
        WHERE user_name = (%s) AND user_surname = (%s);
        """

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(sql, (name, surname))

            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close() 

def import_csv(path):
    sql = """
    INSERT INTO users_phones
    (user_name, user_surname, phone_numbers) 
    VALUES (%s, %s, %s)"
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        with open(path, 'r') as file:
            data = csv.reader(file)
            next(data)
            
            for row in data:
                cur.execute(sql, row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

def import_from_csv(path):
    conn = None
    sql = """
    COPY users_phones(user_name, user_surname, phone_number)
    FROM 'C:\KBTU\PP2\w9\Phone\phone_book.csv' DELIMITER ';'
    CSV HEADER;
    """ # %s into "C:\KBTU\PP2\w9\Phone\phone_book.csv" and format
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql) # 
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not conn:
            conn.close()

def change(surname):
    option = int(input("Select data to change \n 1 -> first name \n 2 -> phone number"))

    sql_name = """
    UPDATE users_phones
    set user_name = %s WHERE user_surname = %s;
    """

    sql_phone = """
    UPDATE users_phones
    set phone_number = %s WHERE user_surname = %s;
    """

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if option == 1:
            name = input("Enter new first name: ")
            cur.execute(sql_name, (name, surname))
        elif option == 2:
            phone_number = input("Enter new phone number: ")
            cur.execute(sql_phone, (phone_number, surname))

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# def sort(option):
#     sql = """
#     SELECT * FROM users_phones
#     ORDER BY %s 
#     """

#     l1 = list(config().keys())

#     for word in l1:
#         if option == word:
#             try:
#                 params = config()
#                 conn = psycopg2.connect(**params)
#                 cur = conn.cursor()
#                 cur.execute(sql, option)
#                 conn.commit()
#                 cur.close()
#             except (Exception, psycopg2.DatabaseError) as error:
#                 print(error)
#             finally:
#                 conn.close()
#         else:
#             print(f"No columns named {option}")

def sort_by_attribute(attribute):
    sql = """
    SELECT * FROM users_phones
    ORDER BY %(attribute)s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, {"attribute": AsIs(attribute)})
        for table in cur.fetchall():
            print(table)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

def show():
    sql = """
    SELECT * FROM users_phones
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print('\t'.join(str(elem) for elem in row))

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print()
        conn.close()
