import unittest
from app import app

class ChatbotTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chatbot_response(self):
        response = self.app.get('/chatbot?city=Cancun&currency=USD&adults=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Encontré algunos lugares interesantes en Cancun.", response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
