from django.shortcuts import render

#own created file
from django.http import HttpResponse

def index(request):
     return HttpResponse("hello ghfghyf")

def about(request):
     return HttpResponse("hello about")

