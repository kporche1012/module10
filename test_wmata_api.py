from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # Initialize a fresh list for each test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

################################################################################
    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        # assert that the response code of 'incidents/escalators returns a 200 code

        elevator_response = app.test_client().get('/incidents/elevators').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code

        for endpoint in ['/incidents/escalators', '/incidents/elevators']:
            response = self.app.get(endpoint)
            self.assertEqual(response.status_code, 200)

################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response assert that each of the required fields
        # are present in the response

        fields = ['StationCode', 'StationName', 'UnitName', 'UnitType']
        response = self.app.get('/incidents/escalators')
        data = json.loads(response.data)
        for incident in data:
            for field in fields:
                self.assertIn(field, incident)

################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        response = self.app.get('/incidents/escalators')
        data = json.loads(response.data)
        for incident in data:
            self.assertEqual(incident['UnitType'], "ESCALATOR")

################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        response = self.app.get('/incidents/elevators')
        data = json.loads(response.data)
        for incident in data:
            self.assertEqual(incident['UnitType'], "ELEVATOR")

################################################################################

if __name__ == "__main__":
    unittest.main()