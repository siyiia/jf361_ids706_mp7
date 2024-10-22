import argparse
from mytool import db


def main():
    parser = argparse.ArgumentParser(
        description="A command-line tool that interacts with an SQLite database."
    )
    parser.add_argument("--db", required=True, help="Path to the SQLite database")
    parser.add_argument(
        "--create", action="store_true", help="Create a table in the database"
    )
    parser.add_argument(
        "--insert",
        nargs=2,
        metavar=("NAME", "MAJOR"),
        help="Insert data into the table",
    )
    parser.add_argument(
        "--query", action="store_true", help="Query data from the table"
    )

    args = parser.parse_args()

    conn = db.connect_db(args.db)

    if args.create:
        db.create_table(conn)
    elif args.insert:
        name, major = args.insert
        db.insert_data(conn, name, major)
    elif args.query:
        db.query_data(conn)

    db.close_db(conn)


if __name__ == "__main__":
    main()
