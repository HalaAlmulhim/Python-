from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt



def index(request):
    return render(request, "index.html")


def success_page(request):
    return render(request, "welcome.html")



def registration(request):
    errors = Registration.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        finame = request.POST['fname']
        laname = request.POST['lname']
        email = request.POST['email']
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        cpassword = bcrypt.hashpw(request.POST['cpassword'].encode(), bcrypt.gensalt()).decode()
        user = Registration.objects.create(first_name= finame , last_name=laname , email=email , password= password , confirm_password=cpassword )
        request.session['frist_name']= user.first_name
        request.session['user_id']= user.id
        return redirect("/success")


def login(request):
    this_user = request.POST['email']
    user_email = Registration.objects.filter(email=this_user)
    user_email = Registration.objects.filter(email=request.POST['email'])
    if user_email:
        this_user_logged = user_email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), this_user_logged.password.encode()):
            request.session['frist_name']= this_user_logged.first_name
            request.session['user_id']= this_user_logged.id
            print("failed email")
            print("failed password")
            return redirect("/")
        else:
            request.session['frist_name']= this_user_logged.first_name
            request.session['last_name']= this_user_logged.last_name
            # request.session['user_id']= this_user_logged.id
            # print("password match")
            return redirect("/success")



   
def logout(request):
    request.session.flush()
    return redirect("/")




