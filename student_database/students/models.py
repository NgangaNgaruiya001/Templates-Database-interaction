from django.db import models

# Create your models here.
class Student(models.Model):
	programme = models.CharField(max_length=100, null=True)
	gender = models.CharField(max_length=100, null=True)
	enrollment_year = models.IntegerField(null=True)
	name = models.CharField(max_length=100, null=True)
	phone_number = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True)
	completion_year = models.IntegerField(null=True)

	def __str__(self):
		return self.name