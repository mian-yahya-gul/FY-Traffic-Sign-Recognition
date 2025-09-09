import sqlite3   # Import SQLite library for handling the database

# ------------------------------
# Function: init_db
# Purpose: Initialize the database and create the 'users' table (if it doesn't exist).
# ------------------------------
def init_db():
    # Connect to (or create if not exists) a local SQLite database file
    conn = sqlite3.connect("traffic_signs.db")
    cursor = conn.cursor()

    # Create a 'users' table with columns for id, username, and password
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-increment user ID
            username TEXT UNIQUE,                  -- Username must be unique
            password TEXT                          -- Password stored as plain text (for prototype only)
        )
    """)

    # Save (commit) the changes
    conn.commit()
    # Close the connection
    conn.close()


# ------------------------------
# Function: get_user
# Purpose: Retrieve a user from the database based on username and password (for login).
# ------------------------------
def get_user(username, password):
    conn = sqlite3.connect("traffic_signs.db")
    cursor = conn.cursor()

    # Check if a user exists with the given username and password
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()   # Returns one matching row if found, else None

    conn.close()
    return result   # Used in login authentication


# ------------------------------
# Function: add_user
# Purpose: Add a new user (registration) into the database.
# ------------------------------
def add_user(username, password):
    conn = sqlite3.connect("traffic_signs.db")
    cursor = conn.cursor()
    try:
        # Insert new user credentials into the users table
        cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        conn.commit()
        success = True   # Registration successful
    except sqlite3.IntegrityError:
        # Error occurs if the username already exists (due to UNIQUE constraint)
        success = False
    conn.close()
    return success
