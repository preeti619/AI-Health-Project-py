import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        port=3306,
        user="sql12791305",
        password="Dk1qdJ3iM5",
        database="sql12791305"
    )

def add_user(username, full_name, phone, email, password, address):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        raise Exception("Username or email already exists.")

    cursor.execute(
        "INSERT INTO users (username, full_name, phone, email, password, address) VALUES (%s, %s, %s, %s, %s, %s)",
        (username, full_name, phone, email, password, address)
    )
    conn.commit()
    cursor.close()
    conn.close()

def validate_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return False

def store_chat(username, user_input, bot_reply):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat_history (username, user_input, bot_reply) VALUES (%s, %s, %s)",
            (username, user_input, bot_reply)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error storing chat: {e}")
