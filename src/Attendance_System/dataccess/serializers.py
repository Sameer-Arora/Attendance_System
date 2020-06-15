from rest_framework import serializers
from django.contrib.auth.models import User
from dataccess.models import *
from rest_framework.reverse import reverse

# ANOTHER APPROACH TO ACHIEVE THE SAME.
# class ProfileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Profile
# 		fields = ('id', 'user','userType',)

# class UserSerializer(serializers.ModelSerializer):
# 	# profile = ProfileSerializer()
# 	profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
# 	id = serializers.IntegerField(read_only=True)
# 	class Meta:
# 		model = User
# 		fields = ('id', 'username', 'password', 'first_name', 'last_name','profile')
# 		## You can also give the related_name argument in model and use that here.
# 		depth= 1
		
# 	def create(self, validated_data):
# 		profile_data = validated_data.pop('profile')
# 		user = User.objects.create_user(**validated_data)
# 		Profile.objects.create(profile_data['userType'],user)
# 		return user

class UserSerializer(serializers.HyperlinkedModelSerializer):
# class DefUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('url','id', 'username', 'password', 'first_name', 'last_name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	UserSerializer
	class Meta:
		model = Profile
		fields = ('url','id', 'user','userType',)
		# depth= 1
		
	def create(self, validated_data):
		profile_data = validated_data.pop('user')
		user = User.objects.create_user(**profile_data)
		Profile.objects.create(validated_data['userType'],user)
		return user

# Create your models here.
class CoursesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Courses
		fields = ('url','id', 'course_code', 'course_name', 'lab_included',)

class TimingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timings
		fields = '__all__'

class CourseSlotsSerializer(serializers.HyperlinkedModelSerializer):
	timing_list = TimingsSerializer()
	class Meta:
		model = CourseSlots
		fields ='__all__'
		
class CourseOfferedSerializer(serializers.HyperlinkedModelSerializer):
	courseId = CoursesSerializer()
	course_slot = CourseSlotsSerializer()	
	class Meta:
		model = CourseOffered
		fields ='__all__'

	# course_offered_id = models.AutoField(primary_key=True)
	# facId = models.ForeignKey('Faculties', on_delete=models.CASCADE, blank=True, null=True)
	# courseId = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True)
	# course_year = models.CharField(max_length=4)
	# course_sem = models.BooleanField()

	
		
class FacultiesSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	courseoffered = serializers.SerializerMethodField()
	# courseoffered = CourseOfferedSerializer()
	class Meta:
		model = Faculties
		fields = ('url','user','firstName','lastName','department','designation','contact','emailId','courseoffered')
	def get_courseoffered(self,obj):
		result = '{}?{}'.format(
			reverse('faculty-courseoffered', args=[obj.id], request=self.context['request']),
			'param=foo'
		)
		print(result)
		return result

	# facId = models.AutoField(primary_key=True)
	# userId = models.OneToOneField(User, models.CASCADE,db_index=False)
	# firstName = models.CharField(max_length=30)
	# lastName = models.CharField(max_length=30)
	# department = models.CharField(max_length=30)
	# designation = models.CharField(max_length=30)
	# contact = models.CharField(unique=True, max_length=100)
	# emailId = models.CharField( max_length=100)

class StudentsSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	courseoffered = serializers.SerializerMethodField()
	def get_courseoffered(self,obj):
		result = '{}?{}'.format(
			reverse('student-coursesregistered', args=[obj.id], request=self.context['request']),
			'param=foo'
		)
		print(result)
		return result
	class Meta:
		model = Students
		fields = '__all__'
	# userId = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	# entryNo = models.CharField(max_length=10, unique=True)
	# firstName = models.CharField(max_length=30)
	# lastName = models.CharField(max_length=30)
	# department = models.CharField(max_length=30)
	# year = models.CharField(max_length=10)
	# degree = models.CharField(max_length=30)
	# contact = models.CharField(unique=True, max_length=100)
	# emailId = models.CharField( max_length=100)


class TeachingAssistantSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	class Meta:
		model = TeachingAssistant
		fields ='__all__'
	
	# userId = models.OneToOneField(User, models.CASCADE, blank=True, null=True)
	# course_offered = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True) 
	# contact = models.CharField(max_length=15, unique=True)
	# emailId = models.CharField( max_length=100)
	# entryNo = models.CharField(max_length=10, unique=True)
	# firstName = models.CharField(max_length=30)
	# lastName = models.CharField(max_length=30)
	# department = models.CharField(max_length=30)

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Courses
		fields ='__all__'


class StudentCourseRegSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = StudentCourseReg
		fields ='__all__'

	# course_reg_id = models.AutoField(primary_key=True)
	# course_offered = models.ForeignKey('CourseOffered', models.CASCADE, blank=True, null=True)
	# studentId = models.ForeignKey('Students', models.CASCADE, blank=True, null=True)


class AttendanceRecordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AttendanceRecord
		fields ='__all__'

	# date = models.DateField(db_index=True)
	# studentReg = models.ForeignKey('StudentCourseReg', models.CASCADE, blank=True, null=True)
	# value = models.BooleanField(default=True)


