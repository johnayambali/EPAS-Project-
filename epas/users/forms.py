from django import forms
from django.contrib.auth.forms import UserCreationForm
from projectListing.models import User

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length =60, help_text="Required. Add valid email")

    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "type", "password1", "password2")