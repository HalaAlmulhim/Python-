from django.shortcuts import render, HttpResponse, redirect
# from .models import *
from .models import User

def home(request):
    context = {
        "all_user": User.objects.all(),
    }

    return render(request, "index.html", context)


def add(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    emailaddress = request.POST['email']
    age= int(request.POST['age'])
    User.objects.create(first_name= firstname , last_name= lastname, email_address= emailaddress , age= age )
    return redirect("/")





