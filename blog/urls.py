from django.urls import path,include
from . import views

urlpatterns = [
    path('create100/',views.create100),
]