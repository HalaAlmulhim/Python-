from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'visit' in request.session:
        request.session['visit'] += 1
    else:
        request.session['visit'] = 1

    return render(request, "index.html")


def destroy(request):
    del request.session['visit']
    return redirect("/")