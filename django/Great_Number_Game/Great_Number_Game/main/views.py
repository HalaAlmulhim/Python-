from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'num' not in request.session:
        request.session['num'] = random.randint(1, 100)
    return render(request, "index.html")

def result(request):
    if int(request.POST['guess']) == request.session['num']:
        request.session['result'] = "correct"
    elif int(request.POST['guess']) > request.session['num']:
        request.session['result'] = "high"
    elif int(request.POST['guess']) < request.session['num']:
        request.session['result'] = "low"

    return redirect("/")

def clear(request):
    request.session.flush()
    return redirect("/")