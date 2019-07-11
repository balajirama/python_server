from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('pets_db')
    all_animals = mysql.query_db('SELECT * from animals ;')
    mysql = connectToMySQL('pets_db')
    all_pets = mysql.query_db('SELECT pet_id, name, common_name FROM pets JOIN animals ON pets.animal_id = animals.id ;')
    return render_template("index.html", all_animals=all_animals, all_pets=all_pets)

@app.route("/add_pet", methods=["POST"])
def add_pet():
    print(request.form)
    mysql = connectToMySQL('pets_db')
    data = {
        'name': request.form['pet_name'],
        'id': int(request.form['pet_type'])
    }
    query = "INSERT INTO pets ( name, create_time, update_time, animal_id ) VALUES ( %(name)s, NOW(), NOW(), %(id)s )"
    mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)