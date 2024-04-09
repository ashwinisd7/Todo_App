from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a view function for the root path
    
]
