#export FLASK_DEBUG=1
#env FLASK_APP=flask/main.py flask ruN

from flask import Flask, escape, request
import json, requests

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/venues')
def api_venues():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    data = get_venues_from_4S(lat, lon)

    return json.dumps(data)

def get_venues_from_4S(lat, lon):
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
        client_id='3RNDXJL151HQQ4MXSQ5YPXBLDXTUSEN4XHI3KT0FYI132OYU',
        client_secret='UULONCCNSBPVGNZHK20QCQFNK5VBL24O2FTCQXL0ZORLCBQL',
        v='20180323',
        ll=str(lat) + "," + str(lon),
        section='sights',
        limit=3
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    if data["meta"]["code"] == 200:

        response = []

        venues = data["response"]["groups"][0]["items"]
        for venue in venues:
            venue = venue["venue"]
            venue_inf = {}
            venue_inf["name"] = venue["name"]
            venue_inf["location"] = venue["location"]
            venue_inf["distance"] = venue["location"]["distance"]
            venue_inf["pretty_address"] = venue["location"]["formattedAddress"]
            venue_inf["category"] = {
                "name": venue["categories"][0]["name"],
                "icon": "https://example.com"
            }
            venue_inf["checkin_count"] = venue["stats"]["checkinsCount"]
            venue_inf["verified"] = venue["verified"]
            response.append(venue_inf)

        return response
    else:
        return {"status":"error","message":"non-200 response from server"}