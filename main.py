from flask import Flask, render_template
import pandas as pd

# Steps: i) insight needs, ii) data acquisition, iii) analysis data, iv) data visualization

# name is a special variable, only run website when script is executed directly
app = Flask(__name__)
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    str_date = str(date[0:4] + '-' + date[4:6] + '-' + date[6:8])
    temperature = df.loc[df['    DATE'] == str_date]['   TG'].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/<station>")
def station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.to_dict(orient="records")
    return {"station": station, "temperature": temperature}


@app.route("/api/v1/peryear/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    str_year = str(year)
    temperature = df.loc[df['    DATE'].str.startswith(str_year)].to_dict(orient="records")
    return {"station": station, "year": str_year, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, port=5001)
