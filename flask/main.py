#export FLASK_DEBUG=1
#env FLASK_APP=flask/main.py flask run

from flask import Flask, escape, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
import json, requests

app = Flask(__name__,
            static_folder = "./static",
            template_folder = "./static")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/js/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    print(path)
    return send_from_directory('static/css', path)

@app.route("/api/otm/detail")
def api_venues_otm_detail():
    xid = request.args.get("xid")

    print(xid)
    data = get_venue_details_from_OTM(xid)

    return json.dumps(data)
    
@app.route("/api/otm")
def api_venues_otm():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if "radius" in request.args:
        radius = request.args.get('radius')
    else:
        radius = 3500
    
    if "categories" in request.args:
        categories = request.args.get('categories')
    else:
        categories = "interesting_places"

    data = get_venues_from_OTM(lat,lon, radius, categories)

    return json.dumps(data)



@app.route('/api/venues')
def api_venues():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    data = get_venues_from_4S(lat, lon)

    return json.dumps(data)

@app.route('/')
def serve_index():
    return render_template("index.html")

def get_venues_from_OTM(lat, lon, radius=3500, categories="interesting_places"):
    #radius=10000&lon=0.00001&lat=51.500944&kinds=interesting_places&format=json&apikey=5ae2e3f221c38a28845f05b677a3c8a48be4b3462eb96b2ca683d48c

    url = 'https://api.opentripmap.com/0.1/en/places/radius'

    params = dict(
        radius = radius,
        lon = lon,
        lat = lat,
        kinds = categories,
        format = "json",
        apikey = "5ae2e3f221c38a28845f05b677a3c8a48be4b3462eb96b2ca683d48c",
        limit = 25
        )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    print(resp.text)

    return data

def get_venue_details_from_OTM(xid):
    #https://api.opentripmap.com/0.1/en/places/xid/Q17550120?apikey=5ae2e3f221c38a28845f05b677a3c8a48be4b3462eb96b2ca683d48c
    url = 'https://api.opentripmap.com/0.1/en/places/xid/' + xid
    print(url)
    print("\n")

    params = dict(
        apikey = "5ae2e3f221c38a28845f05b677a3c8a48be4b3462eb96b2ca683d48c"
    )
    resp = requests.get(url=url, params=params)
    print(resp.url)
    data = json.loads(resp.text)
    print(resp.text)

    return data

def get_venues_from_4S(lat, lon):
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
        client_id='3RNDXJL151HQQ4MXSQ5YPXBLDXTUSEN4XHI3KT0FYI132OYU',
        client_secret='UULONCCNSBPVGNZHK20QCQFNK5VBL24O2FTCQXL0ZORLCBQL',
        v='20180323',
        ll=str(lat) + "," + str(lon),
        radius=300,
        #section='sights',
        limit=3,
        sortByDistance=1,
        categoryId="4deefb944765f83613cdba6e,4bf58dd8d48988d181941735,4bf58dd8d48988d1e2941735,4e0e22f5a56208c4ea9a85a0,4bf58dd8d48988d131941735,4f4530164b9074f6e4fb00ff"
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
