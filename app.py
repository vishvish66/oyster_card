# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from oys import OysterCard, Station, Trip

app = Flask(__name__)
app.secret_key = 'oyster_secret_key'

# Initialize the Oyster Card with a default balance
card = OysterCard()
card.load(30.0)


@app.route('/')
def index():
    balance = card.get_balance()
    return render_template('index.html', balance=balance)


@app.route('/load', methods=['POST'])
def load_money():
    try:
        amount = float(request.form['amount'])
        card.load(amount)
        flash(f'Successfully loaded £{amount:.2f} onto your card.')
    except ValueError:
        flash('Invalid amount. Please enter a valid number.', 'error')
    return redirect(url_for('index'))


@app.route('/trip', methods=['POST'])
def take_trip():
    start_station_name = request.form['start_station']
    end_station_name = request.form['end_station']

    start_station = Station(start_station_name, [1])
    end_station = Station(end_station_name, [1, 2])

    trip = Trip(start_station, end_station)
    try:
        card.make_trip(trip)
        flash(f'Trip from {start_station_name} to {end_station_name} completed.')
    except ValueError as e:
        flash(str(e), 'error')
    return redirect(url_for('index'))


@app.route('/bus', methods=['POST'])
def take_bus_trip():
    try:
        card.bus_trip()
        flash('Bus trip completed.')
    except ValueError as e:
        flash(str(e), 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
