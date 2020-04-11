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
	courseId = models.IntegerField(blank=True, null=True)
	course_code = models.CharField(max_length=5, blank=False, null=False, default='xxxxx')
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

# class Users(models.Model):
# 	userId = models.AutoField(primary_key=True)
# 	userName = models.CharField(max_length=30, unique=True)
# 	password = models.CharField(max_length=30)
# 	userType = models.CharField(max_length=30)
# 	def __str__(self):
# 		return self.userId

class UserManager(models.Manager):

	def create(self,userType,username,password,**kwargs  ):
		print(**kwargs)
		user = User(username=username,password=password, **kwargs)
		user.save()
		profile = Profile(
			user=user,
			userType=userType,
		)
		profile.save()
		return user

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	userType = models.CharField(max_length=30)
	objects = UserManager()

	def __str__(self): 
		return self.user.username

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)
# 	instance.profile.save()

class Faculties(models.Model):
	facId = models.AutoField(primary_key=True)
	userId = models.OneToOneField(User, models.CASCADE,db_index=False)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	contact = models.CharField(unique=True, max_length=100)
	emailId = models.CharField( max_length=100)
	def __str__(self):
		return self.facId

class Students(models.Model):
	userId = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	entryNo = models.CharField(max_length=10, unique=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	year = models.CharField(max_length=10)
	degree = models.CharField(max_length=30)
	contact = models.CharField(unique=True, max_length=20)
	emailId = models.CharField( max_length=100)
	def __str__(self):
		return self.entryNo

class TeachingAssistant(models.Model):
	userId = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	course_offered = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True) 
	contact = models.CharField(max_length=15, unique=True)
	emailId = models.CharField( max_length=100)
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
	course_slot = models.ForeignKey('CourseSlots', models.CASCADE, related_name='+')	

class StudentCourseReg(models.Model):
	course_reg_id = models.AutoField(primary_key=True)
	course_offered = models.ForeignKey('CourseOffered', models.CASCADE, blank=True, null=True)
	studentId = models.ForeignKey('Students', models.CASCADE, blank=True, null=True)




class AttendanceRecord(models.Model):

	class Meta(object):
		unique_together = (("date", "studentReg"), )

	date = models.DateField(db_index=True)
	studentReg = models.ForeignKey('StudentCourseReg', models.CASCADE, blank=True, null=True)
	value = models.BooleanField(default=True)
