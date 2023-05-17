from django.test import TestCase, Client


class ProcessGridPointsAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_process_grid_points(self):
        data = {"points": "2,2;-1,30;20,11;4,5"}

        response = self.client.post("/api/process-grid-points/", data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"message": "Grid points processed successfully"}
        )

    def test_process_no_grid_points(self):
        data = {}  # Empty data, no points provided

        response = self.client.post("/api/process-grid-points/", data=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error", "No points provided"})

    def test_process_malformed_grid_points(self):
        data = {"points": "2,2;-1,30;20,11;4"}  # missing coordinate for one point

        response = self.client.post("/api/process-grid-points/", data=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error", "Malformed points"})
