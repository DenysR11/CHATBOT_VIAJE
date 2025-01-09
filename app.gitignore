from config import RAPIDAPI_KEY, AIRBNB_HOST, BOOKING_HOST
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Configuración de las APIs
RAPIDAPI_KEY = 'tu_clave_rapidapi'
AIRBNB_HOST = 'airbnb19.p.rapidapi.com'
BOOKING_HOST = 'booking-com15.p.rapidapi.com'

# Función para buscar propiedades en Airbnb
def search_airbnb_properties(city, currency='USD', adults=1):
    url = "https://airbnb19.p.rapidapi.com/api/v1/searchPropertyByPlace"
    querystring = {
        "id": city,
        "display_name": city,
        "totalRecords": "10",
        "currency": currency,
        "adult": adults
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": AIRBNB_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json() if response.status_code == 200 else {"error": "Error en Airbnb API"}


def search_booking_attractions(city, currency='USD'):
    url = "https://booking-com15.p.rapidapi.com/api/v1/attraction/searchAttractions"
    querystring = {
        "id": city,
        "page": "1",
        "currency_code": currency,
        "languagecode": "en-us"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": BOOKING_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json() if response.status_code == 200 else {"error": "Error en Booking API"}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    city = request.form.get('city', 'Cancun')
    currency = request.form.get('currency', 'USD')
    adults = int(request.form.get('adults', 1))

    # Obtener datos de las APIs
    airbnb_data = search_airbnb_properties(city, currency, adults)
    booking_data = search_booking_attractions(city, currency)

    return render_template('index.html', 
                           airbnb_properties=airbnb_data, 
                           booking_attractions=booking_data, 
                           city=city)

if __name__ == '__main__':
    app.run(debug=True)
