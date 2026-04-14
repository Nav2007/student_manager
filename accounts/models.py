from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)



class Course(models.Model):
    name = models.CharField(max_length=100)   

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)   
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.course.name})"


class Semester(models.Model):
    number = models.IntegerField() 
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sem {self.number} - {self.department.name}"


class Section(models.Model):
    name = models.CharField(max_length=10) 
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Sem {self.semester.number}"
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#instead of writing CustomUser we specify it in the settings.py and use it using settings.authuser
    roll_number = models.CharField(max_length=20,unique=True)
    year=models.IntegerField()
    img = models.ImageField(upload_to='students/', blank=True, null=True)
    aadhaar_number = models.CharField(max_length=12,unique=True)
    date_of_birth = models.DateField()
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} (Roll: {self.roll_number})"

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20,unique=True)
    img = models.ImageField(upload_to='teachers/', blank=True, null=True)
    aadhaar_number = models.CharField(max_length=12,unique=True)

    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=100)

    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} (Emp: {self.employee_id})"
