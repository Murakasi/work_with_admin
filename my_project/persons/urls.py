from django.urls import path
from persons import views

urlpatterns = [
    path("", views.index, name="index"),
]
