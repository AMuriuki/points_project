from django.test import TestCase, Client

from api.models import Point


class ProcessGridPointsAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_process_grid_points(self):
        # test data
        data = {"points": "2,2;-1,30;20,11;4,5"}

        # make POST request to the view
        response = self.client.post("/api/process-grid-points/", data=data)

        # assert response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"message": "Grid points processed successfully"}
        )

        # assert that the Point instances were created in the DB
        point_count = Point.objects.filter(
            x__in=[2, -1, 20, 4], y__in=[2, 30, 11, 5]
        ).count()
        self.assertEqual(point_count, 4)

        # retrieve one of the created points
        point1 = Point.objects.get(x=2, y=2)

        # call closest_point method to retrieve the closest point
        closest_point = point1.closest_point()

        # assert that the closest point is as expected
        expected_closest_point = Point.objects.get(x=4, y=5)
        self.assertEqual(closest_point, expected_closest_point)

    def test_process_malformed_grid_points(self):
        data = {"points": "2,2;-1,30;20,11;4"}  # missing coordinate for one point

        response = self.client.post("/api/process-grid-points/", data=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error", "Malformed points"})

    def test_process_no_grid_points(self):
        data = {}  # Empty data, no points provided

        response = self.client.post("/api/process-grid-points/", data=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"points": ["This field is required."]})
