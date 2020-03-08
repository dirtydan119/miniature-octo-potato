import requests

base_currency = input("What currency would you like to look up?").upper()
amount = input("What amount do you have?")
converted_currency = input("What currency would you like it converted to?")

r = requests.get("https://api.exchangeratesapi.io/latest?base=" + base_currency)

json_object = r.json()

conversion = (json_object["rates"][converted_currency] * float(amount))

print(str(conversion) + " " + converted_currency)
