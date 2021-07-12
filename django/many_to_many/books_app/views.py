from django.shortcuts import render, HttpResponse, redirect
from .models import *

def books(request):
    context = {
        "all_books": Book.objects.all(),
        "all_publisher": Publisher.objects.all(),
    }

    return render(request, "index.html", context)

    