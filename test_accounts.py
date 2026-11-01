"""Unit tests for sample Accounts Service endpoints."""
import unittest
from app import app


class AccountsServiceTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'ok')

    def test_accounts(self):
        response = self.client.get('/accounts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['accounts'], [])
