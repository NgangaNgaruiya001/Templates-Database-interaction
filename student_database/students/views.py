from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from .forms import StudentForm


# Create your views here.

def home(request):

	students = Student.objects.all()

	total_students = students.count()

	total_courses = Student.objects.values('programme').distinct().count()

	context = {'total_students' : total_students, 'total_courses': total_courses}


	return render(request, 'students/dashboard.html', context )

def student_data(request):

	students = Student.objects.all()

	return render(request, 'students/students.html', {'students' : students})

def create_Student (request):

	form = StudentForm
	if request.method == 'POST':
		# print('printing POST', request.POST)
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form' : form}

	return render(request, 'students/student_form.html', context)
