from django.shortcuts import render

postedProject = [
    {
        'professor': 'Daniel Amyot',
        'title': 'epas',
        'descrption': 'description of the project',
        'date_posted': 'Febuary 3rd 2022'
    },
    {
        'professor': 'Amy Felty',
        'title': 'software develpment',
        'descrption': 'description of the project',
        'date_posted': 'Febuary 1st 2022'
    },
]


def home(request):
    context = {
        'postedProject': postedProject
    }
    return render(request, 'projectListing/home.html', context)

def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

