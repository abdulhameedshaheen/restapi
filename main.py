from flask import Flask, render_template
import pandas as pd
# Create Website Onject
app = Flask(__name__)


# connect HTML with the website obj
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "datasmall/TG_STAID" + str(station).zfill(6) + ".txt"
    df =pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}


#if __name__ == "__name__":
app.run(debug=True)
