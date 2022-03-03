from django.urls import path
from django.views import View
from .views import home

urlpatterns = [
    path('', home, name='home')
]