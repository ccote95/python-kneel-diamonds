import sqlite3
import json

def update_metal(id, metal_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    metal = ?,
                    price = ?
                WHERE id = ?
            """,
            (metal_data['metal'], metal_data['price'], id)
        )
    return True if db_cursor.rowcount > 0 else False