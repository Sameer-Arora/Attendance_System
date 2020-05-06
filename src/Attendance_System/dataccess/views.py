
# Create your views here.

from django.shortcuts import render
from rest_framework import views,viewsets,permissions,status,generics          # add this
from .serializers import *      # add this
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

usertype_dict ={ "student":StudentsSerializer ,"faculty":FacultiesSerializer }

class LoginView(views.APIView):       # add this
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': unicode(request.auth),  # None
    #     }
    #     return Response(content)    
    
    def post(self,request,format=None):
        print(request)
        data = request.data
        print(data)

        username=data.get('username',None)
        password=data.get('password',None)
        print(data,username,password)
        user= authenticate(username=username,password=password)
        content = {'status':"Invalid"}
        if user is not None:
            login(request, user)
            try:
                profile = Profile.objects.get(user=user)
                print(profile)
            except Profile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if profile.userType == "student":
                model = Students.objects.get(user=user)
                serializer = StudentsSerializer(model,context={'request': request})
            elif profile.userType == "faculty":
                model = Faculties.objects.get(user=user)
                serializer = FacultiesSerializer(model,context={'request': request})
            print(serializer.data)
            content=serializer.data
            content['status']='Valid'
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(content,status=status.HTTP_404_NOT_FOUND)

class StudentsCoursesView(views.APIView):
    def get(self,request,stuId,format=None):
            print(request,stuId)
            data = request.data
            print(data)
            student= Students.objects.get_or_create(id=stuId)
            content = {'status':"Student Id Invalid", 'courses':[]}
            if student is not None:
                coursetaken = student.courses.all()
                    # courseoffered = CourseOffered.objects.filter(facId=facId)
                print(courseoffered)
                if len(courseoffered) <= 0:
                    content['status']='Student takes no courses.'
                    return Response(content,status=status.HTTP_404_NOT_FOUND)

                serializer = CourseOfferedSerializer(courseoffered,context={'request': request},many=True)
                print(serializer.data)
                content['courses']=serializer.data
                content['status']='Valid'
                return Response(content,status=status.HTTP_200_OK)
            else:
                return Response(content,status=status.HTTP_404_NOT_FOUND)

class CoursesStudentsView(views.APIView):
    def get(self,request,courseId,format=None):
            print(request,courseId)
            data = request.data
            print(data)
            courseoffered = CourseOffered.objects.get_or_create(id=courseId)
            courseoffered = {'status':"Courseoffered Id Invalid", 'students':[]}
            if courseoffered is not None:
                coursetaken = courseoffered.students.all()
                    # courseoffered = CourseOffered.objects.filter(facId=facId)
                print(courseoffered)
                if len(courseoffered) <= 0:
                    content['status']='Student takes no courses.'
                    return Response(content,status=status.HTTP_404_NOT_FOUND)

                serializer = CourseOfferedSerializer(courseoffered,context={'request': request},many=True)
                print(serializer.data)
                content['courses']=serializer.data
                content['status']='Valid'
                return Response(content,status=status.HTTP_200_OK)
            else:
                return Response(content,status=status.HTTP_404_NOT_FOUND)

class FacultiesCoursesView(views.APIView):
    
    def get(self,request,facId,format=None):
        print(request,facId)
        data = request.data
        print(data)
        faculty= Faculties.objects.get_or_create(id=facId)
        content = {'status':"Faculty Id Invalid", 'courses':[]}
        if faculty is not None:
            courseoffered = CourseOffered.objects.filter(facId_id=facId)
                # courseoffered = CourseOffered.objects.filter(facId=facId)
            print(courseoffered)
            if len(courseoffered) <= 0:
                content['status']='Faculty teaches no courses.'
                return Response(content,status=status.HTTP_404_NOT_FOUND)

            serializer = CourseOfferedSerializer(courseoffered,context={'request': request},many=True)
            print(serializer.data)
            content['courses']=serializer.data
            content['status']='Valid'
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(content,status=status.HTTP_404_NOT_FOUND)

## Trying customization of Genric Views.
# class FacultiesCoursesView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CourseOffered.objects.filter(facId_id=facId)  ## querying through foriegn key's ID.
#     serializer_class = CourseOfferedSerializer
        
class UserView(viewsets.ModelViewSet):       # add this
    serializer_class = UserSerializer          # add this
    queryset = User.objects.all()              # add this
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all() 
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() 
class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all() 
class TimingsView(viewsets.ModelViewSet):
    serializer_class = TimingsSerializer
    queryset = Timings.objects.all() 
class FacultiesView(viewsets.ModelViewSet):
    serializer_class = FacultiesSerializer
    queryset = Faculties.objects.all() 
class StudentsView(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all() 
class TeachingAssistantView(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantSerializer
    queryset = TeachingAssistant.objects.all() 
class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all() 
class CourseSlotsView(viewsets.ModelViewSet):
    serializer_class = CourseSlotsSerializer
    queryset = CourseSlots.objects.all() 
class TimingsView(viewsets.ModelViewSet):
    serializer_class = TimingsSerializer
    queryset = Timings.objects.all() 
class CourseOfferedView(viewsets.ModelViewSet):
    serializer_class = CourseOfferedSerializer
    queryset = CourseOffered.objects.all() 
class StudentCourseRegView(viewsets.ModelViewSet):
    serializer_class = StudentCourseRegSerializer
    queryset = StudentCourseReg.objects.all() 
class AttendanceRecordView(viewsets.ModelViewSet):
    serializer_class = AttendanceRecordSerializer
    queryset = AttendanceRecord.objects.all() 