from django.shortcuts import render

# Create your views here.
#own created file
from django.http import HttpResponse




people = [
                    {"name":"shah", "age":22},
                    {"name":"shah1", "age":23},
                    {"name":"shah2", "age":17},
                    {"name":"shah3", "age":25},
                    {"name":"shah4", "age":26},

     ]



def home(request):

     return render(request, "index.html", context= {'people':people})

def conact(request):

     return render(request, "contact.html", context= {'people':people})

def about(request):

     return render(request, "about.html", context= {'people':people})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> This is success page</h1>")