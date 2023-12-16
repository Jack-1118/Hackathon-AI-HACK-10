from flask import Flask, request, render_template
from input import insert_ai
import re
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('creatingTrip.html')

@app.route('/input', methods=['POST'])
def sum():
    country = request.form['country']
    state = request.form['state']
    day = request.form['days']
    insert_ai(country, state, day)
    return render_template('itinerary.html')


@app.route('/get-data')
def get_data():
    with open('output.txt', 'r') as f:
        data = f.read()
    return data


if __name__ == '__main__':
    app.run(debug=True)