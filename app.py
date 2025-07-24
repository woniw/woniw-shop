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


#! ITEM FUNCTIONS
#? ----------------------------------------------------
@app.route('/headphones_buy_now_button', methods=['POST', "GET"])
def headphones_buy_now_button():

    if request.method == "POST":
        data['temp_buy_now']["current_Item"] = "headphones"
        data['temp_buy_now']["price"] = 250

        save_json("data.json", data)
        print(f"{bright_green} json saved!")

        return redirect(url_for("buy_now_page"))
    else:
        return redirect(url_for("index"))



@app.route('/clear_temp_json', methods=["POST", "GET"])
def clear_temp_json():
    if request.method == 'POST':
        from data.python_function import clear_temp_buy_now
        clear_temp_buy_now()

        print(f'{bright_green}CLEARED!')

        save_json("data.json", data)
        return render_template("index.html", balance=data['balance'])
    else:
        return render_template("index.html", balance=data['balance'])

@app.route("/reset_balance")
def reset_balance():
    from data.python_function import save_json

    print(f'{bright_magenta}balance: {data['balance']}')
    save_json("data.json", data) 

    data['balance'] -= data['balance']
    print(f'{bright_magenta}balance: {data['balance']}')
    save_json("data.json", data)

    data['balance'] += 1000
    print(f'{bright_magenta}balance: {data['balance']}')
    save_json("data.json", data)
    
    print(f"{bright_magenta}WORKING")
    return render_template("index.html", balance=data['balance'])

if __name__ == "__main__":
    app.run(debug=True)
