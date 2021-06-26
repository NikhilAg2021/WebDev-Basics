from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def nikhil(request):
    return HttpResponse("Hi there, Nikhil!!!")

def greet(request, name):
    return HttpResponse(f"Hello, {name} !")

def greet_page(request,name):
    return render(request, "Hello/greet_page.html", {
        "name": name.capitalize(),
    })

                                  