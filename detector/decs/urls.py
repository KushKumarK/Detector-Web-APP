from django.urls import path
from decs import views

urlpatterns = [
    path("", views.home, name="home"),
]