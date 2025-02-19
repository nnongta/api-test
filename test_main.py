import unittest
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_plus(self):
        response = self.client.get('/plus/5/6')
        self.assertEqual(response.data.decode(), '11')

if __name__ == '__main__':
    unittest.main()
