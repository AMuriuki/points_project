from django.test import TestCase, Client


class HelloWorldAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_world(self):
        response = self.client.get("/api/hello-world/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Hello world"})
