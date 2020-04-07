import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Attendance_System.settings.base')

import django
django.setup()

import random
from django.contrib.auth.models import User
# from dataccess.models import Courses, Timings, CourseSlots, Profile, Faculties, Students, TeachingAssistant, CourseOffered, StudentCourseReg, AttendanceRecord
from dataccess.models import Courses, Timings, CourseSlots, Profile, Faculties, Students, CourseOffered, StudentCourseReg, AttendanceRecord
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
cont=[]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
usernameA = ['Akansha', 'Hersh', 'Harshit', 'Sameer', 'Sodhi', 'Anurag', 'Anil', 'Amit']
firstN = ['hello', 'avicii', 'khaleese', 'jong', 'kim', 'khalid', 'bravo', 'alpha']
lastN = ['beta', 'gamma', 'charlie', 'delta', 'rho', 'mho', 'ohm']
userTypeA=['TA','Faculty','Student']
deps=['cse', 'ee', 'me', 'ce', 'che'] #department 
desigs=['f1', 'f2', 'f3', 'f4'] #designation of facs
yr=['first','second', 'third', 'fourth'] #year
deg = ['btech', 'mtech', 'phd']

def genCID(): 
    cid = fuzzy.FuzzyText(length=5)
    while(cid in courseId):
        cid = fuzzy.FuzzyText(length=5)
    courseId.append(cid)
    return cid

def genContact():
    contacta = fakegen.phone_number()
    while contacta in cont:
        contacta = fakegen.phone_number()
    cont.append(contacta)
    return contacta

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
    try:
        u = User.objects.create_user(username=random.choice(usernameA), password=pwd)
        u.userType=xyz
        u.save()
        return u
    except:
        pass
def fac():
    xyz = 'faculty'
    uid = users(xyz)
    f = Faculties.objects.get_or_create(userId=uid.userId, firstName=random.choice(firstN), 
                                lastName=random.choice(lastN), department=random.choice(deps), 
                                designation=random.choice(desigs), contact=genContact(), 
                                emailId=fakegen.email())
    f.save()
    return f

def stu():
    xyz = 'student'
    uid = users(xyz)
    s = Students.objects.get_or_create(userId=uid.userId, entryNo=fuzzy.FuzzyText(length=10), 
                                firstName=random.choice(firstN), lastName=random.choice(lastN), 
                                department=random.choice(deps), year=random.choice(yr), 
                                degree=random.choice(deg), contact=genContact(), 
                                emailId=fakegen.email())
    s.save()
    return s

# def coff():
#     fcid = fac()
#     coff = CourseOffered.objects.get_or_create(facId=fcid.facId, )


if __name__ == "__main__":
    print("Starting populating")
    x=users('student')
    print("user Created")    
