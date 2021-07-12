from django.shortcuts import render, HttpResponse, redirect
from .models import *

def books(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, "index.html", context)


def add_books(request):
    title = request.POST['title']
    description = request.POST['description']
    Book.objects.create(title= title , desc= description)
    return redirect("/")

def display_books(request, id):
    # id = request.session['book.id']
    one_book = Book.objects.get(id=id)
    context = {
        "book_one": one_book ,
        "all_authors_book_one" : one_book.authors.all(),
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }
  

    return render(request, "bookscontent.html", context)

def add_book_base_author(request):
    pass
    author_id = request.POST['author']
    one_author = Author.objects.get(id=author_id)
    Book.objects.create(title=one_book.title , one_author=authors)
    context = {
        "author_one": one_author.books.all() ,
    }

def authors(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, "author.html", context)


def add_authors(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    author_note = request.POST['note']
    Author.objects.create(first_name= fname , last_name = lname, notes= author_note)
    return redirect("/authors")


def display_authors(request, id):
    one_author = Author.objects.get(id=id)
    context = {
        "author_one": one_author,
        "all_books_author_one" : one_author.books.all(),
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, "author_content.html", context)
    
def add_author_base_book(request):
    pass
    book_id = request.POST['book']
    one_book = Book.objects.get(id=book_id)
    context = {
        "book_one": one_book.authors.all() ,
    }
    return redirect("books/{{author_id}}", context)  #wrong

 
