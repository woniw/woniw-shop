from flask import Flask, render_template, request, jsonify, url_for, redirect
from data.variables import data
from data.variables import bright_red
from data.variables import bright_green
from data.variables import bright_blue 
from data.variables import bright_yellow
from data.variables import bright_magenta
from data.variables import bright_white
from data.python_function import save_json
import logging

print(f"{bright_blue} LOG: {data}")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", balance=data['balance']) 

@app.route("/cancel_payment")
def cancel_payment():
    index_url = url_for("index")
    return render_template("cancel_payment.html", index_url=index_url)

@app.route('/payment_confirmed')
def payment_confirmed():
    index_url = url_for("index")
    return render_template("payment_confirmed.html", index_url=index_url)

@app.route('/insufficent_funds')
def insufficent_funds():
    index_url = url_for("index")
    return render_template("insufficent_funds.html", index_url=index_url)

@app.route('/buy_now_page')
def buy_now_page():
    item_purchase = data['temp_buy_now']['current_Item']
    item_price = data['temp_buy_now']["price"]
    cancel_payment_url = url_for("cancel_payment")
    insufficient_funds_message = "insufficient funds"

    return render_template("buy_now_page.html", item_purchase=item_purchase, item_price=item_price, cancel_payment_url=cancel_payment_url)

@app.route('/about_page')
def about_page():
    index_url = url_for("index")
    return render_template("about.html", index_url=index_url)

@app.route("/account_page")
def account_page():
    index_url = url_for("index")
    return render_template("account.html", index_url=index_url)

@app.route("/confirm_payment", methods=['POST', 'GET'])
def confirm_payment():
    if request.method == "POST":
        #! subtracting price
        balance = data['balance']
        item_price = data["temp_buy_now"]["price"]

        print(f"{bright_yellow}USER BALANCE: {balance}")
        print(f"{bright_yellow}ITEM PRICE: {item_price}")

        if balance >= item_price:
            new_balance = balance - item_price
            print(f"{bright_red}NEW BALANCE: {new_balance}")

            data["balance"] = new_balance
            from data.python_function import clear_temp_buy_now
            clear_temp_buy_now()

            save_json('data.json', data)

            return redirect(url_for("payment_confirmed"))
        elif item_price > balance:
            from data.python_function import clear_temp_buy_now
            clear_temp_buy_now()       
            return redirect(url_for("insufficent_funds"))

#! REDIRECT PAGE

@app.route('/redirect_to_about_page')
def redirect_to_about_page():
    print("ABOUT BUTTON DETECTED")
    return redirect(url_for("about_page"))

@app.route('/redirect_to_account_page')
def redirect_to_account_page():
    return redirect(url_for("account_page"))

#! ITEM FUNCTIONS
#? ----------------------------------------------------
@app.route('/headphones_buy_now_button', methods=['POST', "GET"])
def headphones_buy_now_button():

    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "headphones"
        data['temp_buy_now']["price"] = data['items']['headphones']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))


@app.route('/optimus_buy_now_button', methods=['POST', "GET"])
def optimus_buy_now_button():

    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "optimus prime"
        data['temp_buy_now']["price"] = data['items']['optimus_prime']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/iman_buy_now_button', methods=['POST', "GET"])
def iman_buy_now_button():

    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Iman"
        data['temp_buy_now']["price"] = data['items']['Iman']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/gems_buy_now_button', methods=['POST', "GET"])
def gems_buy_now_button():

    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Gems"
        data['temp_buy_now']["price"] = data['items']['gems']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/mighty_miner_buy_now_button', methods=['POST', "GET"])
def mighty_miner_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Mighty Miner"
        data['temp_buy_now']["price"] = data['items']['mighty_miner']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/amin_buy_now_button', methods=['POST', "GET"])
def amin_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Amin eyvaz"
        data['temp_buy_now']["price"] = data['items']['amin']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/shiny_amin_buy_now_button', methods=['POST', "GET"])
def shiny_amin_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Shiny Amin"
        data['temp_buy_now']["price"] = data['items']['shiny amin']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/amin_eyvaz_buy_now_button', methods=['POST', "GET"])
def amin_eyvaz_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Amin eyvaz"
        data['temp_buy_now']["price"] = data['items']['amin']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/mikael_buy_now_button', methods=['POST', "GET"])
def mikael_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Mikael"
        data['temp_buy_now']["price"] = data['items']['mikael']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/homad_buy_now_button', methods=['POST', "GET"])
def homad_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Green Homad"
        data['temp_buy_now']["price"] = data['items']['homad']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/opp_detector_buy_now_button', methods=['POST', "GET"])
def opp_detector_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "opp detector"
        data['temp_buy_now']["price"] = data['items']['opp detector']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/shayan_buy_now_button', methods=['POST', "GET"])
def shayan_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Shayan"
        data['temp_buy_now']["price"] = data['items']['shayan']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))

@app.route('/ahmad_buy_now_button', methods=['POST', "GET"])
def ahmad_buy_now_button():
    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "Ahmad"
        data['temp_buy_now']["price"] = data['items']['ahmad']["price"]

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))


#! OTHER FUNCTIONS
@app.route("/reset_balance")
def reset_balance():
    from data.python_function import save_json

    print(f'{bright_magenta}balance: {data['balance']}')
    save_json("data.json", data) 

    data['balance'] += 1000
    print(f'{bright_magenta}balance: {data['balance']}')
    save_json("data.json", data)
    
    print(f"{bright_magenta}WORKING")
    return render_template("index.html", balance=data['balance'])

if __name__ == "__main__":
    app.run(debug=True)
