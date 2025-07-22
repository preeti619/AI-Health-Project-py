# utils/db_helper.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # change if needed
        password="@*@@)^282206pR",         # update if your root has a password
        database="streamlitprojects"
    )

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            full_name VARCHAR(255),
            phone VARCHAR(20),
            email VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            address TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_user(username, full_name, phone, email, password, address):
    create_users_table()  # Ensure table exists
    conn = get_connection()
    cursor = conn.cursor()

    # Check for existing user/email
    cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        raise Exception("Username or email already exists.")

    # Insert new user
    query = "INSERT INTO users (username, full_name, phone, email, password, address) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (username, full_name, phone, email, password, address))
    conn.commit()

    cursor.close()
    conn.close()

def validate_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"Login error: {e}")
        return False

def store_chat(username, user_input, bot_reply):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                user_input TEXT,
                bot_reply TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

        query = "INSERT INTO chat_history (username, user_input, bot_reply) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, user_input, bot_reply))
        conn.commit()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error storing chat: {e}")
