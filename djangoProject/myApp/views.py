import json
from django.shortcuts import render
from . import models
import requests
import base64


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
            forks_link = gist["forks_url"]
            forks = json.loads(requests.get(forks_link).text)
            if len(forks)>3:
                forks = forks[:3]
            for fork in forks:
                u = models.User()
                u.name = fork["owner"]["login"]
                u.photo = str(base64.b64encode(requests.get(fork["owner"]["avatar_url"]).content))[2:]
                u.photo = u.photo[:-1]
                g.forks.append(u)
            for file in gist["files"]:
                f = models.File()
                f.name = gist["files"][file]["filename"]
                f.filetype = gist["files"][file]["type"]
                f.content = gist["files"][file]["raw_url"]
                g.files.append(f)
            gists.append(g)
    return render(request, "home.html", {'gists': gists})

def getHome(request):
    gists = []
    return render(request, "home.html", {'gists': gists})
