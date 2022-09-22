from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Task

# Create your views here.
def index(request):
    title = "Welcome to Django Course"
    return render(request, "index.html", {
        "title": title
    })

def about(request):
    username = "Fazt"
    return render(request, "about.html", {
        "username": username
    })


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)



def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {
        "projects": projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {
        "tasks": tasks
    })