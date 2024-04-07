import json
import requests
from flask import Flask, jsonify, request

# API endpoint URL's and access keys
WMATA_API_KEY = "695bfccd41cc4d42869fc4d140c0f17a"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)
@app.route("/incidents/<unit_type>s", methods=["GET"])

def get_incidents(unit_type):
    # Example URL for WMATA API (adjust according to actual requirements)
    response = requests.get(INCIDENTS_URL, headers=headers)
    incidents = response.json()['ElevatorIncidents']
    filtered_incidents = [incident for incident in incidents if incident['UnitType'].lower() == unit_type.lower()]

    # Transform filtered_incidents into the desired format
    return jsonify(filtered_incidents)

if __name__ == '__main__':
    app.run(debug=True)

