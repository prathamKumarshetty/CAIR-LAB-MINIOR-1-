from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def AIML(request):
    return render(request,"AIML.html")
def CLOUD(request):
    return render(request,"CLOUD.html")
def RU(request):
    return render(request,"RU.html")
def OTHER(request):
    return render(request,"OTHER.html")
def HPC(request):
    return render(request,"HPC.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Check if all required fields are filled
        if name and email and phone and desc:
            # Create and save the Contact object
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your Message Has Been Sent.")
        else:
            messages.success(request, "Your Message Has  not been Been Sent.")

        
    
    return render(request, "contact.html")
