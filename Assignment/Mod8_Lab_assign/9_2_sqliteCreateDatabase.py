import sqlite3

DB_NAME = "sample.db"


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' ready with table 'products'.")


if __name__ == "__main__":
    main()
