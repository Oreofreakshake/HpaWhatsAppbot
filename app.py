from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from jsonpy import JsonSource
from options import Option

data_source = JsonSource("data/data.json")
data = data_source.data
listdata = data["en"]["options"]

app = Flask(__name__)


@app.route("/")
def bot():
    return "Hi bot is online!"


@app.route("/bot", methods=["POST"])
def main():
    msg = request.form.get("Body").lower()

    resp = MessagingResponse()

    if msg == "hello":
        bot_response = data["en"]["welcome"]
        resp.message(bot_response)
        indexvalue = [
            "1. Statistics",
            "2. Managing COVID 19",
            "3. Vaccination centers",
            "4. Flu clinics & sample collection centers",
            "5. Domestic travel criteria & islands",
            "6. Islands under monitoring",
            "7. Links and contacts",
            "8. Call 1676",
        ]
        for index in indexvalue:
            resp.message(index)

        return str(resp)

    if msg == "1":
        datagiven = Option("1")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "2":
        datagiven = Option("2")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "3":
        datagiven = Option("3")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "4":
        datagiven = Option("4")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "5":
        datagiven = Option("5")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "6":
        datagiven = Option("6")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "7":
        datagiven = Option("7")

        resp.message(datagiven.throwdata)
        return str(resp)
    if msg == "8":
        datagiven = Option("8")

        resp.message(datagiven.throwdata)
        return str(resp)

    else:
        resp.message("try saying hello")
        return str(resp)


if __name__ == "__main__":
    app.run()