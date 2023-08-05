from flask import Flask, render_template, request
import sqlite3, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/suggestions")
def suggest():
    user_query = request.args.get("query")
    lowercase_input = user_query.lower()

    if len(user_query) == 0:
        print(user_query)
        return json.dumps({"Error": "Query with empty string"})

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # cursor.execute(f"SELECT titulo FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")

    cursor.execute(f"SELECT titulo, url FROM catalogo WHERE titulo LIKE '\n\t\t{lowercase_input}%' LIMIT 10")
    
    results = cursor.fetchall()
    # suggestions = [row[0] for row in results]
    suggestions = []
    

    for row in results:
        suggestions.append({
            "suggestion_title": row[0],
            "suggestion_url": row[1]
        })
    
    conn.commit() # Se committean los cambios a la DB
    conn.close()

    print(suggestions)

    return suggestions