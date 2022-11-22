from flask import Flask
from flask import render_template
from flask import request

app = Flask("todoloo")


@app.route("/")
def start():
    return "ok"


@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("todo_form.html")

    if request.method == "POST":
        print(request.form['aufgabe'])
        return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
