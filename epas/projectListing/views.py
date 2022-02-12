from django.shortcuts import render

postedProject = [
    {
        'professor': 'Daniel Amyot',
        'title': 'epas',
        'description': 'description of the project',
        'date_posted': 'Febuary 3rd 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software develpment',
        'description': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
]

projectApplications = [
    {
        'professor': 'Daniel Amyot',
        'title': 'epas',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Accepted'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software develpment',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Denied'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Pending'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software development',
        'description': 'description of the project',
        'date_applied': 'Febuary 3rd 2022',
        'status': 'Denied'
    },
]

def home(request):
    context = {
        'postedProject': postedProject
    }
    return render(request, 'projectListing/home.html', context)

def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

def myprojects(request):
    return render(request, 'projectListing/myprojects.html', {'title': 'My Projects'})

def applications(request):
    context = {
        'projectApplications': projectApplications
    }
    return render(request, 'projectListing/applications.html', context)

