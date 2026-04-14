from django.contrib import admin
from .models import (
    CustomUser, Student, Teacher,
    Course, Department, Semester, Section
)

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Teacher)

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Section)