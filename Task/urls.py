from django.urls import path
from . import views

app_name="Task"
urlpatterns = [
    path("", views.index, name="Index"),
    path("add", views.add, name="add")
]
