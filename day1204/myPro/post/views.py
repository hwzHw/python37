from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reuester):
    return HttpResponse("<h1>Post</h1>")
