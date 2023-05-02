import psycopg2
from typing import List, Tuple
from configparser import ConfigParser


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

def insert_users(user_data: List[Tuple[str,str]]) -> List[Tuple[str,str]]:
    """
    Inserts new users into the database using a list of tuples containing
    name and phone number. Checks the correctness of phone numbers and
    returns a list of incorrect data.

    Args:
    - user_data: A list of tuples containing name and phone number.

    Returns:
    - A list of tuples containing incorrect data.
    """
    incorrect_data = []
    sql = """
    INSERT INTO users_phones
    (user_name, phone_number)
    VALUES
    (%s, %s);
    """

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for user in user_data:
            name, phone = user
            if not is_valid_phone(phone):
                incorrect_data.append(user)
            else:
                cur.execute(sql, (name, phone))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    return incorrect_data

def is_valid_phone(phone: str) -> bool:
    """
    Checks the validity of a phone number.

    Args:
    - phone: A string representing a phone number.

    Returns:
    - True if the phone number is valid, False otherwise.
    """
    # Implement your phone number validation logic here.
    # For example, you could use a regular expression to check the format.
    return True