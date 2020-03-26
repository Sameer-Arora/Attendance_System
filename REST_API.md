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


