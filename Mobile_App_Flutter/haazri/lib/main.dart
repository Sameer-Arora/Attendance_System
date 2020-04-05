import 'package:flutter/material.dart';

import 'app/about.dart';
import 'app/userType.dart';
import 'app/login.dart';

import 'faculty/facultyHome.dart';
import 'faculty/processPhoto.dart';

import 'student/studentHome.dart';

void main() => runApp(AppMain());

class AppMain extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/', // Defines initial route to load on app startup
      routes: {
        '/': (context)=>LoginPage(),
        '/about': (context)=>AboutPage(),
        '/userType':(context)=>UserTypePage(),

        // Student Routes
        '/studentHomePage':(context)=> StudentHomePage(),

        // Faculty Routes
        '/facultyHomePage':(context)=> FacultyHomePage(),
        '/processPhoto' : (context)=> ShowImage(),
      },
    );
  }
}