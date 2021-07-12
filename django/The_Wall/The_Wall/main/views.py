from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import *
import bcrypt

# Create your views here.
def root(request):
    return render(request, "index.html")

def register(request):
    request.session['action'] = "reg"

    errors = Users.objects.register_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        birthday = request.POST['date']

        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash ,birthday=birthday)

        request.session['id'] = user.id
        request.session['username'] = first_name
        return redirect("/wall")

def login(request):
    request.session['action'] = "login"
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        first_name = Users.objects.get(email=request.POST['email']).first_name
        user_id = Users.objects.get(email=request.POST['email']).id
        request.session['username'] = first_name
        request.session['id'] = user_id
        return redirect("/wall")



def wall(request):
    if request.session.is_empty():
        return redirect("/")
    else:
        context = {
            "all_users" : Users.objects.all(),
            "all_messages": Messages.objects.all().order_by('-id'),
            "all_commnets": Comments.objects.all(),
        }
        return render(request, "wall.html", context)


def logout(request):
    request.session.flush()
    return redirect("/")

def post_message(request):
    message = request.POST['message']
    user_id = request.session['id']

    user_message = Messages.objects.create(message=message, user=Users.objects.get(id=user_id))
    return redirect("/wall")


def post_comment(request):
    comment = request.POST['comment']
    message_id = request.POST['message_id']
    user_id = request.session['id']

    user_comment = Comments.objects.create(comment=comment, message=Messages.objects.get(id=message_id), user=Users.objects.get(id=user_id))
    return redirect("/wall")

def delete_message(request):
    message_id = request.POST['msg_id']
    Messages.objects.get(id=message_id).delete()
    return redirect("/wall")