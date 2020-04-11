import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Attendance_System.settings.base')

import django
django.setup()

import random
from django.contrib.auth.models import User
from dataccess.models import Profile,Courses, Timings, CourseSlots, Faculties, Students, TeachingAssistant, CourseOffered, StudentCourseReg, AttendanceRecord
from faker import Faker
from datetime import timedelta, datetime
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

courseId=[] #course code
cid = [] #course id
cont=[]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
usernameA = ['Akansha', 'Hersh', 'Harshit', 'Sameer', 'Sodhi', 'Anurag', 'Anil', 'Amit'] # usernames are created out of this list also
firstN = ['hello', 'avicii', 'khaleese', 'jong', 'kim', 'khalid', 'bravo', 'alpha']
lastN = ['beta', 'gamma', 'charlie', 'delta', 'rho', 'mho', 'ohm']
userTypeA=['TA','Faculty','Student']
deps=['cse', 'ee', 'me', 'ce', 'che'] #department 
desigs=['f1', 'f2', 'f3', 'f4'] #designation of facs
yr=['first','second', 'third', 'fourth'] #year
deg = ['btech', 'mtech', 'phd']

year = ['2017', '2018', '2019', '2020']
facID=[]

def genCID(): #course code
    cid = fakegen.pystr(max_chars=5)
    while(cid in courseId):
        cid = fakegen.pystr(max_chars=5)
    courseId.append(cid)
    # print("cid")
    # print(cid)
    return cid

def gencourseId():
    cid2 = fakegen.random_int(0, 100)
    while cid2 in cid:
        cid2 = fakegen.random_int(0, 100)
    cid.append(cid2)
    return cid2

def genContact():
    contacta = fakegen.phone_number()
    while contacta in cont:
        contacta = fakegen.phone_number()
    cont.append(contacta)
    return contacta

def genFID():
    fid = fakegen.random_int(0, 100)
    while fid in facID:
        fid = fakegen.random_int(0, 100)
    facID.append(fid)
    return fid

# def genUn():
#     un = fuzzy.FuzzyText(length=8)
#     while(un in usernameA):
#         un = fuzzy.FuzzyText(length=8)
#     usernameA.append(un)
#     return un

def add_courses():
    c, created = Courses.objects.get_or_create(courseId=gencourseId(), course_code=genCID(), course_name=fakegen.word(), 
                    lab_included=fakegen.boolean(chance_of_getting_true=50))
    c.save()
    return c 

def add_timings():
    tinit = fakegen.time()
    # print("tinit")
    # print (tinit)
    tend = fakegen.time()
    # print("tend")
    # print(tend)
    t, created = Timings.objects.get_or_create(day=random.choice(days), start_time=tinit, end_time=tend)
    t.save()
    return t

def add_Course_Slots():
    t1 = add_timings()
    t2 = add_timings()
    t3 = add_timings()
    cs, created = CourseSlots.objects.get_or_create()
    ts=[]
    ts.append(t1)
    ts.append(t2)
    ts.append(t3)
    cs.timing_list.set(ts)
    # cs.timing_list.set(t2)
    # cs.timing_list.set(t3)
    # cs.timing_list.add(t2)
    # cs.timing_list.add(t3)
    cs.save()
    return cs

def users(xyz):
    pwd = 'software'
    try:
        print("fsa")
        u = Profile.objects.create(xyz,random.choice(usernameA),pwd)
        # u.save()
        return u
    except Exception as e:
        print('Error: Invalid argument: {}'.format(e))

def fac():
    xyz = 'faculty'
    pwd = 'software'
    u = User.objects.create_user(username=fakegen.name(), password=pwd)
    # try:
    #     u = User.objects.create_user(username=random.choice(usernameA), password=pwd)
    #     u.userType=xyz
    #     u.save()
    #     # return u
    # except:
    #     pass

    fid = genFID()
    # print("u")
    # print(u)
    # print("fid")
    # print(fid)
    f, created = Faculties.objects.get_or_create( userId=u, firstName=random.choice(firstN), 
                                lastName=random.choice(lastN), department=random.choice(deps), 
                                designation=random.choice(desigs), contact=genContact(), 
                                emailId=fakegen.email())
    f.save()
    return f

def stu():
    xyz = 'student'
    pwd = 'software'
    u = User.objects.create_user(username=fakegen.name(), password=pwd)
    s, created = Students.objects.get_or_create(userId=u, entryNo=fakegen.pystr(max_chars=10), 
                                firstName=random.choice(firstN), lastName=random.choice(lastN), 
                                department=random.choice(deps), year=random.choice(yr), 
                                degree=random.choice(deg), contact=genContact(), 
                                emailId=fakegen.email())
    s.save()
    return s

def coff():
    fcid = fac()
    cid = add_courses()
    cslot = add_Course_Slots()
    coff, created = CourseOffered.objects.get_or_create(facId=fcid, courseId=cid, 
                                                course_year=fakegen.year, 
                                                course_sem=fakegen.boolean(chance_of_getting_true=50),
                                                course_slot=cslot)
    coff.save()
    return coff

def studentRegistersInCourse():
    student = stu()
    courseOffered = coff()
    src, created = StudentCourseReg.objects.get_or_create(course_offered=courseOffered, studentId=student)
    src.save()
    return src

def attendanceRec():
    stuRegistration = studentRegistersInCourse()
    ar, created = AttendanceRecord.objects.get_or_create(date=datetime.today(), studentReg=stuRegistration,
                                                        value=fakegen.boolean(chance_of_getting_true=75))
    ar.save()
    return ar

if __name__ == "__main__":
    print("Starting populating")
    x=users('student')
    # f = fac()
    # c = coff()
    # src=studentRegistersInCourse()
    # att = attendanceRec()
    print("user Created")    
