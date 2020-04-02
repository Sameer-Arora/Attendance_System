# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

# from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

# class Users(models.Model):
# 	user_id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=30)
# 	email = models.CharField(unique=True, max_length=100)
# 	address = models.CharField(max_length=400, blank=True, null=True)
# 	mobile = models.BigIntegerField(unique=True)
# 	username = models.CharField(unique=True, max_length=30)
# 	password = models.CharField(max_length=30)
# 	leaves_left = models.IntegerField()
# 	leaves_borrowed = models.IntegerField()
	
# 	def __str__(self):
# 		return self.username +' '+ self.name  +' '+ self.email+' '+str(self.user_id)
			
# 	class Meta:
# 		managed = False
# 		db_table = 'users'
