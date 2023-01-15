import ast
import json

def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string


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

    dict_del = {}
    for number in neue_liste:
        if int(nummer_del) == int(number[6][1]):
            print("lol")
        else:
            dict_temp = {number[6][1]: {"datum": number[0][1],
                                      "gewicht": number[1][1],
                                      "bodyfat": number[2][1],
                                      "tbw": number[3][1],
                                      "muskeln": number[4][1],
                                      "bmi": number[5][1],
                                      "nummer": number[6][1],}
                         }
            dict_del.update(dict_temp)
    inhalt.clear()
    inhalt.update(dict_del)
    with open("database.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)
        open_file.close()


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