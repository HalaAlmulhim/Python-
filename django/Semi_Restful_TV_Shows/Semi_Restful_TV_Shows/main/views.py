from django.shortcuts import render, HttpResponse, redirect
from .models import *



def index(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, "new.html")


def create(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']
    Show.objects.create(title= title , network=network , release_date=release_date , description= description)
    return redirect("/")

def edit(request, id):
    one_show = Show.objects.get(id=id)
    context = {
        'show': one_show,
    }
    return render(request, "edit.html", context)

def show(request, id):
    one_show = Show.objects.get(id=id)
    context = {
        'show': one_show,
    }
    return render(request, "display.html", context)

def update(request, id):
    show_id = Show.objects.get(id=id)
    show_id.title = request.POST['title']

    show_id.network = request.POST['network']

    show_id.release_date = request.POST['release_date']

    show_id.description = request.POST['description']
    show_id.save()
    return redirect("/shows/")





def delete(request, id):
    book_id = Show.objects.get(id=id)
    book_id.delete() 
    return redirect("/")





# def shows(request):
#     context = {
#         "all_shows": Show.objects.all(),
#     }

#     return render(request, "shows.html", context)


# def new_shows(request):
#     title = request.POST['title']
#     network = request.POST['network']
#     release_date = request.POST['release_date']
#     description = request.POST['description']
#     Show.objects.create(title= title , network=network , release_date=release_date , description= description)
#     return render(request, "new.html")

# def create_shows(request):
#     title = request.POST['title']
#     network = request.POST['network']
#     release_date = request.POST['release_date']
#     description = request.POST['description']
#     Show.objects.create(title= title , network=network , release_date=release_date , description= description)
#     return redirect("/shows/")

# def delete_shows(request, id):
#     # book_id = request.session['book.id']
#     book_id = Show.objects.get(id=id)
#     book_id.delete()
  
#     return redirect("/shows")

# def display_shows(request, id):
#     one_show = Show.objects.get(id=id)

#     context = {
#         'show': one_show,
#     }

#     return render(request, "display.html", context)


# def edit_shows(request, id):
#     # title = request.POST['title']
#     # description = request.POST['description']
#     # Book.objects.create(title= title , desc= description)
#     # return redirect("/")
#     return render(request, "edit.html")


# # def display_authors(request):
# #     pass
# #     context = {
# #         "all_authors": Book.objects.all(),
# #         "all_authors": Author.objects.all(),
# #     }

# #     return render(request, "bookscontent.html", context)

    
   
