
# pip install django-multiselectfield

from django.db import models
from multiselectfield  import  MultiSelectField

class Enquiry(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.BigIntegerField(unique=True)

    course_choices = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('RestAPI', 'RestAPI'),
        ('MySQL', 'MySQL'),
    ]
    course = MultiSelectField(choices=course_choices)

    location_choices = [
        ('Hyderabad', 'Hyderabad'),
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai'),
        ('Chennai', 'Chennai'),
    ]
    location = MultiSelectField(choices=location_choices)

    start_date = models.DateField() # mm/dd/yyyy
    gender = models.CharField(max_length=10)



