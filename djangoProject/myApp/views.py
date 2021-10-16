import json
import time

from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import requests


def getHomeWithUser(request):
    try:
        username = request.GET["username"]
    except(Exception):
        username = ""
    gists = []
    if username != "":
        text = 'https://api.github.com/users/' + username + '/gists'
        r = json.loads(requests.get(text).text)
        print(r)
    return render(request, "home.html", {'gists': gists})

def getHome(request):
    gists = []
    return render(request, "home.html", {'gists': gists})
