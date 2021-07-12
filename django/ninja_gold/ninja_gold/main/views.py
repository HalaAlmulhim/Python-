from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if 'yr_gold' not in request.session:
        request.session['yr_gold'] = 0
        request.session['msgs'] = {}
    return render(request, "index.html")


def process_money(request):

    if request.POST['gold'] == "Farm":
        earn = random.randint(10, 20)
        request.session['yr_gold'] += earn
        request.session['msgs'][f"Earned {earn} golds from Farm! (" + strftime("%Y-%m-%d %H:%M %p", gmtime())+")"] = False
    elif request.POST['gold'] == "Cave":
        earn = random.randint(5, 10)
        request.session['yr_gold'] += earn
        request.session['msgs'][f"Earned {earn} golds from Cave! (" + strftime("%Y-%m-%d %H:%M %p", gmtime())+")"] = False
    elif request.POST['gold'] == "House":
        earn = random.randint(2, 5)
        request.session['yr_gold'] += earn
        request.session['msgs'][f"Earned {earn} golds from House! (" + strftime("%Y-%m-%d %H:%M %p", gmtime())+")"] = False
    else:
        earn = random.randint(-50, 50)
        request.session['yr_gold'] += earn
        if earn >= 0:
            request.session['msgs'][f"Earned {earn} golds from Casino! (" + strftime("%Y-%m-%d %H:%M %p", gmtime())+")"] = False
        else:
            request.session['msgs'][f"Entered a Casino and lost {abs(earn)} golds... Ouch.. (" + strftime("%Y-%m-%d %H:%M %p", gmtime())+")"] = True

    return redirect("/")

def clear(request):
    request.session.flush()
    return redirect("/")
