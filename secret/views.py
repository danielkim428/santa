from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
import random

def shuffle_list(some_list):
    randomized_list = some_list[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(some_list, randomized_list):
            if a == b:
                break
        else:
            return randomized_list

# Create your views here
from .models import *

def index(request):
    if request.user.is_authenticated:
        try:
            user = Profile.objects.get(user=request.user)
            context = {
                "group": Group.objects.get(name=user.groups.name),
                "user": user,
            }
            return render(request, "secret/index.html", context)
        except:
            return render(request, "secret/init.html")
    else:
        return render(request, "secret/index.html")

def init(request):
    return render(request, "secret/init.html")

def logout_view(request):
    logout(request)
    return render(request, "secret/login.html", {"message": "Logged out."})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'secret/login.html', {"message": "Invalid credentials."})
    else:
        return render(request, 'secret/login.html')

def mod(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('index'))
    context = {
        "user": request.user,
        "profiles": Group.objects.all(),
    }
    if request.method == 'POST':
        name = request.POST['group']
        group = Group.objects.get(name=name)
        try:
            group.start = 1

            list = []
            newList = []
            for profile in group.profile_set.all():
                list.append(profile.user)
                profile.mortal = None
                profile.save()
            newList = shuffle_list(list)

            i = 0
            for profile in group.profile_set.all():
                profile.mortal = newList[i]
                profile.save()
                i = i + 1

            group.save()
        except:
            context = {
                "user": request.user,
                "profiles": Group.objects.all(),
                "message": "Please try it again",
            }
            return render(request, 'secret/mod.html', context)
        return render(request, "secret/mod.html", context)
    else:
        return render(request, "secret/mod.html", context)
