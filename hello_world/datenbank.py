import ast
import json

def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
    return inhalt_string

def abspeichern(vorname, nachname):
    with open("database.csv", "r") as open_file:
        inhalt_string = open_file.read()
        inhalt = ast.literal_eval(str(inhalt_string))
        open_file.close()

    if vorname not in inhalt.items():
        new_content = {vorname: nachname}
        inhalt.update(new_content)
        with open("database.csv", "w") as write_file:
            inhalt_updated = json.dumps(inhalt)
            write_file.write(inhalt_updated)