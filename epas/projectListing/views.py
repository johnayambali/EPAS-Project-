from email.mime import application
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
    if request.user.is_anonymous:
        context = {
            'postedProject': Post.objects.filter(student=None),
            'appliedProject': Application.objects.all()
        }
        return render(request, 'projectListing/home.html', context)

    if request.user.type == "STUDENT":
        application = Application.objects.filter(student=request.user)
        projects = Post.objects.filter(student=None)
        applied = []
        notApplied = []
        

        for pro in projects:
            flag = False
            for app in application:
                if pro.id == app.project.id:
                    flag = True
            if flag == True:
                applied.append(app)
            if flag == False:
                notApplied.append(pro)

        context = {
            'application': applied,
            'postedProject': notApplied,
            'appliedProject': Application.objects.all()
        }
        return render(request, 'projectListing/home.html', context)

    else:
        context = {
            'postedProject': Post.objects.filter(student=None),
            'appliedProject': Application.objects.all()
        }
        return render(request, 'projectListing/home.html', context)

def homeDirector(request):
    applications = Application.objects.filter(offerStatus='a', applicationStatus='a', project__student=None)
    context = {
        'postedProject': applications
    }
    return render(request, 'projectListing/home_director.html', context)



def profile(request):
    return render(request, 'projectListing/profile.html', {'title': 'Profile'})

def myprojects(request):
    application = Post.objects.filter(student=request.user, completed=False)

    context = {
        'appliedProject': application
    }
    return render(request, 'projectListing/myprojects.html', context)

def applications(request):
    application = Application.objects.filter(student=request.user, project__student=None)
   
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
    applications = Application.objects.filter(project__professor=request.user, student=None)
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
    fields = ['title', 'description', 'desiredNumStudents', 'maxNumStudents', 'minTermLength', 'maxTermLength', 'course']


    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'desiredNumStudents', 'maxNumStudents', 'minTermLength', 'maxTermLength', 'course']

    def form_valid(self, form):
        if self.request.user.type == "PROGRAM_DIRECTOR":
            pass
        else:
            form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor or self.request.user.type == "PROGRAM_DIRECTOR":
            return True
        return False

class PostUpdateView2(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['isApproved']
    success_url = '/'

    def form_valid(self, form):
        application = Application.objects.get(project=self.get_object(), offerStatus='a', applicationStatus='a')
        if self.request.user.type == "PROGRAM_DIRECTOR":
            form.instance.student = application.student
            application.isApproved = True
            application.save()
        else:
            form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor or self.request.user.type == "PROGRAM_DIRECTOR":
            return True
        return False

class PostUpdateView3(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['completed']
    success_url = '/'

    def form_valid(self, form):
        form.instance.professor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.professor:
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
    model = Application
    fields = ['appDetails']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.student:
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