from sqlite3 import Cursor
from typing import Optional


def detect_id_gap(
    db_cursor: Cursor,
    table_name: str,
    id_column: str = "id",
) -> int:
    """
    Detect the first missing positive integer ID in a database table.

    The function assumes that the ID column contains non-negative integers
    (typically a PRIMARY KEY) and returns the first gap in ascending order.

    Example:
        IDs in table: [0, 1, 2, 4, 5]
        -> returns 3

        IDs in table: []
        -> returns 0

    Args:
        db_cursor (Cursor):
            An active SQLite database cursor.

        table_name (str):
            Name of the table to inspect.

        id_column (str):
            Name of the ID column. Defaults to "id".

    Returns:
        int:
            The first missing integer ID.
    """

    query = f"""
        SELECT t1."{id_column}" + 1
        FROM "{table_name}" t1
        LEFT JOIN "{table_name}" t2
        ON t1."{id_column}" + 1 = t2."{id_column}"
        WHERE t2."{id_column}" IS NULL
        ORDER BY t1."{id_column}"
        LIMIT 1
    """

    db_cursor.execute(query)
    result: Optional[tuple] = db_cursor.fetchone()

    if result is not None:
        return result[0]

    # Table empty or no gaps -> return next ID
    db_cursor.execute(f'SELECT MAX("{id_column}") FROM "{table_name}"')
    max_id = db_cursor.fetchone()[0]

    return 0 if max_id is None else max_id + 1
