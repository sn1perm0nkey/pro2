import ast
import json

def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string

def auslesen_del():
    with open("database_edit.csv", "r") as open_file:
        dict_del_string = open_file.read()
    return dict_del_string


def loeschen(nummer_del):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    dict_keep = {}
    for number in neue_liste:
        if int(nummer_del) != int(number[6][1]):
            dict_temp_keep = {number[6][1]: {"datum": number[0][1],
                                        "gewicht": number[1][1],
                                        "bodyfat": number[2][1],
                                        "tbw": number[3][1],
                                        "muskeln": number[4][1],
                                        "bmi": number[5][1],
                                        "nummer": number[6][1], }
                         }
            dict_keep.update(dict_temp_keep)


    inhalt.clear()
    inhalt.update(dict_keep)
    with open("database.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)
        open_file.close()


def loeschen_edit(nummer_del):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    neue_liste = []
    for eintrag in inhalt.values():
        test = {}
        test.update(eintrag)
        neue_liste2 = []
        for bezeichnung, wert in test.items():
            neue_liste2.append([bezeichnung, wert])
        neue_liste.append(neue_liste2)

    dict_del = {}
    for number in neue_liste:
        if int(nummer_del) == int(number[6][1]):
            dict_temp_del = {number[6][1]: {"datum": number[0][1],
                                        "gewicht": number[1][1],
                                        "bodyfat": number[2][1],
                                        "tbw": number[3][1],
                                        "muskeln": number[4][1],
                                        "bmi": number[5][1],
                                        "nummer": number[6][1], }
                         }
            dict_del.update(dict_temp_del)

    with open("database_edit.csv", "w") as write_file:
        dict_del_updated = json.dumps(dict_del)
        write_file.write(dict_del_updated)
        open_file.close()


def abspeichern_edit(datum, gewicht, bodyfat, tbw, muskeln, bmi, nummer):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    new_content = {nummer: {"datum": datum,
                                      "gewicht": gewicht,
                                      "bodyfat": bodyfat,
                                      "tbw": tbw,
                                      "muskeln": muskeln,
                                      "bmi": bmi,
                                      "nummer": nummer,}
                   }
    inhalt.update(new_content)

    with open("database.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)


def abspeichern(datum, gewicht, bodyfat, tbw, muskeln, bmi):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    last_key = list(inhalt)[-1]
    new_entry_number = int(last_key) + 1
    new_content = {new_entry_number: {"datum": datum,
                                      "gewicht": gewicht,
                                      "bodyfat": bodyfat,
                                      "tbw": tbw,
                                      "muskeln": muskeln,
                                      "bmi": bmi,
                                      "nummer": new_entry_number,}
                   }
    inhalt.update(new_content)
    with open("database.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)