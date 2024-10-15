from flask import Flask, render_template

app = Flask("Website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/b1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
