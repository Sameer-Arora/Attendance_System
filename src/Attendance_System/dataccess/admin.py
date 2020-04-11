from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .models import Courses, Timings, CourseSlots, Faculties,Students,TeachingAssistant,CourseOffered, StudentCourseReg,AttendanceRecord 

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Courses)
admin.site.register(Timings)
admin.site.register(CourseSlots)
admin.site.register(Faculties)
admin.site.register(Students)
admin.site.register(TeachingAssistant)
admin.site.register(CourseOffered)
admin.site.register(StudentCourseReg)
admin.site.register(AttendanceRecord)
# admin.site.register(User)
