from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot
import ast
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
    return render_template("index2.html", liste=neue_liste)


@app.route("/home2", methods=["GET", "POST"])
def homescreen():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('home2.html', name=ausgewaehlter_name, username=ausgewaehlter_username)

@app.route("/index", methods=["GET", "POST"])
def homescreen1():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('index.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Home")


@app.route("/index2", methods=["GET", "POST"])
def homescreen2():
    if request.method == "GET":
        inhalt_string = auslesen()
        inhalt = ast.literal_eval(str(inhalt_string))
        neue_liste = []
        for eintrag in inhalt.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('index2.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Home2", liste=neue_liste)

@app.route('/bodyvalues', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Bodyvalues")

    if request.method == "POST":
        datum = request.form['datum']
        gewicht = request.form['gewicht']
        bodyfat = request.form['bodyfat']
        tbw = request.form['tbw']
        muskeln = request.form['muskeln']
        bmi = request.form['bmi']
        abspeichern(datum, gewicht, bodyfat, tbw, muskeln, bmi)
        return "ok"


@app.route("/viz")
def grafik():
    fig = px.pie(labels=[1, 2, 3, 4, 5], values=[6, 7, 8, 9, 10])
    div = plot(fig, output_type="div")

    return render_template("viz.html", barchart=div, seitentitel="Chart")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
