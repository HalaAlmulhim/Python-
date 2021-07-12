from django.urls import path
from . import views

urlpatterns = [
    path("", views.books),
    path("add_books", views.add_books),
    path("books/<int:id>", views.display_books),
    path("addbook", views.add_book_base_author),
    path("authors", views.authors),
    path("add_authors", views.add_authors),
    path("authors/<int:id>", views.display_authors),
    path("display_authors", views.display_authors),
    path("add_authors", views.add_author_base_book),
]

