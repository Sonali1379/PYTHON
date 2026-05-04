import sqlite3

DB_NAME = "lab.sqlite3"


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """
    )

    cur.execute("DELETE FROM students")  # clear demo rows so re-runs stay tidy
    cur.executemany(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        [("Alice", 20), ("Bob", 21), ("Carol", 19)],
    )
    conn.commit()

    cur.execute("SELECT id, name, age FROM students ORDER BY id")
    rows = cur.fetchall()

    print("Rows in students:")
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
