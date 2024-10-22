from mytool import db

def test_create_table():
    conn = db.connect_db(":memory:")
    db.create_table(conn)
    db.close_db(conn)

def test_insert_query():
    conn = db.connect_db(":memory:")
    db.create_table(conn)
    db.insert_data(conn, "test_name", "ECE")
    db.query_data(conn)
    db.close_db(conn)