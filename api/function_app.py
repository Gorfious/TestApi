import json
import azure.functions as func

from sqlite_helper import ( 
    initialize_db,
    get_connection
)

app = func.FunctionApp()

initialize_db()


@app.route(route="customers", methods=["GET"])
def get_customers(req: func.HttpRequest) -> func.HttpResponse:

    conn = get_connection()

    rows = conn.execute(
        "SELECT id, name From customers"
    ).fetchall()

    conn.close()

    data = [dict(row) for row in rows]

    return func.HttpResponse(
        json.dumps(data),
        mimetype="application/json",
        status_code=200
    )

@app.route(route="customers", methods=["POSTS"])
def add_customer(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()

    name = body.get("name")

    conn = get_connection()

    cursor = conn.execute(
        "INSERT INTO customers(name) VALUES (?)",
        (name,)
    )

    conn.commit()

    new_id = cursor.lastrowid

    conn.close()

    return func.HttpResponse(
        json.dumps({
            "id": new_id,
            "name": name
        }),
        mimetype="application/json",
        status_code=201
    )