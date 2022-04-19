from gc import get_objects
from socket import AF_APPLETALK
from django.shortcuts import render
from .models import Post, Professor
from .models import Application
from .models import User
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect


def home(request):
    
    application = Application.objects.filter(student=request.user)
    context = {
        'application': application,
        'postedProject': Post.objects.all(),
        'appliedProject': Application.objects.all()
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
    application = Application.objects.filter(student=request.user)
    context = {
        'appliedProject': application
    }
    return render(request, 'projectListing/myprojects.html', context)

def applications(request):
    application = Application.objects.filter(student=request.user)
    context = {
        'appliedProject': application
    }
    return render(request, 'projectListing/applications.html', context)


def profmyactiveprojects(request):
    projects = Post.objects.filter(professor=request.user)
    context = {
        'postedProject': projects
    }
    return render(request, 'projectListing/prof_myactiveprojects.html', context)

def profprojectapplications(request):
    applications = Application.objects.filter(project__professor=request.user)
    context = {
        'appliedProject': applications
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
    fields = ['appDetails']
    
    def form_valid(self, form):
        form.instance.student = self.request.user
        form.instance.project = Post.objects.get(id=self.kwargs['pk'])
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
    model = Application
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
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor or self.request.user.type == "PROGRAM_DIRECTOR":
            return True
        return False



class UpdateStatusView(UserPassesTestMixin, UpdateView):
    model = Application
    fields = ['applicationStatus']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.type == "PROFESSOR":
            return True
        return False

class UpdateOfferView(UserPassesTestMixin, UpdateView):
    model = Application
    fields = ['offerStatus']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.type == "STUDENT":
            return True
        return False