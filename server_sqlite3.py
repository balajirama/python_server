from flask import Flask, render_template, request, redirect
from sqlite3connection import connectToSQLite3
app = Flask(__name__)

dbname = '/home/balaji/my_db.db'

@app.route("/")
def index():
    conn = connectToSQLite3(dbname)
    all_animals = conn.query_db('SELECT * FROM animals ORDER BY common_name')
    all_pets = conn.query_db('SELECT pets.id, name, common_name FROM pets JOIN animals ON pets.animal_id = animals.id ;')
    return render_template("index2.html", all_animals=all_animals, all_pets=all_pets)

@app.route("/add_pet", methods=["POST"])
def add_pet():
    print(request.form)
    conn = connectToSQLite3(dbname)
    data = {
        'name': request.form['pet_name'],
        'id': int(request.form['pet_type'])
    }
    query = "INSERT INTO pets ( name, animal_id ) VALUES ( :name, :id )"
    conn.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)