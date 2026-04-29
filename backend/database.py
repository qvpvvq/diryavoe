import sqlite3
from flask import g, current_app


def create_db():
    db_path = current_app.config.get("DATABASE_URL", "SQLi.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        content TEXT NOT NULL
        )
    """)

    if cursor.execute("SELECT COUNT(*) FROM posts").fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO posts (username, content) VALUES (?, ?)",
            ("admin", "Добро пожаловать в самую безопасную соцсеть!"),
        )

    users = [
        ("admin", "admin123", "admin"),
        ("user", "user123", "user"),
        ("vasyan", "nasral", "user"),
        ("dodik", "dcp2281337", "user"),
        ("admiral", "degenerat", "user"),
    ]
    for u, p, r in users:
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (u, p, r),
            )
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config["DATABASE_URL"])
        db.row_factory = sqlite3.Row
    return db


def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "database.py":
    create_db
