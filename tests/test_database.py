import sqlite3
from vshc.database import detect_id_gap


def test_detect_id_gap():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY)")
    cursor.executemany(
        "INSERT INTO users (id) VALUES (?)", [(0,), (1,), (2,), (4,), (5,)]
    )

    gap = detect_id_gap(cursor, "users")

    assert gap == 3
