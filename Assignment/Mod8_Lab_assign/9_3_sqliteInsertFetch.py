import sqlite3

DB_NAME = "insert_fetch.db"


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """
    )

    cur.execute("DELETE FROM books")
    cur.executemany(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        [
            ("Python Basics", "Jane Doe"),
            ("SQLite Guide", "John Smith"),
        ],
    )
    conn.commit()

    cur.execute("SELECT id, title, author FROM books ORDER BY id")
    rows = cur.fetchall()

    print("Fetched rows:")
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
