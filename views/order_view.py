import sqlite3
import json

def list_orders():
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id
            FROM Orders O
            """
        )
        query_results = db_cursor.fetchall()

        orders=[]
        for row in query_results:
            orders.append(dict(row))

        serialized_orders = json.dumps(orders)

    return serialized_orders



def single_order(pk):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id
            FROM Orders o
            WHERE o.id = ?

            """,(pk,))
        query_results = db_cursor.fetchone()

        serialized_order = json.dumps(dict(query_results))
    return serialized_order