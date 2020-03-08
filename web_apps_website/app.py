from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"

class CurrencyForm(FlaskForm):
    currency = StringField("Currency to convert: ")
    amount = StringField("Amount: ")
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/currency_conversion", methods=["GET", "POST"])
def currency_conversion():
    desired_currencies = {"USD": "US Dollar", "EUR": "Euro", "CAD": "Canadian Dollar", "GBP": "Brittish Pound", "AUD": "Australian Dollar", "CHF": "Swiss Franc", "RUB": "Russian Ruble", "JPY": "Japanese Yen", "NZD": "New Zeland Dollar", "ZAR": "South African Rand"}
    currency = False
    amount = False
    all_currencies = []
    json_object = {}
    float_amount = 0.0

    form = CurrencyForm()

    if form.validate_on_submit():
        currency = form.currency.data.upper()
        amount = form.amount.data
        float_amount = float(amount)
        r = requests.get("https://api.exchangeratesapi.io/latest?base=" + currency)
        json_object = r.json()
        all_currencies = [i for i in json_object["rates"]]
        form.currency.data = ""
        form.amount.data = ""


    return render_template("currency_convert.html", form=form, currency=currency, amount=amount, all_currencies=all_currencies, json_object=json_object, float_amount=float_amount, desired_currencies=desired_currencies)


if __name__ == "__main__":
    app.run(debug=True)
