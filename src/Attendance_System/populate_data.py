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
datex=[]

def genDates():
    d = fakegen.date_this_year()
    while d in datex:
        d = fakegen.date_this_year()
    datex.append(d)
    return d

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
    c, created = Courses.objects.get_or_create(id=gencourseId(), course_code=genCID(), course_name=fakegen.word(), 
                    lab_included=fakegen.boolean(chance_of_getting_true=50))
    c.save()
    return c 

def add_timings():
    tinit = fakegen.time()
    # print("tinit")
    # print (tinit)
    tend = fakegen.time()
    # print("tend")
    # print(tend)ingAmount.objects.create(pizza=super_pep, topping=pepperoni, amount=ToppingAmount.DOUBLE)

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

def add_Course_Slots(t1, t2, t3): #parametrized
    # t1 = add_timings()
    # t2 = add_timings()
    # t3 = add_timings()
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


def users(xyz,pwd):
    try:
        # print("fsa")
        u = User.objects.create_user(username=fakegen.name(),password=pwd)
        u.save()
        p = Profile.objects.create(xyz,u)
        return u
    except Exception as e:
        print('Error: Invalid argument: {}'.format(e))
        return None

def fac():
    xyz = 'faculty'
    pwd = 'software'
    u = users(xyz,pwd)
    fid = genFID()
    # print("u")
    # print(u)
    # print("fid")
    # print(fid)
    f, created = Faculties.objects.get_or_create( user=u, firstName=random.choice(firstN), 
                                lastName=random.choice(lastN), department=random.choice(deps), 
                                designation=random.choice(desigs), contact=genContact(), 
                                emailId=fakegen.email())
    f.save()
    return f

def stu():
    xyz = 'student'
    pwd = 'software'
    u = users(xyz,pwd)
    s, created = Students.objects.get_or_create(user=u, entryNo=fakegen.pystr(max_chars=10), 
                                firstName=random.choice(firstN), lastName=random.choice(lastN), 
                                department=random.choice(deps), year=random.choice(yr), 
                                degree=random.choice(deg), contact=genContact(), 
                                emailId=fakegen.pystr(max_chars=10))
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

def coffFacSlot(fcid, cid, cslot): #parameterized function for course offered
    # fcid = fac()
    # cid = add_courses()
    # cslot = add_Course_Slots()
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

def studentRegistersInCourse(student, courseOffered): #parameterized 
    # student = stu()
    # courseOffered = coff()
    src, created = StudentCourseReg.objects.get_or_create(course_offered=courseOffered, studentId=student)
    src.save()
    return src


def attendanceRec(): # considers attendance of today only
    stuRegistration = studentRegistersInCourse()
    ar, created = AttendanceRecord.objects.get_or_create(date=datetime.today(), studentReg=stuRegistration,
                                                        value=fakegen.boolean(chance_of_getting_true=75))
    ar.save()
    return ar

def attendanceRec(datewa, stuRegistration):
    # stuRegistration = studentRegistersInCourse()
    ar, created = AttendanceRecord.objects.get_or_create(date=datewa, studentReg=stuRegistration,
                                                        value=fakegen.boolean(chance_of_getting_true=75))
    ar.save()
    return ar


def class1():
    s1 = stu()
    s2 = stu()
    s3 = stu()
    s4 = stu()
    f1 = fac()
    f2 = fac()
    course = add_courses()
    t1 = add_timings()
    t2 = add_timings()
    t3 = add_timings()
    t4 = add_timings()
    cslot1 = add_Course_Slots(t1, t2, t3)
    cslot2 = add_Course_Slots(t2, t3, t4)
    coff1 = coffFacSlot(f1, course, cslot1)
    coff2 = coffFacSlot(f2, course, cslot2)
    sr1 = studentRegistersInCourse(s1, coff1)#student1 registration coff1
    sr2 = studentRegistersInCourse(s2, coff1)#student2 registration coff1
    sr3 = studentRegistersInCourse(s3, coff2)#student3 registration coff2
    sr4 = studentRegistersInCourse(s4, coff2)#student4 registration coff2 
    dates=[]
    x=0
    while x<5:
        x = x+1
        d=genDates()
        dates.append(d)
    ar1=[] #attendance record of student registration 1
    ar2=[]
    ar3=[]
    ar4=[]
    for i in dates:
        a1 = attendanceRec(i, sr1)
        a2 = attendanceRec(i, sr2) 
        a3 = attendanceRec(i, sr3)
        a4 = attendanceRec(i, sr4)
        ar1.append(a1)
        ar2.append(a2)
        ar3.append(a3)
        ar4.append(a4)

    return
import shlex
import subprocess

def system_call(command,stdin=None):
    print(stdin)
    inp=shlex.split(command)
    process = subprocess.run(inp, 
                            stdout=subprocess.PIPE, 
                            universal_newlines=True,
                            input=stdin)
    return process

def clear_database():
    process = system_call(" psql -d sameer -c \"DROP DATABASE test\" ")
    print(process)
    process = system_call(" psql -c  \"CREATE DATABASE test;\" ")
    print(process)
    process = system_call(" python manage.py makemigrations ")
    print(process)
    process = system_call(" python manage.py migrate ")
    print(process)
    process = system_call("echo \"from django.contrib.auth.models import User; User.objects.create_superuser('qw', 'admin@example.com', '12')\"")
    print(process)
    process = system_call("python manage.py shell",stdin=process.stdout)  
    print(process)
     
clear_database()     
if __name__ == "__main__":
    clear_database()
    print("Starting populating")
    # x=users('student')
    # f = fac()
    # c = coff()
    # src=studentRegistersInCourse()
    # att = attendanceRec()
    class1()
    print("user Created")  

