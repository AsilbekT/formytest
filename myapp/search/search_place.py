import requests
from.creadentials import api_key

def find_place(place):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={api_key}"
    res = requests.get(url)
    return res