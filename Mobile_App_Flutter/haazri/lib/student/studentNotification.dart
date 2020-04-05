import 'package:flutter/material.dart';

class LeaveApplication {
  String subject;
  String body;
  String course;

}

class StudNotificationPage extends StatefulWidget {
  @override
  _StudNotificationPageState createState() => _StudNotificationPageState();
}

class _StudNotificationPageState extends State<StudNotificationPage> {

  // index for currently selected icon from bottom navigation bar
  // 0 for Home
  // 1 for Reports
  // 2 for Notifications
  // 3 for Leave Request
  int currentNavBarIndex = 2;

  // Temporary Course List
  List <String> courseList = [
    'CS201 : Data Structures',
    'CS301 : Alogrithms',
    'CS302 : Operating Systems',
    'CS303 : Data Base Managment',
    'CS304 : Computer Networks',
    'CS305 : Software Engineering',
    'CS306 : Computation Theory',
    'CS503 : Machine Learning',
  ];

  //List for storing Bottom Navigation Bar Routes

  List<String> studNavBarRoutes = [
    '/studentHome',
    '/studentReportList',
    '/studentNotification',
    '/studentLeaveRequest',
  ];

  // Bottom Navigation Bar Items
  List<BottomNavigationBarItem> navBarItems = [
    BottomNavigationBarItem(icon: Icon(Icons.home), title: Text('Home')),
    BottomNavigationBarItem(icon: Icon(Icons.insert_chart), title: Text('Reports')),
    BottomNavigationBarItem(icon: Icon(Icons.notifications), title: Text('Notification')),
    BottomNavigationBarItem(icon: Icon(Icons.mail), title: Text('Leave')),
  ];

  // Function to be called on clicking bottom navigation bar item
  void _onItemTapped(int index) {
    setState(() {
      Navigator.pushReplacementNamed(context, studNavBarRoutes[index]);
    });
  }

  @override
  Widget build(BuildContext context) {

    BottomNavigationBar bottomNavigationBar = BottomNavigationBar(
      currentIndex: currentNavBarIndex,
      onTap: _onItemTapped,
      items: navBarItems,
      showUnselectedLabels: true,
      selectedItemColor: Colors.amber[800],
      unselectedItemColor: Colors.black,
    );


    Widget notificationWidget = Container(
        child: Center(
          child: Text('NOTIFICATION', style: TextStyle(fontSize: 32),),
        )
    );

    return Scaffold(
      appBar: AppBar(
        title: Text('Student'),
        backgroundColor: Colors.amber,
      ),
      body: notificationWidget,
      bottomNavigationBar: bottomNavigationBar,
    );
  }
}