from http.client import HTTPResponse
from django.shortcuts import render
from .models import Post
from .forms import CreateNewProject 

projectApplications = [
    {
        'professor': 'Daniel Amyot',
        'title': 'EPAS',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Accepted'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Denied'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_applied': 'February 3rd 2022',
        'status': 'Denied'
    },
]

myProjects = [
    {
        'course': 'CSI4900',
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'semester': 'Fall 2022',
        'status': 'Accepted'
    },
]

def index(request, id):
    ls = Post.objects.get(id=id)
    return render(request, 'projectListing/index.html', {'ls':ls})

def home(request):
    context = {
        'postedProject': Post.objects.all()
    }
    return render(request, 'projectListing/home.html', context)

def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

def myprojects(request):
    context = {
        'myProjects': myProjects
    }
    return render(request, 'projectListing/myprojects.html', context)

def applications(request):
    context = {
        'projectApplications': projectApplications
    }
    return render(request, 'projectListing/applications.html', context)

def projectapplication(request):
    return render(request, 'projectListing/projectapplication.html', {'title': 'Profile'})

def projectapply(request):
    return render(request, 'projectListing/projectapply.html', {'title': 'Profile'})

def addProject(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST)
        if form.is_valid():
            n = form.cleaned_data["title"]
            t = Post(title=n)
            t.save

        return HTTPResponse('/%i' %t.id)
    else:
        form = CreateNewProject()
    return render(request, 'projectListing/addProject.html', {'form': form})




