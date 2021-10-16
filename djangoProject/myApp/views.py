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
        result = json.loads(requests.get(text).text)
        for gist in result:
            newGist = models.Gist()
            newGist.files = []
            newGist.forks = []
            newGist.name = gist["description"]
            forks_link = gist["forks_url"]
            forks = json.loads(requests.get(forks_link).text)
            if len(forks) > 3:
                forks = forks[:3]
            for fork in forks:
                user = models.User()
                user.name = fork["owner"]["login"]
                user.photo = str(base64.b64encode(requests.get(fork["owner"]["avatar_url"]).content))[2:]
                user.photo = user.photo[:-1]
                newGist.forks.append(user)
            for file in gist["files"]:
                newFile = models.File()
                newFile.name = gist["files"][file]["filename"]
                newFile.filetype = gist["files"][file]["type"]
                newFile.content = gist["files"][file]["raw_url"]
                newGist.files.append(newFile)
            gists.append(newGist)
    return render(request, "home.html", {'gists': gists})


def getHome(request):
    gists = []
    return render(request, "home.html", {'gists': gists})
