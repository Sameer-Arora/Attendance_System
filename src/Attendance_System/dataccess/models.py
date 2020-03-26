# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

# from django.db import models


# class AccountsStaff(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'accounts_staff'
# 		unique_together = (('staff', 'date_of_start', 'date_of_end'),)


# class Application(models.Model):
# 	application_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	post_name = models.ForeignKey('Post', models.CASCADE,max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True,default="pending")
# 	remarks = models.CharField(max_length=30, blank=True, null=True,default="pending")
# 	reach_point = models.CharField(max_length=30, blank=True, null=True,default="pending")
# 	number_of_regular_leaves = models.IntegerField(blank=True, null=True)
# 	number_of_borrowing_leaves = models.IntegerField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'application'


# class ApplicationPa(models.Model):
# 	application_id = models.AutoField(primary_key=True)
# 	project = models.ForeignKey('Project', models.CASCADE, blank=True, null=True)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	post_name = models.ForeignKey('Post', models.CASCADE, db_column='post_name', blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	reach_point = models.CharField(max_length=30, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'application_pa'


# class ArLeaveApproval(models.Model):
# 	application_id = models.IntegerField(primary_key=True)
# 	post_name = models.CharField(max_length=30)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'ar_leave_approval'
# 		unique_together = (('application_id', 'post_name'),)


# class ArapprovalPayslip(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	fac = models.ForeignKey('Faculty', models.CASCADE)
# 	month = models.ForeignKey('Bonus', models.CASCADE, db_column='month')
# 	year = models.IntegerField()
# 	salary = models.FloatField(blank=True, null=True)
# 	approval = models.CharField(max_length=30, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'arapproval_payslip'
# 		unique_together = (('staff', 'fac', 'month', 'year'),)


# class ArapprovalPayslip1(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	ps = models.ForeignKey('ProjectAssociate', models.CASCADE)
# 	month = models.ForeignKey('Bonus', models.CASCADE, db_column='month')
# 	year = models.IntegerField()
# 	salary = models.FloatField(blank=True, null=True)
# 	approval = models.CharField(max_length=30, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'arapproval_payslip1'
# 		unique_together = (('staff', 'ps', 'month', 'year'),)


# class AssociatedeanFa(models.Model):
# 	fac = models.ForeignKey('Faculty', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'associatedean_fa'
# 		unique_together = (('fac', 'date_of_start', 'date_of_end'),)


# class AsstRegistrar(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()
# 	dep = models.ForeignKey('StaffDepartment', models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'asst_registrar'
# 		unique_together = (('staff', 'date_of_start', 'date_of_end'),)


# class Bonus(models.Model):
# 	month = models.IntegerField(primary_key=True)
# 	year = models.IntegerField()
# 	amount = models.FloatField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'bonus'
# 		unique_together = (('month', 'year'),)


# class Cfti(models.Model):
# 	grade = models.CharField(primary_key=True, max_length=10)
# 	experience = models.IntegerField()
# 	salary = models.FloatField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'cfti'
# 		unique_together = (('grade', 'experience'),)


# class DeanFa(models.Model):
# 	fac = models.ForeignKey('Faculty', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'dean_fa'
# 		unique_together = (('fac', 'date_of_start', 'date_of_end'),)


# class DeanHiringApproval(models.Model):
# 	application_id = models.IntegerField(primary_key=True)
# 	post_name = models.CharField(max_length=30)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'dean_hiring_approval'
# 		unique_together = (('application_id', 'post_name'),)


# class DepartmentWiseFaculty(models.Model):
# 	fac = models.ForeignKey('Faculty', models.CASCADE, primary_key=True)
# 	dep = models.ForeignKey('FacultyDepartment', models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'department_wise_faculty'


# class DepartmentWiseStaff(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	dep = models.ForeignKey('StaffDepartment', models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'department_wise_staff'


# class DeptSecretaryFaculty(models.Model):
# 	staff_id = models.CharField(primary_key=True, max_length=10)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	date_of_joining = models.DateField()
# 	date_of_leaving = models.DateField(blank=True, null=True)
# 	dep = models.ForeignKey('FacultyDepartment', models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'dept_secretary_faculty'


# class DeptSecretaryStaff(models.Model):
# 	staff_id = models.CharField(primary_key=True, max_length=10)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	date_of_joining = models.DateField()
# 	date_of_leaving = models.DateField(blank=True, null=True)
# 	dep = models.ForeignKey('StaffDepartment', models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'dept_secretary_staff'


# class DirLeaveApproval(models.Model):
# 	application_id = models.IntegerField(primary_key=True)
# 	post_name = models.CharField(max_length=30)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'dir_leave_approval'
# 		unique_together = (('application_id', 'post_name'),)


# class EstablishmentStaff(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'establishment_staff'
# 		unique_together = (('staff', 'date_of_start', 'date_of_end'),)


# class Faculty(models.Model):
# 	fac_id = models.CharField(primary_key=True, max_length=10)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	date_of_joining = models.DateField()
# 	date_of_leaving = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'faculty'


# class FacultyDepartment(models.Model):
# 	dep_id = models.CharField(primary_key=True, max_length=10)
# 	name = models.CharField(max_length=20)

# 	class Meta:
# 		managed = False
# 		db_table = 'faculty_department'


# class FacultyPost(models.Model):
# 	fac = models.ForeignKey(Faculty, models.CASCADE, blank=True, null=True)
# 	faculty_post_name = models.ForeignKey('Post', models.CASCADE, db_column='faculty_post_name', primary_key=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'faculty_post'


# class FinalTable(models.Model):
# 	application_id = models.IntegerField(primary_key=True)
# 	post_name = models.CharField(max_length=30)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'final_table'
# 		unique_together = (('application_id', 'post_name'),)


# class FinalTablePa(models.Model):
# 	application_id = models.IntegerField(primary_key=True)
# 	pi_post = models.CharField(max_length=30)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'final_table_pa'
# 		unique_together = (('application_id', 'pi_post'),)


# class FundingAgency(models.Model):
# 	agency_id = models.AutoField(primary_key=True)
# 	agency_name = models.CharField(max_length=30, blank=True, null=True)
# 	agency_address = models.CharField(max_length=30, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'funding_agency'


# class FundingSalary(models.Model):
# 	agency = models.ForeignKey(FundingAgency, models.CASCADE, primary_key=True)
# 	manpower_jrf = models.IntegerField(blank=True, null=True)
# 	manpower_srf = models.IntegerField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'funding_salary'


# class GradeHistory(models.Model):
# 	fac = models.ForeignKey(Faculty, models.CASCADE, primary_key=True)
# 	grade_no = models.ForeignKey('Grades', models.CASCADE, db_column='grade_no')
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'grade_history'
# 		unique_together = (('fac', 'grade_no', 'date_of_start', 'date_of_end'),)


# class Grades(models.Model):
# 	grade_no = models.CharField(primary_key=True, max_length=10)

# 	class Meta:
# 		managed = False
# 		db_table = 'grades'


# class Hod(models.Model):
# 	fac = models.ForeignKey(Faculty, models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()
# 	dep = models.ForeignKey(FacultyDepartment, models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'hod'
# 		unique_together = (('fac', 'date_of_start', 'date_of_end'),)


# class Login(models.Model):
# 	user = models.ForeignKey('Users', models.CASCADE, primary_key=True)
# 	role = models.ForeignKey('Role', models.CASCADE)
# 	time_last_logged = models.DateTimeField()

# 	def __str__(self):
# 		return self.user.username  +' '+ self.role.name
			
# 	class Meta:
# 		managed = False
# 		db_table = 'login'
# 		unique_together = (('user', 'role'),)


# class MainPi(models.Model):
# 	project = models.ForeignKey('Project', models.CASCADE, primary_key=True)
# 	fac = models.ForeignKey(Faculty, models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'main_pi'


# class Payslip(models.Model):
# 	fac = models.ForeignKey(Faculty, models.CASCADE, primary_key=True)
# 	month = models.ForeignKey(Bonus, models.CASCADE, db_column='month')
# 	year = models.IntegerField()
# 	salary = models.FloatField(blank=True, null=True)
# 	approval = models.CharField(max_length=30, blank=True, null=True)
# 	approval_staff = models.CharField(max_length=10, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'payslip'
# 		unique_together = (('fac', 'month', 'year'),)


# class Payslip1(models.Model):
# 	ps = models.ForeignKey('ProjectAssociate', models.CASCADE, primary_key=True)
# 	month = models.IntegerField()
# 	year = models.IntegerField()
# 	salary = models.FloatField(blank=True, null=True)
# 	approval = models.CharField(max_length=30, blank=True, null=True)
# 	approval_staff = models.CharField(max_length=10, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'payslip1'
# 		unique_together = (('ps', 'month', 'year'),)


# class Permission(models.Model):
# 	permiss_id = models.AutoField(primary_key=True)
# 	name = models.CharField(unique=True, max_length=30)
# 	modules = models.CharField(max_length=100)

# 	class Meta:
# 		managed = False
# 		db_table = 'permission'


# class Pi(models.Model):
# 	project = models.ForeignKey('Project', models.CASCADE, primary_key=True)
# 	fac = models.ForeignKey(Faculty, models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'pi'
# 		unique_together = (('project', 'fac'),)


# class Post(models.Model):
# 	post_name = models.CharField(primary_key=True, max_length=30)

# 	class Meta:
# 		managed = False
# 		db_table = 'post'


# class PostToSucc(models.Model):
# 	post_name = models.ForeignKey('Post', models.CASCADE,primary_key=True, max_length=30,related_name='%(class)s_post_name')
# 	succ_post_name = models.ForeignKey('Post', models.CASCADE,max_length=30, blank=True, null=True,related_name='%(class)s_succ_post_name')

# 	class Meta:
# 		managed = False
# 		db_table = 'post_to_succ'


# class Project(models.Model):
# 	project_id = models.AutoField(primary_key=True)
# 	project_name = models.CharField(max_length=30, blank=True, null=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField(blank=True, null=True)
# 	manpower = models.FloatField(blank=True, null=True)
# 	equipment = models.FloatField(blank=True, null=True)
# 	travel = models.FloatField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'project'


# class ProjectAssociate(models.Model):
# 	ps_id = models.CharField(primary_key=True, max_length=10)
# 	post_id = models.CharField(max_length=10, blank=True, null=True)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	date_of_joining = models.DateField()
# 	date_of_leaving = models.DateField(blank=True, null=True)

# 	class Meta:  
# 		managed = False
# 		db_table = 'project_associate'


# class ProjectAssociateLinkProject(models.Model):
# 	ps = models.ForeignKey(ProjectAssociate, models.CASCADE, primary_key=True)
# 	project = models.ForeignKey(Project, models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'project_associate_link_project'


# class ProjectFunding(models.Model):
# 	project = models.ForeignKey(Project, models.CASCADE, primary_key=True)
# 	agency = models.ForeignKey(FundingAgency, models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'project_funding'
# 		unique_together = (('project', 'agency'),)


# class ReportingPi(models.Model):
# 	ps = models.ForeignKey(ProjectAssociate, models.CASCADE, primary_key=True)
# 	fac = models.ForeignKey(Faculty, models.CASCADE, blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'reporting_pi'


# class Role(models.Model):
# 	role_id = models.AutoField(primary_key=True)
# 	name = models.CharField(unique=True, max_length=30)
# 	description = models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.name

# 	class Meta:
# 		managed = False
# 		db_table = 'role'


# class RoleGets(models.Model):
# 	role = models.ForeignKey(Role, models.CASCADE, primary_key=True)
# 	max_leaves_alloted = models.IntegerField()
# 	max_leaves_borrowed = models.IntegerField()

# 	class Meta:
# 		managed = False
# 		db_table = 'role_gets'


# class RolePermission(models.Model):
# 	role = models.ForeignKey(Role, models.CASCADE, primary_key=True)
# 	permiss = models.ForeignKey(Permission, models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'role_permission'
# 		unique_together = (('role', 'permiss'),)


# class SponsoredProjectsStaff(models.Model):
# 	staff = models.ForeignKey('Staff', models.CASCADE, primary_key=True)
# 	date_of_start = models.DateField()
# 	date_of_end = models.DateField()

# 	class Meta:
# 		managed = False
# 		db_table = 'sponsored_projects_staff'
# 		unique_together = (('staff', 'date_of_start', 'date_of_end'),)


# class Staff(models.Model):
# 	staff_id = models.CharField(primary_key=True, max_length=10)
# 	user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
# 	date_of_joining = models.DateField()
# 	date_of_leaving = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'staff'


# class StaffDepartment(models.Model):
# 	dep_id = models.CharField(primary_key=True, max_length=10)
# 	name = models.CharField(max_length=20)

# 	class Meta:
# 		managed = False
# 		db_table = 'staff_department'


# class StaffPost(models.Model):
# 	staff = models.ForeignKey(Staff, models.CASCADE, blank=True, null=True)
# 	staff_post_name = models.ForeignKey(Post, models.CASCADE, db_column='staff_post_name', primary_key=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'staff_post'


# class Successor(models.Model):
# 	application_id = models.IntegerField()
# 	post_name = models.ForeignKey('Post', models.CASCADE, max_length=30,related_name='%(class)s_post_name')
# 	succ_post_name = models.ForeignKey('Post', models.CASCADE,max_length=30, blank=True, null=True,related_name='%(class)s_succ_post_name')
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'successor'
# 		unique_together = (('application_id', 'post_name', 'succ_post_name'),)


# class SuccessorPa(models.Model):
# 	application_id = models.IntegerField(primary_key=True)  
# 	pi_post = models.ForeignKey(Post, models.CASCADE, db_column='pi_post',related_name='%(class)s_pi_post')
# 	succ_pi_post = models.ForeignKey(Post, models.CASCADE, db_column='succ_pi_post',related_name='%(class)ssucc_pi_post', blank=True, null=True)
# 	comments = models.CharField(max_length=30, blank=True, null=True)
# 	status = models.CharField(max_length=30, blank=True, null=True)
# 	remarks = models.CharField(max_length=30, blank=True, null=True)
# 	date_forwarded = models.DateField(blank=True, null=True)

# 	class Meta:
# 		managed = False
# 		db_table = 'successor_pa'
# 		unique_together = (('application_id', 'pi_post'),)


# class UserRole(models.Model):
# 	role = models.ForeignKey(Role, models.CASCADE, primary_key=True)
# 	user = models.ForeignKey('Users', models.CASCADE)

# 	class Meta:
# 		managed = False
# 		db_table = 'user_role'
# 		unique_together = (('role', 'user'),)


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
