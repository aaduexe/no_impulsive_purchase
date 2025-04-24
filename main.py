from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route("/")

def startHere():
    return render_template("index.html")

@app.route("/adder")
def addItem():
    return render_template("adder.html")

@app.route("/decide")
def dataDropDown():
    column_data = []
    with open('data/wishes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            column_data.append(row['Wish'])  # Change 'City' to your column name

    return render_template("decider.html", items=column_data)

@app.route("/quest")
def questions():
    return render_template("questionaire.html")

if __name__ == "__main__":
    app.run(debug=True)
