from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("registration", views.registration),
    path("success", views.success_page),
    path("login", views.login),
    path("logout", views.logout),
]

