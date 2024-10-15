from flask import Flask, render_template
# name is a special variable, only run website when script is executed directly
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pandas...
    temperature = 23
    # return str(temperature)
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
