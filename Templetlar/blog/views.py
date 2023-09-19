from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(reques):
    return HttpResponse("Hello, World!")


def salom_dunyo(request):
    return HttpResponse("Salmlar")
