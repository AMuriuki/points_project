from django.contrib import admin
from .models import Point


class PointAdmin(admin.ModelAdmin):
    list_display = ("id", "x", "y", "closest_point")
    readonly_fields = ("closest_point",)

    def closest_point(self, obj):
        return obj.closest_point()

    closest_point.short_description = "Closest Point"


admin.site.register(Point, PointAdmin)
