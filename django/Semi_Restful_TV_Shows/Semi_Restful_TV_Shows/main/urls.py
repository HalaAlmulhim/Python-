from django.urls import path
from . import views

urlpatterns = [
    # path("", views.shows),
    # path("new", views.new_shows),
    # path("shows/<int:id>", views.display_shows),
    # path("<int:id>/edit", views.edit_shows),
    # # path("shows/<int:id>/shows/new", views.new_shows),
    # path("<int:id>/delete", views.delete_shows),

    path("", views.index),
    path("new", views.new),
    path("create", views.create),
    path("<int:id>/update", views.update),
    path("<int:id>", views.show),
    path("<int:id>/edit", views.edit),
    path("<int:id>/delete", views.delete),

]

