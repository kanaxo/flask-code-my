import sqlite3
from sqlite3 import Error
from hello import app, db

database = r"users.db"

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY
        name text NOT NULL
        email text NOT NULL
        date_added datetime 
    )
    """
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_table)
    else:
        print("Error! cannot create the database connection.")


def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    # create_connection(database)
    # main()
    create_db()
    print("Created database!")
    
    