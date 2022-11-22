from flask import Flask
from flask import render_template
from flask import request


import random

from hello_world.datenbank import abspeichern
from hello_world.datenbank import auslesen

app = Flask("Hello World")

@app.route("/")
def start():
    todos = auslesen()
    # todos_html = todos.replace("\n", "<br>")
    todo_liste = todos.split("\n")
    neue_liste = []
    for eintrag in todo_liste:
        vorname, nachname = eintrag.split(",")
        neue_liste.append([vorname, nachname])
    return render_template("index.html", liste=neue_liste)


@app.route("/home2", methods=["GET", "POST"])
def homescreen():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('home2.html', name=ausgewaehlter_name, username=ausgewaehlter_username)

@app.route("/home", methods=["GET", "POST"])
def homescreen1():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('home.html', name=ausgewaehlter_name, username=ausgewaehlter_username)

@app.route('/bodyvalues', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username)

    if request.method == "POST":
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        abspeichern(vorname, nachname)
        return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
