from django.shortcuts import render,HttpResponse

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
    return render(request,"contact.html")

