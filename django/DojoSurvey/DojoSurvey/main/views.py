from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def  results(request):
    context = {
        "name" : request.POST['name'],
        "location" : request.POST['location'],
        "lang" : request.POST['lang'],
        "comment" : request.POST['comment'],
    }
    return render(request, "results.html", context)