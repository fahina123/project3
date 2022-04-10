from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hai")


def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')  


