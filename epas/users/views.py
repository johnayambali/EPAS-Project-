from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from  users.forms import RegistrationForm

# Create your views here.

#Registration
#Creates the form
def registration_view(request):
    #context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            type = form.cleaned_data.get('type')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
        '''else:
            context['registration_form'] = form'''

    else:
        form = RegistrationForm()
        #context['registration_form'] = form
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')