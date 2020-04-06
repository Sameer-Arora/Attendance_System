import 'package:flutter/material.dart';

class FacultyReportListPage extends StatefulWidget {
  @override
  _FacultyReportListPageState createState() => _FacultyReportListPageState();
}

class _FacultyReportListPageState extends State<FacultyReportListPage> {

  // index for currently selected icon from bottom navigation bar
  // 0 for Home
  // 1 for Reports
  // 2 for Notifications
  // 3 for Open Camera
  int currentNavBarIndex = 1;

  //List for storing Bottom Navigation Bar Routes
  List<String> facultyNavBarRoutes = [
    '/facultyHome',
    '/facultyReportList',
    '/facultyNotification',
    '/facultyOpenCamera',
  ];

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

    Widget reportsWidget = Container(
      child: ListView.builder(
        itemCount: courseList.length,
        itemBuilder: (context, index){
          return Card(
            child: ListTile(
              trailing: Icon(Icons.keyboard_arrow_right),
              title: Text(courseList[index]),
              leading: Icon(Icons.library_books),
              onTap: (){ },
              onLongPress: (){
                setState(() {
                  Navigator.pushReplacementNamed(context, facultyNavBarRoutes.last, arguments: {'course':courseList[index]});
                });
              },
            ),
          );
        },
      ),
    );

    return Scaffold(
      appBar: AppBar(
        title: Text('Student'),
        backgroundColor: Colors.amber,
      ),
      body: reportsWidget,
      bottomNavigationBar: bottomNavigationBar,
    );
  }
}