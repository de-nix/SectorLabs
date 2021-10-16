import json
import time

from django.http import HttpResponse
from django.shortcuts import render

from . import models
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
        for gist in r:
            g = models.Gist()
            g.files = []
            g.forks = []
            g.name = gist["description"]
            for file in gist["files"]:
                f = models.File()
                f.name = gist["files"][file]["filename"]
                f.filetype = gist["files"][file]["type"]
                f.content = gist["files"][file]["raw_url"]
                g.files.append(f)
            gists.append(g)
            print(g.name)

    return render(request, "home.html", {'gists': gists})

def getHome(request):
    gists = []
    return render(request, "home.html", {'gists': gists})
