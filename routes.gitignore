from flask import Flask, jsonify, request
from controllers import search_airbnb_properties, search_booking_attractions

app = Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def chatbot():
    city = request.args.get('city', 'Cancun')
    currency = request.args.get('currency', 'USD')
    adults = request.args.get('adults', 1)

    airbnb_data = search_airbnb_properties(city, currency, adults)
    booking_data = search_booking_attractions(city, currency)

    return jsonify({
        "response": f"Encontré algunos lugares interesantes en {city}.",
        "airbnb_properties": airbnb_data,
        "booking_attractions": booking_data
    })
