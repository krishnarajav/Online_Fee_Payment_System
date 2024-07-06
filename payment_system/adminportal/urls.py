from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.addStudent, name='addStudent'),
    path('getCourse/', views.course, name='course'),
    path('studentData/', views.studentDetails, name='studentDetails'),
]
