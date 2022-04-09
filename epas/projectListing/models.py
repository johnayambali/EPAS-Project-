from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse


class User(AbstractUser):
    class Types(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        PROFESSOR = 'PROFESSOR', 'Professor'
        CORPORATE_SUPERVISOR = 'CORPORATE_SUPERVISOR', 'Corporate Supervisor'
        PROGRAM_DIRECTOR = 'PROGRAM_DIRECTOR', 'Program Director'

    #fields
    type = models.CharField(max_length=50, choices=Types.choices, default=Types.STUDENT)
  

    def __str__(self):
        return self.username


#ProxyModels for the different types of users. It inherits User class
# UserManager classes manage queries for the different type of users

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.STUDENT)


class Student(User):
    objects = StudentManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)


class ProfessorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.PROFESSOR)


class Professor(User):
    objects = ProfessorManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PROFESSOR
        return super().save(*args, **kwargs)

    



class CorporateManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.CORPORATE_SUPERVISOR)


class CorporateSupervisor(User):
    objects = CorporateManager()
    class Meta:
        proxy = True

    @property
    def more(self):
        return self.corporatesupervisormore

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CORPORATE_SUPERVISOR
        return super().save(*args, **kwargs)

#logs company_name
class CorporateSupervisorMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)


class DirectorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.PROGRAM_DIRECTOR)


class ProgramDirector(User):
    objects = DirectorManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PROGRAM_DIRECTOR
        return super().save(*args, **kwargs)



#I added new fields to post to reflect ER & Added Application and MyDocuments Tables


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    desiredNumStudents = models.IntegerField()
    maxNumStudents = models.IntegerField()
    minTermLength = models.IntegerField()
    maxTermLength = models.IntegerField()
    relatedProgram = models.CharField(max_length=100)
    course = models.CharField(max_length=100, default="null")
    active = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

class Application(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Post, on_delete=models.CASCADE)
    projectID = models.IntegerField(default=-1)
    appDetails = models.TextField()
    def __str__(self):
        return f'Application from {self.student}'

    def get_absolute_url(self):
        return reverse("application-detail", kwargs={"pk": self.project.pk})


class MyDocuments(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    resumeFile = models.FileField()
    transcriptFile = models.FileField()
    linkedinURl = models.URLField()

    def __str__(self):
        return f'Documents from {self.student}'





