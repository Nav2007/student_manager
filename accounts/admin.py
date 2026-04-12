from django.contrib import admin
from .models import CustomUser, Student, Teacher
# What is “registering models with admin”?
# Making your models visible and manageable inside Django’s admin panel.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Teacher)