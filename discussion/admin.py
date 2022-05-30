from django.contrib import admin

# Register your models here.

from .models import StudentDiscussion, FacultyDiscussion

admin.site.register(StudentDiscussion)
admin.site.register(FacultyDiscussion)
