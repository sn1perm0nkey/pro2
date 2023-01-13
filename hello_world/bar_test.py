import plotly.express as px
import pandas as pd


#@app.route("/viz")
#def grafik():
#    fig = px.pie(labels=[1, 2, 3, 4, 5], values=[6, 7, 8, 9, 10])
#    div = plot(fig, output_type="div")

#    return render_template("viz.html", barchart=div)



@app.route("/viz")
def grafik():
    fig = px.pie(labels=[1, 2, 3, 4, 5], values=[6, 7, 8, 9, 10])
    div = plot(fig, output_type="div")

    return render_template("viz.html", barchart=div, seitentitel="Chart")