# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

# from django.db import models

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from importlib import import_module
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Courses(models.Model):
	course_code = models.CharField(max_length=5, blank=False, null=False, default='xxxxx')
	course_name = models.CharField(max_length=30, blank=True, null=True)
	lab_included = models.BooleanField()
	def __str__(self):
		return str(self.courseId)

class Timings(models.Model):
	day = models.CharField(max_length=9, default='Sunday')
	start_time = models.TimeField()
	end_time = models.TimeField()

class CourseSlots(models.Model):
	timing_list = models.ManyToManyField(Timings)
	def __str__(self):
		return str(self.course_slot_id)
class ProfileManager(models.Manager):

	def create(self,userType,user,**kwargs):
		# print("2",**kwargs)
		profile = Profile(
			user=user,
			userType=userType,
		)
		profile.save()
		return user

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	userType = models.CharField(max_length=30)
	objects = ProfileManager()

	def __str__(self): 
		return self.user.username

# Signals to do some operations after Database Updates JUST like SQL triggers.
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)
# 	instance.profile.save()

# class BaseManager(models.Manager):
# 	def __init__(self,modelClass):
# 		super(BaseManager, self).__init__()
# 		self.userType=None
# 		self.modelClass=modelClass

# 	def create(self,**kwargs):
# 		user=kwargs['user']
# 		profile = Profile(
# 			user=user,
# 			# userType=userType,
# 			userType=self.userType,
# 		)
# 		profile.save()
# 		faculty = self.modelClass(**kwargs)
# 		faculty.save()
# 		return faculty

class FacultiesManager(models.Manager):
	def __init__(self):
		super(FacultiesManager, self).__init__()
		self.userType="Faculty"

	def create(self,**kwargs):
		user=kwargs['user']
		profile = Profile(
			user=user,
			# userType=userType,
			userType=self.userType,
		)
		profile.save()
		faculty = Faculties(**kwargs)
		faculty.save()
		return faculty

class StudentsManager(models.Manager):
	def __init__(self):
		super(StudentsManager, self).__init__()
		self.userType="Student"
	def create(self,**kwargs):
		user=kwargs['user']
		profile = Profile(
			user=user,
			# userType=userType,
			userType=self.userType,
		)
		profile.save()
		faculty = Students(**kwargs)
		faculty.save()
		return faculty

class Faculties(models.Model):
	user = models.OneToOneField(User, models.CASCADE,db_index=False)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	contact = models.CharField(unique=True, max_length=100)
	emailId = models.CharField( max_length=100)
	objects = FacultiesManager()
	def __str__(self):
		return str(self.facId)

class Students(models.Model):
	user = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	entryNo = models.CharField(max_length=10, unique=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	year = models.CharField(max_length=10)
	degree = models.CharField(max_length=30)
	contact = models.CharField(unique=True, max_length=100)
	emailId = models.CharField( max_length=100)
	courses = models.ManyToManyField('CourseOffered', through='StudentCourseReg', related_name='students')
	def __str__(self):
		return self.entryNo


class TeachingAssistant(models.Model):
	user = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	course_offered = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True) 
	contact = models.CharField(max_length=15, unique=True)
	emailId = models.CharField( max_length=100)
	entryNo = models.CharField(max_length=10, unique=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)

class CourseOffered(models.Model):
	facId = models.ForeignKey('Faculties', on_delete=models.CASCADE, blank=True, null=True)
	courseId = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True)
	course_year = models.CharField(max_length=4)
	course_sem = models.BooleanField()
	course_slot = models.ForeignKey('CourseSlots', models.CASCADE, related_name='+')	

class StudentCourseReg(models.Model):
	course_offered = models.ForeignKey('CourseOffered', models.CASCADE, blank=True, null=True)
	studentId = models.ForeignKey('Students', models.CASCADE, blank=True, null=True)




class AttendanceRecord(models.Model):

	class Meta(object):
		unique_together = (("date", "studentReg"), )

	date = models.DateField(db_index=True)
	studentReg = models.ForeignKey('StudentCourseReg', models.CASCADE, blank=True, null=True)
	value = models.BooleanField(default=True)

# class Pizza(models.Model):

# 	name = models.CharField(max_length=30)
# 	toppings = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas')

# 	def __str__(self):
# 		return self.name


# class Topping(models.Model):

# 	name = models.CharField(max_length=30)

# 	def __str__(self):
# 		return self.name

# class ToppingAmount(models.Model):

# 	REGULAR = 1
# 	DOUBLE = 2
# 	TRIPLE = 3
# 	AMOUNT_CHOICES = (
# 		(REGULAR, 'Regular'),
# 		(DOUBLE, 'Double'),
# 		(TRIPLE, 'Triple'),
# 	)

# 	pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
# 	topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
# 	amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
