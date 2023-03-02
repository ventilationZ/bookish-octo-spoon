from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student


def edit_page(request):
    return render(request, "edit.html")


def index_page(request):
    return render(request, "index.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Student(name=name,
                        email=email,
                        age=age,
                        gender=gender)
        query.save()

    return render(request, 'index.html')
