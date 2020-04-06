import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Attendance_System/settings.base')

import django
django.setup()

import random

from attendance_management.models import Courses, Timings, CourseSlots, Users, Faculties, Students, TeachingAssistant, CourseOffered, StudentCourseReg, AttendanceRecord
from faker import Faker
from datetime import timedelta
import factory.fuzzy

fakegen = Faker()

# schools = ['dps', 'avn']

# fake_address = fakegen.address()
# fake_email = fakegen.email()
# fake_phone_number = fakegen.phone_number()

# def add_school():
#     s = School.objects.get_or_create(name=random.choice(schools), address=fake_address, email=fake_email, phone_number=fake_phone_number)[0]
#     s.save()
#     return s 

courseId=[]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
usernameA = ['Akansha', 'Hersh', 'Harshit', 'Sameer', 'Sodhi', 'Anurag', 'Anil', 'Amit']
userTypeA=['TA','Faculty','Student']
deps=['cse', 'ee', 'me', 'ce', 'che'] #department 
desigs=['f1', 'f2', 'f3', 'f4'] #designation of facs

def genCID(): 
    cid = fuzzy.FuzzyText(length=5)
    while(cid in courseId):
        cid = fuzzy.FuzzyText(length=5)
    courseId.append(cid)
    return cid

# def genUn():
#     un = fuzzy.FuzzyText(length=8)
#     while(un in usernameA):
#         un = fuzzy.FuzzyText(length=8)
#     usernameA.append(un)
#     return un

def add_courses():
    c = Courses.objects.get_or_create(course_code=genCID(), course_name=fuzzy.FuzzyText(length=10), 
                    lab_included=True)
    c.save()
    return c 

def add_timings():
    tinit = fakegen.time()
    tend = tinit+timedelta(hours=1)
    t = Timings.objects.get_or_create(day=random.choice(days), start_time=tinit, end_time=tend)
    t.save()
    return t

def add_Course_Slots():
    t1 = add_timings()
    t2 = add_timings()
    t3 = add_timings()
    cs = CourseSlots.objects.get_or_create(timing_list=[t1, t2, t3])
    cs.save()
    return cs

def users(xyz):
    pwd = 'software'
    u = Users.objects.get_or_create(userName=random.choice(usernameA), password=pwd, userType=xyz)
    u.save()
    return u

def fac():
    xyz = 'faculty'
    uid = users(xyz)
    f = Faculties.objects.get_or_create(userId=uid.userId, firstName=fakegen.name(), 
                                lastName=fuzzy.FuzzyText(length=8), department=random.choice(deps), 
                                designation=random.choice(desigs), contact=fakegen.phone_number(), 
                                emailId=fakegen.email())
    f.save()
    return f

def stu():
    

if __name__ == "__main__":
    print("Starting populating")
    x=users('Student')
    print("user Created")    
