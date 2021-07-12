from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("addDojo", views.addDojo),
    path("addNinja", views.addNinja),
]

