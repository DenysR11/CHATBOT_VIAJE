import requests
from config import RAPIDAPI_KEY, AIRBNB_HOST, BOOKING_HOST

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
