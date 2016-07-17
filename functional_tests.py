import unittest

import state_server

import requests


class FunctionalTests(unittest.TestCase):
    """Create at least one test to cover each of the states in the json file.
        Need to figure out how to start server as a background process as setUp is not working properly.
    """

    '''def setUp(self):
        state_server.run()

    def tearDown(self):
        state_server.destroy()'''

    def test_pennsylvania(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Pennsylvania', result.content)

    def test_washington(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Washington', result.content)

    def test_montana(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Montana', result.content)

    def test_maine(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Maine', result.content)

    def test_north_dakota(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('North Dakota', result.content)

    def test_south_dakota(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('South Dakota', result.content)

    def test_wyoming(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Wyoming', result.content)

    def test_wisconsin(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Wisconsin', result.content)

    def test_idaho(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Idaho', result.content)

    def test_vermont(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Vermont', result.content)

    def test_minnesota(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Minnesota', result.content)

    def test_oregon(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Oregon', result.content)

    def test_new_hampshire(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('New Hampshire', result.content)

    def test_iowa(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Iowa', result.content)

    def test_massachusetts(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Massachusetts', result.content)

    def test_nebraska(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Nebraska', result.content)

    def test_new_york(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('New York', result.content)

    def test_indiana(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Indiana', result.content)

    def test_nevada(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Nevada', result.content)

    def test_utah(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Utah', result.content)

    def test_california(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('California', result.content)

    def test_ohio(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Ohio', result.content)

    def test_illinois(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Illinois', result.content)

    def test_west_virginia(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('West Virginia', result.content)

    def test_maryland(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Maryland', result.content)

    def test_colorado(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Colorado', result.content)

    def test_kentucky(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Kentucky', result.content)

    def test_kansas(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Kansas', result.content)

    def test_virginia(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Virginia', result.content)

    def test_missouri(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Missouri', result.content)

    def test_arizona(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Arizona', result.content)

    def test_oklahoma(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Oklahoma', result.content)

    def test_north_carolina(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('North Carolina', result.content)

    def test_tennessee(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Tennessee', result.content)

    def test_texas(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Texas', result.content)

    def test_new_mexico(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('New Mexico', result.content)

    def test_alabama(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Alabama', result.content)

    def test_mississippi(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Mississippi', result.content)

    def test_georgia(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Georgia', result.content)

    def test_south_carolina(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('South Carolina', result.content)

    def test_arkansas(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Arkansas', result.content)

    def test_louisiana(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Louisiana', result.content)

    def test_florida(self):
        result = requests.post('http://localhost:8080', 'longitude=-77.036133&latitude=40.513799')
        self.assertEqual('Florida', result.content)

if __name__ == '__main__':
    unittest.main()
