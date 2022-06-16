
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_data, name='students'),
    path('create_student/', views.create_Student, name='create_student'),


]
	