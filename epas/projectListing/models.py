<<<<<<< HEAD
=======
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
>>>>>>> e9c956d046dd5f6322231ea4b0c9e29fe354f988
