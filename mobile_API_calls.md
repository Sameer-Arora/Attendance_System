## Mobile App API Calls

### Sign In

**Login credential verification:**
 
    Sent: Username, Password  
    Received: 
              { 
                status   : “valid” or “invalid”, // status is invalid if credidentials not valid
                userID   : 1234243 or -1, // if status is invalid return -1
                userType : 1,2,3 or -1,    // if status is invalid return -1
                Name   : "Harshit Malik" or "" // if status is invalid return empty string
              }
              
 ### Report

 **Course List**
 
    Note: If userType is student, return all course he is enrolled in, if usertype is faculty, return all the courses he teaches
    
    Sent: userID, userType
    Received: 
              { 
                TotalCourse   : 6,
                CourseList   : [
                                {
                                  courseID : 12331,
                                  courseName : "CS301",
                                  courseTitle : "Intro to DBMS",
                                 }, 
                                 {
                                  courseID : 12331,
                                  courseName : "CS503",
                                  courseTitle : "Machine Learning",
                                 }, 
                                 .
                                 .
                                 .
                                 ], 
                
              }
         
  **Course Details**
  
    Sent: courseID
    Received: 
              { 
              ` courseID : 12331,
                courseName : "CS503",
                courseTitle : "Machine Learning",
                Instructor : "Dr CKN",
                TotalStudentsEnrolled : 67,
                MinAttendaceRequirement : 75%,
                LectureTimings : ["Mon 9:00AM 9:50AM" ,"Tues 9:00AM 9:50AM", "Wed 9:00AM 9:50AM"] 
                TutTimigs : [" Thrus 6:00PM 6:50PM"],
                Venue : "M4 LHC"               
              }
              
 **Student Course Attendance Details**
 
    Sent: userID, userType, courseID
    Received: 
              { 
              ` Instructor : "Dr. Gunturi",
                TotalClassesSoFar   : 42,
                Present : 38,
                Leave : 1,
                Absent : 3,
                AbsentDates : ['12-04-2020', '16-04-2020', '20-04-2020'], // If we are storing these dates
                MinAttendaceRequirement : 75%,
              }
              
  **Faculty Course Attendance Details**
  
    Sent: userID, userType, courseID
    Received: 
              { 
              ` Instructor : "Dr. Gunturi",
                TotalClassesSoFar   : 42,
                MinAttendaceRequirement : 75%,
                TotalStudentsEnrolled : 67,
                TA : [
                      {
                        userID : 123123,
                        Name : "Harshit Malik",
                        EntryNumber : "2017csb1078",
                        Contact : 8587963620,
                       },
                       .
                       .
                       .
                      ],
                EnrolledStudents : [
                                    {
                                      userID : 123123,
                                      Name : "Harshit Malik",
                                      EntryNumber : "2017csb1078",
                                      Contact : 8587963620,
                                      Present : 38,
                                      Leave : 1,
                                      Absent : 3,
                                     },
                                     {
                                      userID : 123124,
                                      Name : "Hersh Dhillon",
                                      EntryNumber : "2017csb1079",
                                      Contact : 8587963620,
                                      Present : 37,
                                      Leave : 0,
                                      Absent : 5,
                                     },
                                     .
                                     .
                                    ]
                
              }
              
