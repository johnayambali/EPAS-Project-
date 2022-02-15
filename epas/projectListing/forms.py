from socket import fromshare
from django import forms

class CreateNewProject(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    check = forms.BooleanField()