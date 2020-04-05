import 'package:flutter/material.dart';

import 'app/about.dart';
import 'app/userType.dart';
import 'app/login.dart';

import 'faculty/facultyHome.dart';
import 'faculty/facultyReportList.dart';
import 'faculty/facultyNotification.dart';
import 'faculty/facultyOpenCamera.dart';
import 'faculty/processPhoto.dart';

import 'student/studentHome.dart';
import 'student/studReportList.dart';
import 'student/studentNotification.dart';
import 'student/studLeaveRequest.dart';

void main() => runApp(AppMain());

class AppMain extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/', // Defines initial route to load on app startup
      routes: {

        //Main App Routes
        '/': (context)=>LoginPage(),
        '/about': (context)=>AboutPage(),
        '/userType': (context)=>UserTypePage(),

        // Student Routes
        '/studentHome': (context)=> StudHomePage(),
        '/studentReportList': (context)=> StudReportListPage(),
        '/studentNotification': (context)=> StudNotificationPage(),
        '/studentLeaveRequest': (context)=> StudentLeaveRqstPage(),

        // Faculty Routes
        '/facultyHome': (context)=> FacultyHomePage(),
        '/facultyReportList': (context)=> FacultyReportListPage(),
        '/facultyNotification': (context)=> FacultyNotificationPage(),
        '/facultyOpenCamera': (context)=> FacultyOpenCamPage(),
        '/processPhoto': (context)=> ShowImage(),
      },
    );
  }
}