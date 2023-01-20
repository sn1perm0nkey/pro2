# hier sind alle imports aufgelistet
import ast
import json

# bei dieser funktion werden die daten aus "database.csv" ausgelesen
def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string

# bei dieser funktion werden die daten aus "database_jogging.csv" ausgelesen
def auslesen_jogging():
    with open("database_jogging.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string

# bei dieser funktion werden die daten aus "database_edit.csv" ausgelesen
def auslesen_del():
    with open("database_edit.csv", "r") as open_file:
        dict_del_string = open_file.read()
    return dict_del_string

# bei dieser funktion werden die daten aus "database_jogging_edit.csv" ausgelesen
def auslesen_jogging_del():
    with open("database_jogging_edit.csv", "r") as open_file:
        dict_del_string = open_file.read()
    return dict_del_string

# bei dieser funktion wird der ausgewählte eintrag bei den bodyvalues gelöscht
def loeschen(nummer_del):
    with open("database.csv", "r") as open_file:
        # hier wird das dict aus "database.csv" ausgelesen
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue temporäre liste erstellt
    # beim for-loop wird das dict in die neue liste eingespeist, um später den ausgewählten eintrag zu löschen
    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    # hier wird ein neues dict erstellt
    # hier werden alle daten eingespeist, welche behalten werden sollen
    dict_keep = {}
    for number in neue_liste:
        # alle einträge, welche nicht der identifikationsnummer des ausgewählten eintrags entsprechen, werden zum temporären dict hinzugefügt
        if int(nummer_del) != int(number[6][1]):
            dict_temp_keep = {number[6][1]: {"datum": number[0][1],
                                            "gewicht": number[1][1],
                                            "bodyfat": number[2][1],
                                            "tbw": number[3][1],
                                            "muskeln": number[4][1],
                                            "bmi": number[5][1],
                                            "nummer": number[6][1],
                                            "bodyfat_kg": round(float(number[2][1]) * float(number[1][1]) / 100, 1),
                                            "muskeln_kg": round(float(number[4][1]) * float(number[1][1]) / 100, 1), }
                         }
            dict_keep.update(dict_temp_keep)

    # der inhalt des dict wird gelöscht und anschliessen werden die einträge ohne dem ausgewählten beitrag wieder eingespeist
    inhalt.clear()
    inhalt.update(dict_keep)
    # hier wird die datenbank mit dem neuem aktualisierten datensatz überschrieben
    with open("database.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database.csv" abgespeichert werden kann
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)
        open_file.close()

# bei dieser funktion wird der ausgewählte eintrag beim jogging gelöscht
def loeschen_jogging(nummer_del):
    with open("database_jogging.csv", "r") as open_file:
        # hier wird das dict aus "database.csv" ausgelesen
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue temporäre liste erstellt
    # beim for-loop wird das dict in die neue liste eingespeist, um später den ausgewählten eintrag zu löschen
    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    # hier wird ein neues dict erstellt
    # hier werden alle daten eingespeist, welche behalten werden sollen
    dict_keep = {}
    # alle einträge, welche nicht der identifikationsnummer des ausgewählten eintrags entsprechen, werden zum temporären dict hinzugefügt
    for number in neue_liste:
        if int(nummer_del) != int(number[4][1]):
            dict_temp_keep = {number[4][1]: {"datum": number[0][1],
                                            "strecke": number[1][1],
                                            "zeit": number[2][1],
                                            "km_schnitt": round(float(number[2][1]) / float(number[1][1]), 2),
                                            "nummer": number[4][1], }
                         }
            dict_keep.update(dict_temp_keep)

    # der inhalt des dict wird gelöscht und anschliessen werden die einträge ohne dem ausgewählten beitrag wieder eingespeist
    inhalt.clear()
    inhalt.update(dict_keep)

    # hier wird die datenbank mit dem neuem aktualisierten datensatz überschrieben
    with open("database_jogging.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database_jogging.csv" abgespeichert werden kann
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)
        open_file.close()



# bei dieser funktion wird der ausgewählte eintrag der bodyvalues in eine neue datenbank abgespeichert, damit dieser bearbeitet werden kann
def loeschen_edit(nummer_del):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue temporäre liste erstellt
    # beim for-loop wird das dict in die neue liste eingespeist, um später den ausgewählten eintrag zu löschen
    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    # hier wird ein neues dict erstellt
    # hier werden alle daten eingespeist, welche bearbeitet und überschrieben werden sollen
    dict_del = {}
    # alle einträge, welche der identifikationsnummer des ausgewählten eintrags entsprechen, werden zum temporären dict hinzugefügt
    for number in neue_liste:
        if int(nummer_del) == int(number[6][1]):
            dict_temp_del = {number[6][1]: {"datum": number[0][1],
                                        "gewicht": number[1][1],
                                        "bodyfat": number[2][1],
                                        "tbw": number[3][1],
                                        "muskeln": number[4][1],
                                        "bmi": number[5][1],
                                        "nummer": number[6][1],
                                        "bodyfat_kg": round(float(number[2][1]) * float(number[1][1]) / 100, 1),
                                        "muskeln_kg": round(float(number[4][1]) * float(number[1][1]) / 100, 1), }
                         }
            # hier werden die alten daten mit den neuen daten überschrieben
            dict_del.update(dict_temp_del)

    # hier wird in die datenbank der zu bearbeitende eintrag abgespeichert
    # in dieser separaten datenbank befindet sich jeweils nur der zu bearbeitende eintrag
    with open("database_edit.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database_edit.csv" abgespeichert werden kann
        dict_del_updated = json.dumps(dict_del)
        write_file.write(dict_del_updated)
        open_file.close()


# bei dieser funktion wird der ausgewählte eintrag deim jogging in eine neue datenbank abgespeichert, damit dieser bearbeitet werden kann
def loeschen_jogging_edit(nummer_del):
    with open("database_jogging.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue temporäre liste erstellt
    # beim for-loop wird das dict in die neue liste eingespeist, um später den ausgewählten eintrag zu löschen
    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    # hier wird ein neues dict erstellt
    # hier werden alle daten eingespeist, welche bearbeitet und überschrieben werden sollen
    dict_del = {}
    # alle einträge, welche der identifikationsnummer des ausgewählten eintrags entsprechen, werden zum temporären dict hinzugefügt
    for number in neue_liste:
        if int(nummer_del) == int(number[4][1]):
            dict_temp_del = {number[4][1]: {"datum": number[0][1],
                                        "strecke": number[1][1],
                                        "zeit": number[2][1],
                                        "km_schnitt": round(float(number[2][1]) / float(number[1][1]), 2),
                                        "nummer": number[4][1], }
                         }
            # hier werden die alten daten mit den neuen daten überschrieben
            dict_del.update(dict_temp_del)

    # hier wird in die datenbank des zu bearbeitende eintrag abgespeichert
    # in dieser separaten datenbank befindet sich jeweils nur der zu bearbeitende eintrag
    with open("database_jogging_edit.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database_jogging_edit.csv" abgespeichert werden kann
        dict_del_updated = json.dumps(dict_del)
        write_file.write(dict_del_updated)
        open_file.close()



# bei dieser funktion wird der ausgewählte bearbeitete eintrag bei den bodyvalues aktualisiert bzw. wieder hinzugefügt, da er zuvor gelöscht wurde
def abspeichern_edit(datum, gewicht, bodyfat, tbw, muskeln, bmi, nummer):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue dict erstellt mit den aktualisierten daten als inhalt
    new_content = {nummer: {"datum": datum,
                            "gewicht": gewicht,
                            "bodyfat": bodyfat,
                            "tbw": tbw,
                            "muskeln": muskeln,
                            "bmi": bmi,
                            "nummer": nummer,
                            "bodyfat_kg": round(float(bodyfat) * float(gewicht) / 100, 1),
                            "muskeln_kg": round(float(muskeln) * float(gewicht) / 100, 1), }
                   }
    # hier werden die neuen aktualisierten daten der dict hinzugefügt
    inhalt.update(new_content)

    # hier wird die aktualisierte datenbank überschrieben
    with open("database.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database.csv" abgespeichert werden kann
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)

# bei dieser funktion wird der ausgewählte bearbeitete eintrag beim jogging aktualisiert bzw. wieder hinzugefügt, da er zuvor gelöscht wurde
def abspeichern_jogging_edit(datum, strecke, zeit, nummer):
    with open("database_jogging.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue dict erstellt mit den aktualisierten daten als inhalt
    new_content = {nummer: {"datum": datum,
                                      "strecke": strecke,
                                      "zeit": zeit,
                                      "km_schnitt": round(float(zeit) / float(strecke), 2),
                                      "nummer": nummer, }
                   }
    # hier werden die neuen aktualisierten daten der dict hinzugefügt
    inhalt.update(new_content)

    # hier wird die aktualisierte datenbank überschrieben
    with open("database_jogging.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database_jogging.csv" abgespeichert werden kann
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)

# bei dieser funktion wird der eintrag bei den bodyvalues hinzugefügt
def abspeichern(datum, gewicht, bodyfat, tbw, muskeln, bmi):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue nummer für den eintrag generiert
    # dabei wird geschaut, welche nummer der zuletzt hinzugefügte eintrag hat (dieser hat durch diese methode immer die höchste nummer)
    # dieser nummer wird 1 hinzugefügt, so entsteht die neue identifikationsnummer
    last_key = list(inhalt)[-1]
    new_entry_number = int(last_key) + 1
    # hier wird eine neue dict erstellt mit den neuen daten als inhalt
    new_content = {new_entry_number: {"datum": datum,
                                      "gewicht": gewicht,
                                      "bodyfat": bodyfat,
                                      "tbw": tbw,
                                      "muskeln": muskeln,
                                      "bmi": bmi,
                                      "nummer": new_entry_number,
                                      "bodyfat_kg": round(float(bodyfat) * float(gewicht) / 100, 1),
                                      "muskeln_kg": round(float(muskeln) * float(gewicht) / 100, 1), }
                   }
    # hier werden die neuen neuen daten der dict hinzugefügt
    inhalt.update(new_content)

    # hier wird die datenbank mit den neuen daten überschrieben
    with open("database.csv", "w") as write_file:
        # hier wird das dict wieder zu einem string umgewandelt, damit es wieder in "database.csv" abgespeichert werden kann
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)


# bei dieser funktion wird der eintrag beim jogging hinzugefügt
def abspeichern_jogging(datum, strecke, zeit):
    with open("database_jogging.csv", "r") as open_file:
        inhalt_string = open_file.read()
        # da es beim auslesen zu einem string wird, wird es hier zu einem dict umgewandelt
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    # hier wird eine neue nummer für den eintrag generiert
    # dabei wird geschaut, welche nummer der zuletzt hinzugefügte eintrag hat (dieser hat durch diese methode immer die höchste nummer)
    # dieser nummer wird 1 hinzugefügt, so entsteht die neue identifikationsnummer
    last_key = list(inhalt)[-1]
    new_entry_number = int(last_key) + 1
    # hier wird eine neue dict erstellt mit den neuen daten als inhalt
    new_content = {new_entry_number: {"datum": datum,
                                      "strecke": strecke,
                                      "zeit": zeit,
                                      "km_schnitt": round(float(zeit) / float(strecke), 2),
                                      "nummer": new_entry_number, }
                   }
    # hier werden die neuen neuen daten der dict hinzugefügt
    inhalt.update(new_content)

    # hier wird die datenbank mit den neuen daten überschrieben
    with open("database_jogging.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)