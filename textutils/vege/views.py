from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required (login_url="/login/")
def recipes (request):

    if request.method == "POST":
        data = request.POST

        rimg = request.FILES.get('rimg')
        rname = data.get("rname")
        rdesc = data.get("rdesc")
        print(rname)
        print(rdesc)
        print(rimg)
   
        Recipe.objects.create(
            rimg = rimg,
            rdesc = rdesc,
            rname = rname,
            )
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(rname__icontains = request.GET.get('search'))

    context = {"recipes": queryset}
   
    return render (request, 'recipes.html' , context)

@login_required (login_url="/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()

    return redirect('/recipes/')

@login_required (login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data  = request.POST
        rimg = request.FILES.get('rmg')
        rname = data.get('rname')
        rdesc = data.get('rdesc')

        queryset.rname = rname
        queryset.rdesc = rdesc

        if rimg:
            queryset.rimg = rimg

        queryset.save()
        return redirect('/recipes/')

    context = {"recipe": queryset}

    return render(request, 'update_recipe.html' , context)


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username = username).exists():
             messages.error(request, "Invalid username")
             return redirect('/login/')
        user = authenticate(username = username , password = password)
        if user == None:
            messages.error(request, "Invalid credentials")
            return redirect('/login/')

        else:
            login(request, user)
            return redirect('/recipes/')

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/register/')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            user.save()
            messages.success(request, "Account created successfully")
            return redirect('/register/')

    return render(request, "register.html")

    