from __future__ import unicode_literals
from django.db import models
from importlib import import_module

# Create your models here.
class Courses(models.Model):
	courseId = models.AutoField(primary_key=True)
	course_code = models.CharField(max_length=5, blank=False, null=False, default='xxxxx', unique=True)
	course_name = models.CharField(max_length=30, blank=True, null=True)
	lab_included = models.BooleanField()
	def __str__(self):
		return self.courseId

class Timings(models.Model):
	day = models.CharField(max_length=9, default='Sunday')
	start_time = models.TimeField()
	end_time = models.TimeField()

class CourseSlots(models.Model):
	course_slot_id = models.AutoField(primary_key=True)
	timing_list = models.ManyToManyField(Timings)
	def __str__(self):
		return self.course_slot_id		

class Users(models.Model):
	userId = models.AutoField(primary_key=True)
	userName = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30)
	userType = models.CharField(max_length=30)
	def __str__(self):
		return self.userId

class Faculties(models.Model):
	facId = models.AutoField(primary_key=True)
	userId = models.OneToOneField('Users', models.CASCADE,db_index=False)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	contact = models.CharField(max_length=15, unique=True)
	emailId = models.EmailField(unique=True, max_length=100)
	def __str__(self):
		return self.facId

class Students(models.Model):
	userId = models.OneToOneField('Users', models.CASCADE, blank=True, null=True)
	entryNo = models.CharField(max_length=10, unique=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	year = models.CharField(max_length=10)
	degree = models.CharField(max_length=30)
	contact = models.CharField(max_length=15, unique=True)
	emailId = models.EmailField(unique=True, max_length=100)
	def __str__(self):
		return self.entryNo

class TeachingAssistant(models.Model):
	userId = models.OneToOneField('Users', models.CASCADE, blank=True, null=True)
	course_offered = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True) 
	contact = models.CharField(max_length=15, unique=True)
	emailId = models.EmailField(unique=True, max_length=100)
	entryNo = models.CharField(max_length=10, unique=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)

class CourseOffered(models.Model):
	course_offered_id = models.AutoField(primary_key=True)
	facId = models.ForeignKey('Faculties', on_delete=models.CASCADE, blank=True, null=True)
	courseId = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True)
	course_year = models.CharField(max_length=4)
	course_sem = models.BooleanField()
	course_slot = models.ForeignKey('Timings', models.CASCADE, related_name='+')	

class StudentCourseReg(models.Model):
	course_offered = models.ForeignKey('CourseOffered', models.CASCADE, blank=True, null=True)
	studentId = models.ForeignKey('Students', models.CASCADE, blank=True, null=True)


class AttendanceRecord(models.Model):

	class Meta(object):
		unique_together = (("date", "studentReg"), )

	date = models.DateField(db_index=True)
	studentReg = models.ForeignKey('StudentCourseReg', models.CASCADE, blank=True, null=True)
	value = models.BooleanField(default=True)
