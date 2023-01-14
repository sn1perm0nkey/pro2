from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
import pandas as pd
from plotly.offline import plot
import ast
import random



from hello_world.datenbank import abspeichern
from hello_world.datenbank import auslesen
from hello_world.datenbank import loeschen

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

    if request.method == "POST":
        if 'nummer_del' in request.form:
            print("yes")
            nummer_del = request.form['nummer_del']
            loeschen(nummer_del)

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

        else:
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

        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Bodyvalues")


@app.route("/viz")
def grafik():
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

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[1][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        x=[*liste_x],
        y=[*liste_y],
    ))
    df = df.sort_values(by="x")
    fig = px.line(df, x="x", y="y", title="Sorted Input")

    fig.update_layout(autotypenumbers='convert types')

    div = plot(fig, output_type="div")

    auswahl = ["Robin"]
    auswahl_username = ["grafrob"]
    ausgewaehlter_username = random.choice(auswahl_username)
    ausgewaehlter_name = random.choice(auswahl)


    return render_template("viz.html", barchart=div, name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Chart")






if __name__ == "__main__":
    app.run(debug=True, port=5000)
