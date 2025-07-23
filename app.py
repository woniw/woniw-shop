from flask import Flask, render_template, request, jsonify, url_for, redirect
from data.variables import data
from data.variables import bright_red
from data.variables import bright_green
from data.variables import bright_blue 
from data.variables import bright_yellow

print(f"{bright_blue} LOG: {data}")

app = Flask(__name__)

@app.route('/')
def index():
    balance = data['balance']
    return render_template("index.html")

@app.route("/dummy_site")
def dummy_site():
    return render_template("dummy_site.html")

@app.route('/headphones_buy_now_button', methods=['POST', "GET"])
def headphones_buy_now_button():

    if request.method == "POST":
        print(f"{bright_yellow}LOG: working")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
