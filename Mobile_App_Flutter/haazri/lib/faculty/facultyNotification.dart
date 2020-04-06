import 'package:flutter/material.dart';

class FacultyNotificationPage extends StatefulWidget {
  @override
  _FacultyNotificationPageState createState() => _FacultyNotificationPageState();
}

class _FacultyNotificationPageState extends State<FacultyNotificationPage> {

  // index for currently selected icon from bottom navigation bar
  // 0 for Home
  // 1 for Reports
  // 2 for Notifications
  // 3 for Open Camera
  int currentNavBarIndex = 2;

  //List for storing Bottom Navigation Bar Routes
  List<String> facultyNavBarRoutes = [
    '/facultyHome',
    '/facultyReportList',
    '/facultyNotification',
    '/facultyOpenCamera',
  ];

  // Bottom Navigation Bar Items
  List<BottomNavigationBarItem> navBarItems = [
    BottomNavigationBarItem(icon: Icon(Icons.home), title: Text('Home')),
    BottomNavigationBarItem(icon: Icon(Icons.insert_chart), title: Text('Reports')),
    BottomNavigationBarItem(icon: Icon(Icons.notifications), title: Text('Notification')),
    BottomNavigationBarItem(icon: Icon(Icons.camera_alt), title: Text('Photo')),
  ];

  // Function to be called on clicking bottom navigation bar item
  void _onItemTapped(int index) {
    setState(() {
      Navigator.pushReplacementNamed(context, facultyNavBarRoutes[index]);
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