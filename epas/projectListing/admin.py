from django.contrib import admin

from .models import (User, Student, Professor, CorporateSupervisor,
                     ProgramDirector, Post)


admin.site.register(Post)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(ProgramDirector)
admin.site.register(CorporateSupervisor)