from django.db import models
import re, datetime
import bcrypt
# Create your models here.

class UsersManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        ### Name VALIDATION ######
        if len(postData['fname']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"

        if len(postData['lname']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        
        ### Email VALIDATION ######
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Please enter a valid email address!"
        elif len(Users.objects.filter(email=postData['email'])) > 0:
            errors['used'] = "Email address is already in use"

        ### DATE VALIDATION ######
        if len(postData['date']) < 1:
            errors['date'] = "Date should not be empty"
        elif postData['date']:
            post_date = datetime.datetime.strptime(postData['date'], "%Y-%m-%d")
            if datetime.datetime.today() < post_date:
                errors['date_grater'] = "Date must be in the past"

        ### PASSWORDS VALIDATION ######
        if len(postData['password']) < 8:           
            errors['password'] = "Password should be at least 8 characters"

        if postData['password'] != postData['conf_pass']:
            errors['mismatch'] = "Passwords should match"

        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):            
            errors['login_email'] = "Please enter a valid email address!"

        if len(Users.objects.filter(email = postData['email'])) == 0:
            errors['email'] = "Email or password is incorrect"
        else:
            user = Users.objects.filter(email = postData['email'])
            user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['email'] = "Email or password is incorrect"

        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsersManager()

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Users, related_name="message", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Users, related_name="comment", on_delete = models.CASCADE)
    message = models.ForeignKey(Messages, related_name="comment", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)