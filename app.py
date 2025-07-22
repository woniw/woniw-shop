from flask import Flask, render_template, request, jsonify, url_for, redirect
from data.variables import data
from data.variables import bright_red
from data.variables import bright_green
from data.variables import bright_blue 

print(f"{bright_blue} LOG: {data}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
