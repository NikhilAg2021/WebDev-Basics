
from django.urls import path

from Hello import views #'.' refers to current directory-Hello

app_name="Hello"
urlpatterns=[
        path("<str:name>", views.greet_page, name="Greet"),
        path("", views.index , name="Index") , #1st argument-No additional argument;2nd argument-what view should be visible when this url is visited
        path("nikhil", views.nikhil, name="Nikhil")
]
