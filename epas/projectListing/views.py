from django.shortcuts import render

postedProject = [
    {
        'professor': 'Daniel Amyot',
        'title': 'EPAS',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 3rd 2022',
        'num_students': '3'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 1st 2022',
        'num_students': '2-3'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 1st 2022',
        'num_students': '3'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 1st 2022',
        'num_students': '1'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 1st 2022',
        'num_students': '3'
    },
    {
        'professor': 'Amy Felty',
        'title': 'Software development',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam posuere convallis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas non leo at enim porttitor mattis sit amet elementum nisl. Suspendisse dictum ipsum eu erat faucibus vestibulum. Ut tincidunt sit amet justo nec tempus. Fusce at interdum sem, sit amet volutpat odio. Nunc dignissim lacus eu est aliquet, et tempor purus accumsan. Proin finibus porta commodo. Ut congue sodales massa at malesuada. Mauris a ligula nec risus tristique volutpat. Etiam sed nisi interdum, euismod arcu nec, pellentesque nisi. Suspendisse ac malesuada diam. Quisque a sagittis ex, eget eleifend arcu. Phasellus a arcu odio. Proin cursus, lacus et cursus gravida, dui libero tincidunt est, ac varius quam tortor et nulla.',
        'date_posted': 'February 1st 2022',
        'num_students': '2'
    },
]

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

def home(request):
    context = {
        'postedProject': postedProject
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

