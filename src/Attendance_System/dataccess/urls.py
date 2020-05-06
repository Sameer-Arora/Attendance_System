"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from dataccess import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'user', views.UserView, 'user')     # add this
router.register(r'profile', views.ProfileView, 'profile')     # add this
router.register(r'course', views.CoursesView, 'course')     # add this
router.register(r'timings',views.TimingsView,'timings')
router.register(r'faculties',views.FacultiesView,'faculties')
router.register(r'students',views.StudentsView,'students')
router.register(r'teachingassistant',views.TeachingAssistantView,'teachingassistant')
router.register(r'courses',views.CoursesView,'courses')
router.register(r'timings',views.TimingsView,'timings')
router.register(r'courseslots',views.CourseSlotsView,'courseslots')
router.register(r'courseoffered',views.CourseOfferedView,'courseoffered')
router.register(r'studentCourseReg',views.StudentCourseRegView,'studentCourseReg')
router.register(r'attendanceRecord',views.AttendanceRecordView,'attendanceRecord')

urlpatterns = [
    path('login/',views.LoginView.as_view(),name="login"),
    path('faculty/<int:facId>/courses',views.FacultiesCoursesView.as_view(),name="faculty-courseoffered"),
    path('student/<int:stuId>/courses',views.StudentsCoursesView.as_view(),name="student-coursesregistered"),
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]