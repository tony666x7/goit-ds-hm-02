import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100),
            email VARCHAR(100) UNIQUE
        )
        """,
        """
        CREATE TABLE status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE
        )
        """,
        """
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            description TEXT,
            status_id INTEGER REFERENCES status(id),
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        # Підключення до бази даних
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost"
        )
        cursor = conn.cursor()
        # Виконання кожної команди CREATE TABLE
        for command in commands:
            cursor.execute(command)
        # Закриття курсора та збереження змін
        cursor.close()
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
