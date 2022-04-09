from gc import get_objects
from django.shortcuts import render
from .models import Post
from .models import Application
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect


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

profMyProjects = [
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
        'postedProject': Post.objects.all()
    }
    return render(request, 'projectListing/home.html', context)

def homeDirector(request):
    context = {
        'postedProject': Post.objects.all()
    }
    return render(request, 'projectListing/home_director.html', context)



def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

def myprojects(request):
    context = {
        'myProjects': myProjects
    }
    return render(request, 'projectListing/myprojects.html', context)

def applications(request):
    context = {
        'appliedProject': Application.objects.all()
    }
    return render(request, 'projectListing/applications.html', context)

def projectapplication(request):
    return render(request, 'projectListing/projectapplication.html', {'title': 'Profile'})

def projectapply(request):
    return render(request, 'projectListing/projectapply.html', {'title': 'Profile'})


def profprofile(request):
    return render(request, 'projectListing/prof_profile.html', {'title': 'Profile'})

def profmyprojects(request):
    return render(request, 'projectListing/prof_myprojects.html', {'title': 'Profile'})

def profmyactiveprojects(request):
    context = {
        'postedProject': Post.objects.all()
    }
    return render(request, 'projectListing/prof_myactiveprojects.html', context)

def profprojectapplications(request):
    context = {
        'appliedProject': Application.objects.all()
    }
    return render(request, 'projectListing/prof_projectapplications.html', context)

def createapplication(request):
    if request.method=='POST':
        if request.POST.get('student') and request.POST.get('project') and request.POST.get('id') and request.POST.get('appDetails'):
            post=Application()
            post.student = request.POST.get('student')
            post.project = request.POST.get('project')
            post.projectID = request.POST.get('projectID')
            post.appDetails = request.POST.get('appDetails')  
            post.save()

            return render(request, 'projectListing/home.html')
        else:
            return render(request, 'projectListing/home.html' )

def createapplication2(request):
    if request.method=='POST':
        if request.POST.get('student') and request.POST.get('project') and request.POST.get('id') and request.POST.get('appDetails'):
            post=Application()
            post.student = request.POST.get('student')
            post.project = request.POST.get('project')
            post.projectID = request.POST.get('projectID')
            post.appDetails = request.POST.get('appDetails')  
            post.save()

            return render(request, 'projectListing/home.html')
        else:
            return render(request, 'projectListing/home.html' )


 
class PostListView(ListView):
    model = Post
    template_name = 'projectListing/home.html'
    context_object_name = 'postedProject'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'date_posted', 'desiredNumStudents', 'maxNumStudents', 'minTermLength', 'maxTermLength', 'relatedProgram', 'course', 'active']


    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'date_posted', 'desiredNumStudents', 'maxNumStudents', 'minTermLength', 'maxTermLength', 'relatedProgram', 'course', 'active']

    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor or self.request.user.type == "PROGRAM_DIRECTOR":
            return True
        return False

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor:
            return True
        return False


class ApplicationListView(ListView):
    model = Application
    template_name = 'projectListing/applications.html'
    context_object_name = 'appliedProject'
    ordering = ['-date_posted']

class ApplicationDetailView(DetailView):
    model = Application
    

class ApplicationCreateView(CreateView):
    model = Application
    success_url = '/'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class ApplicationUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['status']

    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor:
            return True
        return False

class ApplicationDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.student:
            return True
        return False

class UpdateApprovalView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['isApproved']

    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor or self.request.user.type == "PROGRAM_DIRECTOR":
            return True
        return False



