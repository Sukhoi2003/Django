from django.contrib import admin
from django.urls import path
from .views import hello_world, salom_dunyo


urlpatterns = [
    path('', hello_world),
    path('salom', salom_dunyo)
]
 