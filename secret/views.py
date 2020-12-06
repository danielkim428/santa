from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.tz import gettz
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
            try:
                angel = Profile.objects.get(mortal=request.user)
                context = {
                    "group": Group.objects.get(name=user.groups.name),
                    "user": user,
                    "angel": angel,
                }
                return render(request, "secret/index.html", context)
            except:
                context = {
                    "group": Group.objects.get(name=user.groups.name),
                    "user": user,
                }
                return render(request, "secret/index.html", context)
        except:
            return render(request, "secret/init.html")
    else:
        return render(request, "secret/index.html")

def mortal(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    try:
        user = Profile.objects.get(user=request.user)
        if (Group.objects.get(name=user.groups.name).start == 0):
            return HttpResponseRedirect(reverse('index'))
        angel = Profile.objects.get(mortal=request.user)
        mortal = Profile.objects.get(user=user.mortal)
        context = {
            "group": Group.objects.get(name=user.groups.name),
            "user": user,
            "angel": angel,
            "letter": Letter.objects.filter(mortal=request.user)
        }
        return render(request, "secret/mortal.html", context)
    except:
        return HttpResponseRedirect(reverse('init'))

def new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    try:
        user = Profile.objects.get(user=request.user)
        if (Group.objects.get(name=user.groups.name).start == 0):
            return HttpResponseRedirect(reverse('index'))
        mortal = Profile.objects.get(user=user.mortal)
        context = {
            "group": Group.objects.get(name=user.groups.name),
            "user": user,
            "mortal": mortal,
            "letter": Letter.objects.filter(angel=request.user)
        }
        if request.method == 'POST':
            try:
                date = datetime.now(tz=gettz('Asia/Kolkata'))
                content = request.POST['content']
                if not content:
                    context = {
                        "group": Group.objects.get(name=user.groups.name),
                        "user": user,
                        "mortal": mortal,
                        "letter": Letter.objects.filter(angel=request.user),
                        "message": "Please write something"
                    }
                    return render(request, "secret/new.html", context)
                if len(content) >= 3000:
                    context = {
                        "group": Group.objects.get(name=user.groups.name),
                        "user": user,
                        "mortal": mortal,
                        "letter": Letter.objects.filter(angel=request.user),
                        "message": "Too much"
                    }
                    return render(request, "secret/new.html", context)
                angel = request.user
                mortal = user.mortal
                new_letter = Letter(date=date, content=content, angel=angel, mortal=mortal)
                new_letter.save()
                return HttpResponseRedirect(reverse('new'))
            except:
                context = {
                    "group": Group.objects.get(name=user.groups.name),
                    "user": user,
                    "mortal": mortal,
                    "letter": Letter.objects.filter(angel=request.user),
                    "message": "Something went wrong"
                }
                return render(request, "secret/new.html", context)
        else:
            return render(request, "secret/new.html", context)
    except:
        return HttpResponseRedirect(reverse('init'))

def init(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    try:
        user = Profile.objects.get(user=request.user)
        context = {
            "group": Group.objects.get(name=user.groups.name),
            "user": user,
        }
        return HttpResponseRedirect(reverse('index'))
    except:
        if (request.user.email.split("@")[1] != "woodstock.ac.in"):
            logout(request)
            return render(request, 'secret/login.html', {"message": "Please sign in with your woodstock account."})
        if request.method == 'POST':
            try:
                code = request.POST['code']
                group = Group.objects.get(code=code)
            except:
                return render(request, "secret/init.html", {"message": "Wrong Code"})
            try:
                user = request.user
                description = request.POST['description']

                new_profile = Profile(user=user, description=description, groups=group)
                new_profile.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                return render(request, "secret/init.html", {"message": "Something went wrong"})
        else:
            return render(request, "secret/init.html")

def account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    try:
        user = Profile.objects.get(user=request.user)
        context = {
            "group": Group.objects.get(name=user.groups.name),
            "user": user,
        }
        if request.method == 'POST':
            description = request.POST['description']
            if len(description) >= 3000:
                context = {
                    "group": Group.objects.get(name=user.groups.name),
                    "user": user,
                    "message": "Too much",
                }
                return render(request, "secret/account.html", context)
            profile = Profile.objects.get(user=request.user)
            profile.description = description
            profile.save()
            return HttpResponseRedirect(reverse('account'))
        else:
            return render(request, "secret/account.html", context)
    except:
        return HttpResponseRedirect(reverse('init'))

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
