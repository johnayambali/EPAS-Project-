from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'postedProject': Post.objects.all()
    }
    return render(request, 'projectListing/home.html', context)

def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

def myprojects(request):
    return render(request, 'projectListing/myprojects.html', {'title': 'My Projects'})

def applications(request):
    return render(request, 'projectListing/applications.html', {'title' : 'Applications'})

