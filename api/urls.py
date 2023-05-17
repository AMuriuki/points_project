from django.urls import path
from api.views import hello_world

urlpatterns = [path("hello-world/", hello_world, name="hello_world")]
