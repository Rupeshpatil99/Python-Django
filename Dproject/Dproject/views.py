from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse("Hello, World!. You are at the django home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is the about page.")

def  contact(request):
    return HttpResponse("This is the contact page.")