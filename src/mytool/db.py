import sqlite3


def connect_db(db_path):
    """Connect to SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def create_table(conn):
    """Create a table if it doesn't exist."""
    try:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS data
                        (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         major TEXT NOT NULL);"""
        )
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_data(conn, name, major):
    """Insert a record into the table."""
    try:
        conn.execute("INSERT INTO data (name, major) VALUES (?, ?)", (name, major))
        conn.commit()
        print(f"Inserted ({name}, {major}) into the database")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")


def query_data(conn):
    """Query all records from the table."""
    try:
        cursor = conn.execute("SELECT id, name, major FROM data")
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"ID = {row[0]}, Name = {row[1]}, Major = {row[2]}")
        else:
            print("No data found")
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")


def close_db(conn):
    """Close the database connection."""
    try:
        conn.close()
        print("Database connection closed")
    except sqlite3.Error as e:
        print(f"Error closing database connection: {e}")
