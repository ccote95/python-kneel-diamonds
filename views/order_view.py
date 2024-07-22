import sqlite3
import json

def list_orders():
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute(
            """
            SELECT
                o.id AS order_id,
                o.metal_id,
                m.metal AS metal_name,
                m.price AS metal_price,
                o.size_id,
                s.carets AS size_carets,
                s.pricce AS size_price,
                o.style_id,
                st.style AS style_name,
                st.price AS style_price
            FROM Orders o
            JOIN Metals m ON m.id = o.metal_id
            JOIN Sizes s ON s.id = o.size_id
            JOIN Styles st ON st.id = o.style_id
            """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            order = {
                'order_id': row['order_id'],
                'metal': {
                    'id': row['metal_id'],
                    'name': row['metal_name'],
                    'price': row['metal_price']
                },
                'size': {
                    'id': row['size_id'],
                    'carets': row['size_carets'],
                    'price': row['size_price']
                },
                'style': {
                    'id': row['style_id'],
                    'name': row['style_name'],
                    'price': row['style_price']
                }
            }
            orders.append(order)

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

def new_order(order):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Orders (metal_id, style_id, size_id)
            VALUES (?,?,?)
            """,
            (order['metal_id'], order['style_id'], order['size_id'])
        )
    return True if db_cursor.rowcount > 0 else False

def remove_order(pk):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Orders WHERE id = ?
            """,(pk,)
        )
        number_of_rows_deleted = db_cursor.rowcount
    return True if number_of_rows_deleted > 0 else False