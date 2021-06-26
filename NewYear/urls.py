from django.urls import path

from . import views

app_name="NewYear"
urlpatterns=[
    path("", views.index,name="Index")
    ]