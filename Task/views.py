from django import forms
from django.shortcuts import render

tasks=["foo","var","baz"]

class NewForm(forms.form):
    task= forms.CharField(label="Enter New Task ->")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
# Create your views here.
def index(request):
    return render(request, "Task/index.html",{
        "tasks": tasks #tasks is the variable accessed by django whereas tasks holds the value 

    })
def add(request):
    return render (request, "Task/add.html", {
        "form": NewForm()
    })