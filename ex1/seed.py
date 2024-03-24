from faker import Faker
import psycopg2
import random

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost"
)

def seed_users(num_users):
    cursor = conn.cursor()
    try:
        for _ in range(num_users):
            fullname = fake.name()
            email = fake.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        cursor.close()

def seed_statuses():
    cursor = conn.cursor()
    statuses = ['new', 'in progress', 'completed']
    try:
        for status in statuses:
            cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        cursor.close()

def seed_tasks(num_tasks):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cursor.fetchall()]

        for _ in range(num_tasks):
            title = fake.sentence()
            description = fake.text()
            status_id = random.choice(status_ids)
            user_id = random.choice(user_ids)
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                           (title, description, status_id, user_id))
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
    finally:
        cursor.close()

if __name__ == '__main__':
    seed_users(10)
    seed_statuses()
    seed_tasks(20)
    conn.close()
