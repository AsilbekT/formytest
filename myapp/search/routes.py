from flask import Blueprint
from flask import render_template, request
from .search_place import find_place
import logging
from slugify import slugify
from .calculate_distance import haversine

search = Blueprint("search", __name__)


@search.route('/search', methods=['GET', 'POST'])
def search_place():
    if request.method == "POST":
        data = request.form.to_dict()
        specified_address = slugify(data['address'])

        address1 = find_place("Moscow Ring Road")
        address2 = find_place(specified_address)
        location1 = address1.json()['results'][0]['geometry']['location']
        location2 = address2.json()['results'][0]['geometry']['location']
        lon1, lat1 = location1['lng'], location1['lat']
        lon2, lat2 = location2['lng'], location1['lat']
        distance = haversine(lon1, lat1, lon2, lat2)
        with open("output.log", 'a') as file:

            if distance < 108.9:
                file.append(f"inside MKAD\n")
            else:
                file.write(f"the distance between {data['address']} and Moscow Ring Road is {distance} km according to Haversine algorithm\n")

        return render_template('search.html', data=f"{address1.json()}, {address2.json()}")
    return render_template('search.html', data='')



