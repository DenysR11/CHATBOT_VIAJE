# api_client.py

import requests
from config import BOOKING_API_URL, BOOKING_API_KEY, BOOKING_HOST, AIRBNB_API_URL, AIRBNB_API_KEY, AIRBNB_HOST

def get_attractions_booking(location, page=1, currency="MXN", language="es"):
    headers = {
        "x-rapidapi-key": BOOKING_API_KEY,
        "x-rapidapi-host": BOOKING_HOST,
    }
    params = {
        "location_id": location,
        "page": page,
        "currency_code": currency,
        "languagecode": language
    }
    response = requests.get(BOOKING_API_URL, headers=headers, params=params)
    return response.json()

def get_properties_airbnb(location, records=10, currency="MXN", language="es"):
    headers = {
        "x-rapidapi-key": AIRBNB_API_KEY,
        "x-rapidapi-host": AIRBNB_HOST,
    }
    params = {
        "location_id": location,
        "totalRecords": records,
        "currency": currency,
        "display_name": language
    }
    response = requests.get(AIRBNB_API_URL, headers=headers, params=params)
    return response.json()
