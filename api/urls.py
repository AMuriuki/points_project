from django.urls import path
from api.views import process_grid_points

urlpatterns = [
    path("process-grid-points/", process_grid_points, name="process_grid_points")
]
