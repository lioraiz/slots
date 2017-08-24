import json

from django.contrib import auth
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf

from .models import Funds
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm



def game(request):
    activeuser = request.user
    userfunds = Funds.objects.get(player=activeuser)
    if request.method == "POST":
        context = {}
        gameresult = request.POST.get('result')
        print(userfunds.player)
        if gameresult == 'lose':
            userfunds.amount -= 5
            context["userfund"] = userfunds.amount
            context["restart"] = ""
            userfunds.save()
        else:
            userfunds.amount += 25
            context["userfund"] = userfunds.amount
            context["restart"] = ""
            userfunds.save()

        if userfunds.amount <= 0:
            context["restart"] = "its a fake game so keep going on!"
            userfunds.amount = 100
            userfunds.save()




        return HttpResponse(json.dumps(context))


    else:

        return render(request, 'onlineslots/game.html', {"userfunds":userfunds})

def UserFormView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            funds = Funds(player=newuser)
            funds.save()
            newuser = authenticate(request, username=form.cleaned_data["username"],
                                   password=form.cleaned_data["password1"])
            login(request, newuser)
            return HttpResponseRedirect("/game")
    else:
        form = UserForm()
        return render(request, "onlineslots/registration_form.html", {"form":form})


def login_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("onlineslots/index.html", c)


def auth_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect("/game/")
    else:
        return HttpResponseRedirect("/invalid_login/")


def invalid_login(request):
    return render_to_response("onlineslots/invalid_login.html")


def logout(request):
    auth.logout(request)
    return render_to_response("onlineslots/logged_out.html")


