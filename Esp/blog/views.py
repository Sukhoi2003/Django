from django.shortcuts import render
# from django.views import View
from django.http import HttpResponse
from .models import Post

# Create your views here.
# class SimplePost(View):
#     def get(self, request):#get bolganda
#         posts = Post.objects.all()
#         post:Post
#         for post in posts:
#             print(f"{post.title} --> {post.body} --> {post.update}")
#         return HttpResponse("Terminalga qara...")
#     def post():#post bolganda
#         pass


def hello_world(request):
    print(request.method)
    print("+"*8, request, 8*"+")
    return HttpResponse('Hello, World!!!')

def first(request):
    print("+"*8, request, 8*"+")
    return HttpResponse('Birinchi ishladi')

def info(request):
    posts = Post.objects.all()
    post:Post
    for post in posts:
        print(f"{post.title} --> {post.body} --> {post.update}")
    return render(request, "test.html", {"posts" : posts})