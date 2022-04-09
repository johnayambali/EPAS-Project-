from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'date_posted', 'professor', 'desiredNumStudents', 'maxNumStudents', 'minTermLength', 'maxTermLength', 'relatedProgram', 'course', 'active',]

