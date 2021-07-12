from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/shows/new')
    else:
        title=request.POST['title']
        network=request.POST['network']
        date=request.POST['date']
        desc=request.POST['desc']
        new = Show.objects.create(
                title=title, 
                network=network, 
                release_date=date, 
                describtion=desc)
        return redirect('/shows/'+str(new.id))

def edit(request, show_id):
    context={
        "id": show_id
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    show_edit = Show.objects.get(id=show_id)
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/shows/'+str(show_id)+'/edit')
    else:
        show_edit.title = request.POST['title']
        show_edit.network = request.POST['network']
        show_edit.release_date = request.POST['date']
        show_edit.description = request.POST['desc']
        return redirect('/shows/'+str(show_id))

def show(request, show_id):
    show_details=Show.objects.get(id=show_id)
    context={
        "id": show_id,
        "show_title": show_details.title,
        "show_network": show_details.network,
        "show_rel_date": show_details.release_date,
        "show_description": show_details.describtion,
        "show_last_update": show_details.updated_at,
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    get_show=Show.objects.get(id=show_id)
    get_show.delete()
    return redirect('/shows')