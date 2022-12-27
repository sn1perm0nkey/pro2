import ast
import json

def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string

def abspeichern(datum, gewicht, bodyfat, tbw, muskeln, bmi):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    entries = len(inhalt)
    new_entry_number = entries + 1
    new_content = {new_entry_number: {"datum": datum, "gewicht": gewicht, "bodyfat": bodyfat, "tbw": tbw, "muskeln": muskeln, "bmi": bmi}}
    inhalt.update(new_content)
    with open("database.csv", "w") as write_file:
        inhalt_updated = json.dumps(inhalt)
        write_file.write(inhalt_updated)