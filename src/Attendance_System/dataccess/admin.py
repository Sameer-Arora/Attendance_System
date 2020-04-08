from django.contrib import admin

# Register your models here.
# from django.contrib.auth.models import User
from .models import Courses, Timings, CourseSlots, Faculties,Students,TeachingAssistant,CourseOffered

admin.site.register(Courses)
admin.site.register(Timings)
admin.site.register(CourseSlots)
admin.site.register(Faculties)
admin.site.register(Students)
admin.site.register(TeachingAssistant)
admin.site.register(CourseOffered)
# admin.site.register(StudentCourseReg)
# admin.site.register(AttendanceRecord)
# admin.site.register(User)