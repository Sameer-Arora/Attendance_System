from django.contrib import admin

# Register your models here.
from .models import Courses, Timings, CourseSlots, Users

admin.site.register(Courses)
admin.site.register(Timings)
admin.site.register(CourseSlots)
admin.site.register(Users)