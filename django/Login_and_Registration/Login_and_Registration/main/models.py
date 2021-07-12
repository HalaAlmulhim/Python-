from django.db import models
from django.core.exceptions import ValidationError
import re	


class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["first_name"] = "Registration First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["last_name"] = "Registration Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']) :    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8 :
            errors["password"] = "Registration Password should be in past date and show 8 characters"
        if len(postData['cpassword']) < 8:
            errors["confirm_password"] = "Registration Confirm Password should be at least 8 characters"
        return errors

class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RegistrationManager()

# reg1=Registration.objects.create(first_name="", last_name="", email="", password="", confirm_password="")