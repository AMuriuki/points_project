from django.db import models
import math

# Create your models here.


def euclidean_distance(x1, y1, x2, y2):
    """
    Calculates the distance of a straight line between two
    points in a two-dimensional space.

    Args:
        x1 (int): X-coordinate of the first point
        y1 (int): Y-coordinate of the first point
        x2 (int): X-coordinate of the second point
        y2 (int): Y-coordinate of the second point

    Returns:
        The Euclidean distance between the two points
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    closest_point = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return f"{self.x},{self.y}"

    def closest_point(self):
        # avoid including current point as its own closest point
        queryset = Point.objects.exclude(id=self.id)

        closest_point = min(
            queryset, key=lambda p: euclidean_distance(self.x, self.y, p.x, p.y)
        )

        return closest_point
