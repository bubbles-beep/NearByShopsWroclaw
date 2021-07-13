from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = 51.1078852
latitude = 17.0385376

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "shops/index.html"


home = Home.as_view()