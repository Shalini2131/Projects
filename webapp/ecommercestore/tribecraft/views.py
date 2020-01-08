from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home_page(request):
#     return HttpResponse("<h1 style='text-align : centre;'>Welcome to Tribe Crafts</h1>")
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'sign.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')