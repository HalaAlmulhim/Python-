from django.shortcuts import render, HttpResponse, redirect
# from .models import *
from .models import *

def home(request):
    context = {
        "all_dojo": Dojos.objects.all(),
        "all_ninja": Ninjas.objects.all(),
    }

    return render(request, "index.html", context)


def addDojo(request):
    fullname = request.POST['fullname']
    city = request.POST['city']
    state = request.POST['state']
    Dojos.objects.create(name= fullname , city= city, state= state )
    return redirect("/")

def addNinja(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    # first way
    dojo = request.POST['dojo']
    dojo_id = Dojos.objects.get(id = dojo)
    Ninjas.objects.create(dojo_id = dojo_id , first_name= firstname , last_name= lastname )

    # second way
    # dojo = Dojos.objects.get(id = request.POST['dojo'])  
    # Ninjas.objects.create(dojo_id = dojo , first_name= firstname , last_name= lastname )
    return redirect("/")





