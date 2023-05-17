from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Point

from api.serializer import PointSerializer


@api_view(["POST"])
def process_grid_points(request):
    serializer = PointSerializer(data=request.data)

    if serializer.is_valid():
        # Access the data
        validated_data = serializer.validated_data
        points = validated_data["points"]
        if points:
            points_list = points.split(";")
            all_points = []
            for point in points_list:
                coordinates = point.split(",")
                if len(coordinates) != 2:
                    return Response({"error", "Malformed points"}, status=400)
                all_points.append(Point(x=int(coordinates[0]), y=int(coordinates[1])))

            # save point instance to DB
            Point.objects.bulk_create(all_points)

            for point in all_points:
                point.closest_point = point.closest_point()
                point.save()

            return Response({"message": "Grid points processed successfully"})
    else:
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
