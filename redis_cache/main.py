import sqlite3
import redis
import json


def create_db():
    database_name = "database.db"
    connection = sqlite3.connect(database_name)
    c = connection.cursor()

    # Create table
    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
                Id INTEGER NOT NULL, 
                name TEXT NOT NULL
        )"""
    )

    c.close()
    # commit the changes to db
    connection.commit()
    # close the connection
    connection.close()

    print(f"database {database_name}created successfully!!!")


def insert_rows(id, name):
    """
    INSERT a ROW in a TABLE
    id: integer
    name: string
    """
    import sqlite3

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    insert_row = """
        INSERT INTO users VALUES (?, ?)
    """

    cursor.execute(insert_row, (id, name))

    cursor.close()
    connection.commit()
    connection.close()

    print(f"row ({id} {name})inserted successfully!!!")


def delete_row(id):
    import sqlite3

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    row_id_to_delete = id

    delete_row_query = """
        DELETE FROM users
        WHERE id = ?
    """

    cursor.execute(delete_row_query, (row_id_to_delete,))
    cursor.close()
    connection.commit()
    connection.close()

    print(f"row {row_id_to_delete} deleted successfully!!!")


def show_database():
    import sqlite3

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    select_all_query = """
        SELECT * FROM users
    """

    cursor.execute(select_all_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


def get_my_friends():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    redis_client = redis.Redis(host="localhost", port=6379, db=0)

    cached_friends = redis_client.get("get_friends")

    if cached_friends is not None:
        print("getting info from cache.")
        return json.loads(cached_friends)

    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()

    redis_client.set(name="get_friends", value=json.dumps(result), ex=60)
    # redis_client.expire(get_friends, timedelta(seconds=20))

    cursor.close()
    connection.close()
    redis_client.close()

    print("getting info from database.")
    return result


if __name__ == "__main__":
    # create_db()
    # show_database()

    # insert_rows(1, "Ram")
    # insert_rows(2, "Geeta")
    # insert_rows(3, "Ramu")
    # insert_rows(4, "Seeta")

    # delete_row(1)
    # delete_row(2)
    print(get_my_friends())
