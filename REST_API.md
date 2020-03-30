# :scroll: REST API DESIGN DOCUMENT
A dcoumentation pertaining the api desgin to be followed in the project.
Everywhere to keep the api uniform using plural form for each of the resource.

## Sections
- [Resources Identified](#Resources-Identified-For-API) 
- [Main Endpoints Exposed](#Endpoints-Exposed)
- [Querying Resources](#Querying-Resources-Identified )
- [Updating Resources](#Updating-Resources-Identified)

## Resources Identified For API
### Primary Resources
- courses  /api/course
- users  /api/user
- student  /api/student
- faculty  /api/faculty
- TA  /api/TA

### Secondary Resources
- /api/student/course
- /api/faculty/course
- /api/TA/course
- /api/student/course/date
- /api/faculty/course/date
- /api/TA/course/date
- /api/faculty/course/date/media
- /api/TA/course/date/media

## Endpoints Exposed
- 

## Querying Resources Identified 
- GET /api/course
- GET /api/courses
- GET /api/user
- GET /api/users
- Simlarily Others..

## Updating Resources Identified
- PUT /api/course
- PUT /api/courses
- PUT /api/user
- PUT /api/users
- Simlarily Others..


## API calls from frontend
1. Sign-in page
    - PUT credentials (username, password)
    - GET status (correct or incorrect)

2. Display for Courses Studying
    1. Obtain list of courses studying
        - PUT username
        - GET list[courses]
    2. Attendance data for 1 course
        - PUT username + course_id
        - GET attendance data (days absent, days present, last 5 classes maybe)

3. Display for Courses Teaching (Instructors and TA)
    1. Obtain list of courses teaching
        - PUT username
        - GET list[coursesTeaching]
    2. Attendance data for the class
        - PUT username + course_id
        - GET attendance data
    3. Report for a class
        - PUT username + course_id
        - GET detailed report generated (table output maybe, can be downloaded as excel file)

4. Notifications
    1. List of last n notifications
        - PUT username
        - GET list[notifications] of size n feteched along with courses.
    2. Send Notification/Requests*
    3. Accept Request*
    4. Reject Request*
