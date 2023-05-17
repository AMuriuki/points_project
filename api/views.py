from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def process_grid_points(request):
    points = request.data.get("points")
    if points:
        points_list = points.split(";")
        for point in points_list:
            coordinates = point.split(",")
            if len(coordinates) != 2:
                return Response({"error", "Malformed points"}, status=400)
        # TODO: Process points
        return Response({"message": "Grid points processed successfully"})
    else:
        return Response({"error", "No points provided"}, status=400)
