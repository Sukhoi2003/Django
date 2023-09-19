from django.contrib import admin
from django.urls import path
from .views import hello_world, first, info

urlpatterns = [
    path('', hello_world),
    path('birinchi/', first),
    path('postlar/', info),
]
