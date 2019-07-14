from flask import Flask, render_template, request, redirect, session, flash, get_flashed_messages
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
from datetime import datetime
import re
import os
app = Flask(__name__)

app.secret_key = 'darksecret'

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$")
NUM_REGEX = re.compile(r"^.*[0-9]+.*")
CAP_REGEX = re.compile(r"^.*[A-Z]+.*")

dbname = 'dbname'

@app.route("/")
def mainpage():
    print(get_flashed_messages())
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)