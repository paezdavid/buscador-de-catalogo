from flask import Flask, render_template, request
import sqlite3, json

app = Flask(__name__)

@app.route("/")
def index():
    # conn = sqlite3.connect("catalogo_07_08_2023.db")
    # cursor = conn.cursor()
    # # cursor.execute(f"SELECT titulo FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")

    # cursor.execute(f"SELECT titulo, url FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")
    


    return render_template("index.html")


@app.route("/registro/<id>")
def datos_de_un_registro(id):
    conn = sqlite3.connect("catalogo_07_08_2023.db")
    cursor = conn.cursor()
    # cursor.execute(f"SELECT titulo FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")
 
    cursor.execute(f"SELECT * FROM catalogo_03_08_2023 WHERE id = {id}") # Se trae un registro unico

    registro_list_of_tup = cursor.fetchall() # Se almacena todo es una variable, pero fetchall() devuelve una lista de tuplas

    registro_list = list(registro_list_of_tup[0]) # Convertimos en una lista la tupla que nos trajo fetchall()

    print(registro_list)

    return render_template("registro.html", registro_data=registro_list)
    


@app.route("/api/suggestions")
def suggest():
    user_query = request.args.get("query")
    lowercase_input = user_query.lower()

    if len(user_query) == 0:
        print(user_query)
        return json.dumps({"Error": "Query with empty string"})

    conn = sqlite3.connect("catalogo_07_08_2023.db")
    cursor = conn.cursor()
    # cursor.execute(f"SELECT titulo FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")

    cursor.execute(f"SELECT id, titulo FROM catalogo_03_08_2023 WHERE titulo LIKE '{lowercase_input}%' LIMIT 10")
    
    results = cursor.fetchall()
    # suggestions = [row[0] for row in results]
    suggestions = []
    

    for row in results:
        suggestions.append({
            "id": row[0],
            "suggestion_title": row[1]
        })
    
    conn.commit() # Se committean los cambios a la DB
    conn.close()

    print(suggestions)

    return suggestions