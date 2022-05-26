from django.shortcuts import render
from Enquiry_App.models import Enquiry
from Enquiry_App.forms import EnquiryForm
from django.http import HttpResponse

def EnquiryView(request):
    if request.method=='POST':
        form = EnquiryForm(request.POST)
        print(request.POST)
        print()
        print(form)

        if form.is_valid():
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')

            course = form.cleaned_data.get('course')
            location = form.cleaned_data.get('location')
            start_date = form.cleaned_data.get('start_date')
            gender = form.cleaned_data.get('gender')
            #course = request.POST.get('course')
            #location = request.POST.get('location')

            Enquiry.objects.create(
                firstname=firstname,lastname=lastname,email=email,mobile=mobile,
                course=course, location=location, start_date=start_date,gender=gender
            )
            return HttpResponse("Form data saved into database")
        else:
            return HttpResponse("form data not saved into database")

    else:
        form = EnquiryForm()
        context = {
            "form" : form
        }
        return render(request, 'enquiry_form.html', context)