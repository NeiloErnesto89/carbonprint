from django.urls import path

from . import views # import weather/views.py

# same pattern as url routing 
urlpatterns = [
    path("", views.index, name="weather"),
    path("emissions/", views.emissions, name="emissions"),

]