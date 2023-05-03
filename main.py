from flask import Flask, render_template

# Create Website Onject
app = Flask(__name__)


# connect HTML with the website obj
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)
