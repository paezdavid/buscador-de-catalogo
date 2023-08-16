from flask import Flask, render_template, request
import sqlite3, json, re

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/registro/<id>")
def datos_de_un_registro(id):
    conn = sqlite3.connect("catalogo_07_08_2023.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM catalogo_03_08_2023 WHERE id = {id}") # Se trae un registro unico

    registro_list_of_tup = cursor.fetchall() # Se almacena todo en una variable, pero fetchall() devuelve una lista con una tupla dentro

    registro_list = list(registro_list_of_tup[0]) # Convertimos en una lista la tupla que nos trajo fetchall()

    # Antes de enviar los datos al cliente, tenemos que parsear la lista de temas que viene envuelta en angle brackets (<INGENIERIA INDUSTRIAL>< CONSTRUCCION >)
    angle_bracket_pattern = r'[<>]'
    parsed_temas_str = re.sub(angle_bracket_pattern, "|", registro_list[6]) # reemplazamos los angle brackets por un |

    # Reemplazamos el valor anterior del index de la lista en el cual se encuentran los temas 
    registro_list[6] = parsed_temas_str.lower()


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

    cursor.execute(f"SELECT id, titulo FROM catalogo_03_08_2023 WHERE titulo LIKE '%{lowercase_input}%' LIMIT 10")
    
    results = cursor.fetchall()
    suggestions = []
    

    for row in results:
        suggestions.append({
            "id": row[0],
            "suggestion_title": row[1]
        })
    
    conn.commit() # Se committean los cambios a la DB
    conn.close()

    return suggestions