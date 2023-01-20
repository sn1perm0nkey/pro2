# hier sind alle imports aufgelistet
from flask import Flask, redirect
from flask import render_template
from flask import request
import plotly.express as px
import pandas as pd
from plotly.offline import plot
import ast
import random


# hier sind weitere imports aufgelistet, welche aus einer eigener python-datei stammen
from hello_world.datenbank import abspeichern
from hello_world.datenbank import abspeichern_jogging
from hello_world.datenbank import abspeichern_edit
from hello_world.datenbank import abspeichern_jogging_edit
from hello_world.datenbank import auslesen
from hello_world.datenbank import auslesen_jogging
from hello_world.datenbank import auslesen_del
from hello_world.datenbank import auslesen_jogging_del
from hello_world.datenbank import loeschen
from hello_world.datenbank import loeschen_jogging
from hello_world.datenbank import loeschen_edit
from hello_world.datenbank import loeschen_jogging_edit


app = Flask("Hello World")



# hier sind parameter, welche auf allen seiten vorkommen
# man könnte noch weiter namen hinzufügen, dann wären sie randomized
# wenn man es noch ein wenig abändert, dann könnte man mehrere nutzer erstellen, welche sich anmelden können
# dies würde aber viel zeit in anspruch nehmen zum umcoden.
auswahl = ["Robin"]
auswahl_username = ["grafrob"]
ausgewaehlter_username = random.choice(auswahl_username)
ausgewaehlter_name = random.choice(auswahl)

# dies ist die startseite, sie leitet weiter auf die index seite weiter unten
@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "GET":
        return render_template('index.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Home")

# dies ist die index seite
# auf dieser seite kann man die kategorie auswählen, um neue einträge dazu zu erstellen
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Home")


# auf dieser seite kann man für die kategorie "jogging" neue einträge erstellen
@app.route("/jogging", methods=["GET", "POST"])
def jogging():
    if request.method == "GET":
        return render_template('jogging.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Jogging")

    if request.method == "POST":
        # hier sind die einzelnen eingabefelder definiert, welche der nutzer ausfüllt
        datum = request.form['datum']
        strecke = request.form['strecke']
        zeit = request.form['zeit']
        # hier wird die funktion aus "datenbank.py" abgerufen
        abspeichern_jogging(datum, strecke, zeit)

        return render_template('jogging.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Jogging")


# auf dieser seite kann man für die kategorie "body values" neue einträge erstellen
@app.route('/bodyvalues', methods=["GET", "POST"])
def bodyvalues():
    if request.method == "GET":
        return render_template('bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Bodyvalues")

    if request.method == "POST":
        # hier sind die einzelnen eingabefelder definiert, welche der nutzer ausfüllt
        datum = request.form['datum']
        gewicht = request.form['gewicht']
        bodyfat = request.form['bodyfat']
        tbw = request.form['tbw']
        muskeln = request.form['muskeln']
        bmi = request.form['bmi']
        # hier wird die funktion aus "datenbank.py" abgerufen
        abspeichern(datum, gewicht, bodyfat, tbw, muskeln, bmi)

        return render_template('bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Bodyvalues")


# auf dieser seite kann man die kategorie auswählen, um die dazugehörigen statistiken anzuschauen
@app.route("/statistik", methods=["GET", "POST"])
def statistik():
    if request.method == "GET":
        return render_template('statistik.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik")



# auf dieser seite kann man die statistiken zu der kategorie "jogging" anschauen
@app.route("/statistik_jogging")
def statistik_jogging():
    if request.method == "GET":
        # hier wird das dict aus "database_jogging.csv" ausgelesen
        inhalt_string = auslesen_jogging()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        # hier wird eine neue temporäre liste erstellt
        # beim for-loop wird das dict in die neue liste eingespeist, um später die statistiken mit dieser liste zu erstellen
        neue_liste = []
        for eintrag in inhalt.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[1][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Strecke=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Strecke", title="An welchem Datum welche Strecke in km gejogged:")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div1 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[2][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Zeit=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Zeit", title="An welchem Datum wie viele Minuten gejogged:")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div2 = plot(fig, output_type="div")

    # die vorher gegebenen namen werden hier nochmals definiert, um im html code die statistiken darzustellen
    return render_template("statistik_jogging.html", barchart_datum_strecke=div1, barchart_datum_zeit=div2, name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik Jogging")


# auf dieser seite kann man die statistiken zu der kategorie "body values" anschauen
@app.route("/statistik_bodyvalues")
def grafik():
    if request.method == "GET":
        # hier wird das dict aus "database.csv" ausgelesen
        inhalt_string = auslesen()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        # hier wird eine neue temporäre liste erstellt
        # beim for-loop wird das dict in die neue liste eingespeist, um später die statistiken mit dieser liste zu erstellen
        neue_liste = []
        for eintrag in inhalt.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[1][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Gewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Gewicht", title="Gewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div1 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[2][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Bodyfat=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Bodyfat", title="Bodyfat in %")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div2 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[3][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Körperwasser=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Körperwasser", title="Körperwasser in %")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div3 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[4][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Muskeln=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Muskeln", title="Muskeln in %")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div4 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[5][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        BMI=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="BMI", title="BMI")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div5 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[7][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Fettgewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Fettgewicht", title="Fettgewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div6 = plot(fig, output_type="div")

    ######################################################################################

    # hier werden zwei weitere neue temporäre listen erstellt, eine für die daten der x-achse, eine für die daten der y-achse
    # im for-loop werden dann die gewünschten daten für die x- und y-achse in die jeweilige liste eingespiesen
    liste_x = []
    liste_y = []
    for eintrag in neue_liste:
        liste_x_add = eintrag[0][1]
        liste_x.append(liste_x_add)
        liste_y_add = eintrag[8][1]
        liste_y.append(liste_y_add)

    # mithilfe von plotly wird dann ein liniendiagramm erstellt
    # falls die benennung geändert werden sollte ist es wichtig, diese in allen zeilen zu ändern, nicht nur in einer der zeilen
    df = pd.DataFrame(dict(
        # durch das "*" werden von der liste "[" und "]" nicht mitgenommen, sodass nur noch die daten eingespeist werden
        Datum=[*liste_x],
        Muskelgewicht=[*liste_y],
    ))
    df = df.sort_values(by="Datum")
    fig = px.line(df, x="Datum", y="Muskelgewicht", title="Muskelgewicht in kg")

    fig.update_layout(autotypenumbers='convert types')

    # hier wird der statistik einen namen gegeben, um sie dann darzustellen
    # dieser name kommt unten beim return nochmals vor
    div7 = plot(fig, output_type="div")

    # die vorher gegebenen namen werden hier nochmals definiert, um im html code die statistiken darzustellen
    return render_template("statistik_bodyvalues.html", barchart_gewicht=div1, barchart_bodyfat=div2, barchart_tbw=div3, barchart_muskeln=div4, barchart_bmi=div5, barchart_fettgewicht=div6, barchart_muskelgewicht=div7, name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Statistik Bodyvalues")



# auf dieser seite kann man die kategorie auswählen, um die dazugehörige liste anzuschauen
@app.route("/listen", methods=["GET", "POST"])
def listen():
    if request.method == "GET":
        return render_template('listen.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Listen")


# auf dieser seite kann man die liste zu der kategorie "jogging" anschauen
@app.route("/liste_jogging", methods=["GET", "POST"])
def liste_jogging():
    if request.method == "GET":
        # hier wird das dict aus "database_jogging.csv" ausgelesen
        inhalt_string = auslesen_jogging()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        # hier wird eine neue temporäre liste erstellt
        # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
        neue_liste = []
        for eintrag in inhalt.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

        # die zuvor erstellte temporäre liste wird beim return nochmals definiert, um damit im html code eine tabelle mit den daten der liste zu erstellen
        return render_template('liste_jogging.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Jogging", liste=neue_liste)

    if request.method == "POST":
        # hier wird das dict aus "database_jogging.csv" ausgelesen
        inhalt_string_len = auslesen_jogging()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt_len = ast.literal_eval(str(inhalt_string_len))
        # hier wird geprüft, ob die liste 2 oder mehr einträge hat
        # ist dies nicht der fall, so hat die liste nurnoch 1 eintrag
        # dies ist weiter unten nochmals wichtig, denn mit dieser information wird bestimmt, ob ein eintrag gelöscht werden kann oder nicht
        # dadurch wird sichergestellt, dass die liste immer mindestens einen eintrag beinhaltet
        if len(inhalt_len) >= 2:
            # hier wird überprüft, ob "löschen" gedrückt wurde und dabei ein eintrag überhaupt ausgewählt wurde
            if 'löschen' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu löschen
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu löschen
                loeschen_jogging(nummer_del)

                # hier wird das dict aus "database_jogging.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen_jogging()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

            # hier wird überprüft, ob "bearbeiten" gedrückt wurde und dabei ein eintrag überhaupt ausgewählt wurde
            elif 'bearbeiten' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu bearbeiten
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu bearbeiten
                loeschen_jogging_edit(nummer_del)


                # hier wird das dict aus "database_jogging_edit.csv" ausgelesen, dies sind die daten des ausgewählten eintrages
                dict_del_string = auslesen_jogging_del()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                dict_del = ast.literal_eval(str(dict_del_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später beim bearbeiten-screen die zu bearbeitenden werte vorzugeben
                neue_liste = []
                for eintrag in dict_del.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

                # nachdem "bearbeiten" gedrückt wurde, wird man zum screen von "jogging_edit.html" weitergeleitet
                # dieser screen zeigt dann die werte die man bearbeiten will
                return redirect("http://127.0.0.1:5000/jogging_edit", code=302)

            # falls "löschen" oder "bearbeiten" gedrückt wurde aber kein eintrag ausgewählt wurde, wird "else" ausgeführt
            else:
                # hier wird das dict aus "database_jogging.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen_jogging()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

        # falls nur noch 1 eintrag in der liste vorhanden ist, kann man ihn mit diesem "elif" noch bearbeiten, jedoch nicht löschen
        # dadurch wird sichergestellt, dass die liste immer mindestens einen eintrag beinhaltet
        elif len(inhalt_len) == 1:
            if 'löschen' in request.form and "nummer_del" in request.form:
                # hier wird das dict aus "database_jogging.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen_jogging()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

            elif 'bearbeiten' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu bearbeiten
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu bearbeiten
                loeschen_jogging_edit(nummer_del)


                # hier wird das dict aus "database_jogging_edit.csv" ausgelesen, dies sind die daten des ausgewählten eintrages
                dict_del_string = auslesen_jogging_del()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                dict_del = ast.literal_eval(str(dict_del_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später beim bearbeiten-screen die zu bearbeitenden werte vorzugeben
                neue_liste = []
                for eintrag in dict_del.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

                # nachdem "bearbeiten" gedrückt wurde, wird man zum screen von "jogging_edit.html" weitergeleitet
                # dieser screen zeigt dann die werte die man bearbeiten will
                return redirect("http://127.0.0.1:5000/jogging_edit", code=302)

            # falls "löschen" oder "bearbeiten" gedrückt wurde aber kein eintrag ausgewählt wurde, wird "else" ausgeführt
            else:
                # hier wird das dict aus "database_jogging.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen_jogging()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

        # die zuvor erstellte temporäre liste wird beim return nochmals definiert, um damit im html code eine tabelle mit den daten der liste zu erstellen
        return render_template('liste_jogging.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Jogging", liste=neue_liste)


@app.route("/liste_bodyvalues", methods=["GET", "POST"])
def liste_bodyvalues():
    if request.method == "GET":
        # hier wird das dict aus "database.csv" ausgelesen
        inhalt_string = auslesen()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        # hier wird eine neue temporäre liste erstellt
        # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
        neue_liste = []
        for eintrag in inhalt.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

        # die zuvor erstellte temporäre liste wird beim return nochmals definiert, um damit im html code eine tabelle mit den daten der liste zu erstellen
        return render_template('liste_bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Bodyvalues", liste=neue_liste)

    if request.method == "POST":
        # hier wird das dict aus "database.csv" ausgelesen
        inhalt_string_len = auslesen()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt_len = ast.literal_eval(str(inhalt_string_len))
        # hier wird geprüft, ob die liste 2 oder mehr einträge hat
        # ist dies nicht der fall, so hat die liste nurnoch 1 eintrag
        # dies ist weiter unten nochmals wichtig, denn mit dieser information wird bestimmt, ob ein eintrag gelöscht werden kann oder nicht
        # dadurch wird sichergestellt, dass die liste immer mindestens einen eintrag beinhaltet
        if len(inhalt_len) >= 2:
            # hier wird überprüft, ob "löschen" gedrückt wurde und dabei ein eintrag überhaupt ausgewählt wurde
            if 'löschen' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu löschen
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu löschen
                loeschen(nummer_del)

                # hier wird das dict aus "database.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

            # hier wird überprüft, ob "bearbeiten" gedrückt wurde und dabei ein eintrag überhaupt ausgewählt wurde
            elif 'bearbeiten' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu bearbeiten
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu bearbeiten
                loeschen_edit(nummer_del)

                # hier wird das dict aus "database_edit.csv" ausgelesen, dies sind die daten des ausgewählten eintrages
                dict_del_string = auslesen_del()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                dict_del = ast.literal_eval(str(dict_del_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später beim bearbeiten-screen die zu bearbeitenden werte vorzugeben
                neue_liste = []
                for eintrag in dict_del.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

                # nachdem "bearbeiten" gedrückt wurde, wird man zum screen von "bodyvalues_edit.html" weitergeleitet
                # dieser screen zeigt dann die werte die man bearbeiten will
                return redirect("http://127.0.0.1:5000/bodyvalues_edit", code=302)

            # falls "löschen" oder "bearbeiten" gedrückt wurde aber kein eintrag ausgewählt wurde, wird "else" ausgeführt
            else:
                # hier wird das dict aus "database.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)


        # falls nur noch 1 eintrag in der liste vorhanden ist, kann man ihn mit diesem "elif" noch bearbeiten, jedoch nicht löschen
        # dadurch wird sichergestellt, dass die liste immer mindestens einen eintrag beinhaltet
        elif len(inhalt_len) == 1:
            if 'löschen' in request.form and "nummer_del" in request.form:
                # hier wird das dict aus "database.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

            elif 'bearbeiten' in request.form and "nummer_del" in request.form:
                # "nummer_del" ist die nummer des eintrags, welcher ausgewählt wurde um zu bearbeiten
                # aus genau solchen identifizierungsgründen wird in "datenbank.py" jedem eintrag eine nummer gegeben, wenn dieser erstellt wird
                nummer_del = request.form['nummer_del']
                # hier wird eine funktion aus "datenbank.py" ausgeführt, um den ausgewählten eintrag zu bearbeiten
                loeschen_edit(nummer_del)

                # hier wird das dict aus "database_edit.csv" ausgelesen, dies sind die daten des ausgewählten eintrages
                dict_del_string = auslesen_del()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                dict_del = ast.literal_eval(str(dict_del_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später beim bearbeiten-screen die zu bearbeitenden werte vorzugeben
                neue_liste = []
                for eintrag in dict_del.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

                # nachdem "bearbeiten" gedrückt wurde, wird man zum screen von "bodyvalues_edit.html" weitergeleitet
                # dieser screen zeigt dann die werte die man bearbeiten will
                return redirect("http://127.0.0.1:5000/bodyvalues_edit", code=302)

            # falls "löschen" oder "bearbeiten" gedrückt wurde aber kein eintrag ausgewählt wurde, wird "else" ausgeführt
            else:
                # hier wird das dict aus "database.csv" nochmals ausgelesen, um die liste zu aktualisieren
                inhalt_string = auslesen()
                # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
                inhalt = ast.literal_eval(str(inhalt_string))
                # hier wird eine neue temporäre liste erstellt
                # beim for-loop wird das dict in die neue liste eingespeist, um später die übersichtsliste mit dieser liste zu erstellen
                neue_liste = []
                for eintrag in inhalt.values():
                    test = {}
                    test.update(eintrag)
                    neue_liste2 = []
                    for bezeichnung, wert in test.items():
                        neue_liste2.append([bezeichnung, wert])
                    neue_liste.append(neue_liste2)

        # die zuvor erstellte temporäre liste wird beim return nochmals definiert, um damit im html code eine tabelle mit den daten der liste zu erstellen
        return render_template('liste_bodyvalues.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Liste Bodyvalues", liste=neue_liste)





@app.route('/bodyvalues_edit', methods=["GET", "POST"])
def bodyvalues_edit():
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

        return redirect("http://127.0.0.1:5000/liste_bodyvalues", code=302)



@app.route('/jogging_edit', methods=["GET", "POST"])
def jogging_edit():
    if request.method == "GET":
        dict_del_string = auslesen_jogging_del()
        dict_del = ast.literal_eval(str(dict_del_string))
        neue_liste = []
        for eintrag in dict_del.values():
            test = {}
            test.update(eintrag)
            neue_liste2 = []
            for bezeichnung, wert in test.items():
                neue_liste2.append([bezeichnung, wert])
            neue_liste.append(neue_liste2)

        return render_template('jogging_edit.html', name=ausgewaehlter_name, username=ausgewaehlter_username, seitentitel="Edit Jogging Stats", liste=neue_liste)


    if request.method == "POST":
        dict_del_string = auslesen_jogging_del()
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
            nummer_def = eintrag[4][1]


        datum = request.form['datum']
        strecke = request.form['strecke']
        zeit = request.form['zeit']
        nummer = nummer_def
        abspeichern_jogging_edit(datum, strecke, zeit, nummer)

        return redirect("http://127.0.0.1:5000/liste_jogging", code=302)

















if __name__ == "__main__":
    app.run(debug=True, port=5000)
