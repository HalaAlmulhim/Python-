from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect(to)("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new from to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destory(request, number):
    return redirect("/blog")

#def jason(request):
#    lastEx(
#       title :"my first blog",
#       content : "lorem, ipsum dolor sit amet consecteture adipisicing elit..."
#    )
#        return HttpResponse(f"{lastEx[title]} {lastEx[content]}")