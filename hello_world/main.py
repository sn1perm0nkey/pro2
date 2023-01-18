from flask import Flask, redirect
from flask import render_template
from flask import request
import plotly.express as px
import pandas as pd
from plotly.offline import plot
import ast
import random



from hello_world.datenbank import abspeichern
from hello_world.datenbank import abspeichern_edit
from hello_world.datenbank import auslesen
from hello_world.datenbank import auslesen_del
from hello_world.datenbank import loeschen
from hello_world.datenbank import loeschen_edit

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
    return render_template("bodyvalues_list.html", liste=neue_liste)


@app.route("/training", methods=["GET", "POST"])
def training():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('training.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Training")

@app.route("/statistik_kategorie", methods=["GET", "POST"])
def statistik_kategorie():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('statistik_kategorie.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik Kategorie")


@app.route("/listen_kategorie", methods=["GET", "POST"])
def listen_kategorie():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('listen_kategorie.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Listen Kategorie")


@app.route("/statistik", methods=["GET", "POST"])
def statistik():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('statistik.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik")


@app.route("/listen", methods=["GET", "POST"])
def listen():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('listen.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Listen")


@app.route("/index", methods=["GET", "POST"])
def homescreen1():
    if request.method == "GET":
        auswahl = ["Robin"]
        auswahl_username = ["grafrob"]
        ausgewaehlter_username = random.choice(auswahl_username)
        ausgewaehlter_name = random.choice(auswahl)
        return render_template('index.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Home")




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


@app.route('/bodyvalues_edit', methods=["GET", "POST"])
def hello_world1():
    if request.method == "GET":
        dict_del_string = auslesen_del()
        dict_del = ast.literal_eval(str(dict_del_string))
        neue_liste = []
        for eintrag in dict_del.values():
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
        return render_template('bodyvalues_edit.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Edit Bodyvalues", liste=neue_liste)


    if request.method == "POST":
        dict_del_string = auslesen_del()
        dict_del = ast.literal_eval(str(dict_del_string))
        neue_liste = []
        for eintrag in dict_del.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

        for eintrag in neue_liste:
            nummer_def = eintrag[6][1]


        datum = request.form['datum']
        gewicht = request.form['gewicht']
        bodyfat = request.form['bodyfat']
        tbw = request.form['tbw']
        muskeln = request.form['muskeln']
        bmi = request.form['bmi']
        nummer = nummer_def
        abspeichern_edit(datum, gewicht, bodyfat, tbw, muskeln, bmi, nummer)

        return redirect("http://127.0.0.1:5000/bodyvalues_list", code=302)



@app.route("/bodyvalues_list", methods=["GET", "POST"])
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
        return render_template('bodyvalues_list.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Bodyvalues", liste=neue_liste)

    if request.method == "POST":
        inhalt_string_len = auslesen()
        inhalt_len = ast.literal_eval(str(inhalt_string_len))
        if len(inhalt_len) >= 2:
            if 'löschen' in request.form and "nummer_del" in request.form:
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

            elif 'bearbeiten' in request.form and "nummer_del" in request.form:
                nummer_del = request.form['nummer_del']
                loeschen_edit(nummer_del)

                dict_del_string = auslesen_del()
                dict_del = ast.literal_eval(str(dict_del_string))
                neue_liste = []
                for eintrag in dict_del.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

                return redirect("http://127.0.0.1:5000/bodyvalues_edit", code=302)


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
        return render_template('bodyvalues_list.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Bodyvalues", liste=neue_liste)





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
        Datum=[*liste_x],
        Gewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Gewicht", title="Gewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    div1 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[2][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        Bodyfat=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Bodyfat", title="Bodyfat in %")

    fig.update_layout(autotypenumbers='convert types')

    div2 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[3][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        Körperwasser=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Körperwasser", title="Körperwasser in %")

    fig.update_layout(autotypenumbers='convert types')

    div3 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[4][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        Muskeln=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Muskeln", title="Muskeln in %")

    fig.update_layout(autotypenumbers='convert types')

    div4 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[5][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        BMI=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="BMI", title="BMI")

    fig.update_layout(autotypenumbers='convert types')

    div5 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[7][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        Fettgewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Fettgewicht", title="Fettgewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    div6 = plot(fig, output_type="div")

    ######################################################################################

    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[8][1]
        liste_y.append(liste_y_add)

    df = pd.DataFrame(dict(
        Datum=[*liste_x],
        Muskelgewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Muskelgewicht", title="Muskelgewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    div7 = plot(fig, output_type="div")



    auswahl = ["Robin"]
    auswahl_username = ["grafrob"]
    ausgewaehlter_username = random.choice(auswahl_username)
    ausgewaehlter_name = random.choice(auswahl)


    return render_template("viz.html", barchart_gewicht=div1, barchart_bodyfat=div2, barchart_tbw=div3, barchart_muskeln=div4, barchart_bmi=div5, barchart_fettgewicht=div6, barchart_muskelgewicht=div7, name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik Bodyvalues")






if __name__ == "__main__":
    app.run(debug=True, port=5000)
