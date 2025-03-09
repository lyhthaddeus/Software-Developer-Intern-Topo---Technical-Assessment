import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from api.api import api

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api)
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_json_data(self):
        response = self.client.get('/api/data/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

    def test_get_csv_data(self):
        response = self.client.get('/api/data/csv')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_pptx_data(self):
        response = self.client.get('/api/data/pptx')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_pdf_data(self):
        response = self.client.get('/api/data/pdf')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_unified_data(self):
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

    def test_activity_to_revenue(self):
        response = self.client.get('/api/utils/activity_to_revenue')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

    def test_location_to_revenue(self):
        response = self.client.get('/api/utils/location_to_revenue')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

if __name__ == '__main__':
    unittest.main()