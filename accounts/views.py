# your_app/views.py

from django.http import JsonResponse
from .models import Department, Semester, Section,Course
from django.shortcuts import render

def student_form(request):
    courses = Course.objects.all()
    return render(request, 'student_form.html', {'courses': courses})


def load_departments(request):
    course_id = request.GET.get('course_id')
    departments = Department.objects.filter(course_id=course_id)
    return JsonResponse(list(departments.values('id', 'name')), safe=False)

def load_semesters(request):
    dept_id = request.GET.get('dept_id')
    semesters = Semester.objects.filter(department_id=dept_id)
    return JsonResponse(list(semesters.values('id', 'number')), safe=False)


def load_sections(request):
    sem_id = request.GET.get('sem_id')
    sections = Section.objects.filter(semester_id=sem_id)
    return JsonResponse(list(sections.values('id', 'name')), safe=False)