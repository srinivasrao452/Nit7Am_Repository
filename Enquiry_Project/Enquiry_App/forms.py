from django import forms
from multiselectfield  import MultiSelectFormField
from django.forms.widgets import SelectDateWidget

class EnquiryForm(forms.Form):
    firstname = forms.CharField(
        label="Enter your firstname",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "your firstname",
            }
        )
    )
    lastname = forms.CharField(
        label="Enter your lastname",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "your lastname",
            }
        )
    )
    email = forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "your email",
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "your mobile",
            }
        )
    )

    course_choices = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('RestAPI', 'RestAPI'),
        ('MySQL', 'MySQL'),
    ]
    course = MultiSelectFormField(
        choices=course_choices,
        label="Select required courses"
    )

    location_choices = [
        ('Hyderabad', 'Hyderabad'),
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai'),
        ('Chennai', 'Chennai'),
    ]
    location = MultiSelectFormField(
        choices=location_choices,
        label="Select required locations"
    )

    y = range(1980, 2022)
    start_date = forms.DateField(
        widget=SelectDateWidget(years=y),
        label="Select required Date"
    )

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect(),
        label="Select your Gender"
    )


