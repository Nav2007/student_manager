from django.urls import path
from . import views

urlpatterns = [
    path('student-form/', views.student_form, name='student_form'),
    path('ajax/load-departments/', views.load_departments, name='load_departments'),
    path('ajax/load-semesters/', views.load_semesters),
    path('ajax/load-sections/', views.load_sections),
]