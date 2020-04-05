import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class _DateTime{

  int day;
  int month;
  int year;
  int hour;
  int minute;
  String weekday;

  _DateTime(DateTime dateTime){
    this.day = dateTime.day;
    this.weekday = getWeekDay(dateTime.weekday);
    this.month = dateTime.month;
    this.year = dateTime.year;
    this.hour = dateTime.hour;
    this.minute = dateTime.minute;
  }

  String getDate(){
    return '${this.day} ${getMonth(this.month)} ${this.year}';
  }

  String getTime(){
    return '${this.hour} : ${this.minute}';
  }

  String getWeekDay(int weekday){
    switch(weekday){
      case 1: return 'Monday';
      case 2: return 'Tuesday';
      case 3: return 'Wednesday';
      case 4: return 'Thrusday';
      case 5: return 'Friday';
      case 6: return 'Saturday';
      case 7: return 'Sunday';

    }
  }

  String getMonth(int month){
    switch(month){
      case 1: return 'January';
      case 2: return 'February';
      case 3: return 'March';
      case 4: return 'April';
      case 5: return 'May';
      case 6: return 'June';
      case 7: return 'July';
      case 8: return 'August';
      case 9: return 'September';
      case 10: return 'October';
      case 11: return 'November';
      case 12: return 'December';
    }
  }
}

class FacultyOpenCamPage extends StatefulWidget {
  @override
  _FacultyOpenCamPageState createState() => _FacultyOpenCamPageState();
}

class _FacultyOpenCamPageState extends State<FacultyOpenCamPage> {

  // index for currently selected icon from bottom navigation bar
  // 0 for Home
  // 1 for Reports
  // 2 for Notifications
  // 3 for Open Camera
  int currentNavBarIndex = 3;

  // Text to display for course section in photo clicking screen
  String photoCourseText = 'Select course';

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

  // Function to take picture from Camera
  void openCamera() async{
    var picture = await ImagePicker.pickImage(
      source: ImageSource.camera,
    );
    Navigator.pushNamed(context, '/processPhoto', arguments: { 'image' : picture});
  }

  @override
  Widget build(BuildContext context) {

    Map passedData = ModalRoute.of(context).settings.arguments;
    if(passedData != null){
      photoCourseText = passedData['course'];
    }

    _DateTime dateTime = _DateTime(DateTime.now());

    BottomNavigationBar bottomNavigationBar = BottomNavigationBar(
      currentIndex: currentNavBarIndex,
      onTap: _onItemTapped,
      items: navBarItems,
      showUnselectedLabels: true,
      selectedItemColor: Colors.amber[800],
      unselectedItemColor: Colors.black,
    );

    // Open Camera Button Design
    final openCameraButon = FlatButton.icon(
      icon: Icon(Icons.camera, color: Colors.black,),
      label: Text('Open Camera', style: TextStyle(fontSize: 20, color: Colors.black),),
      onPressed: (){ openCamera();},
      shape: RoundedRectangleBorder(
        borderRadius: new BorderRadius.circular(18.0),
        side: BorderSide(color: Colors.black, width: 2),
      ),
    );

    Widget photoClickWidget = Container(
      child: Padding(
          padding: EdgeInsets.symmetric(vertical: 8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: <Widget>[
                    PopupMenuButton<String>(
                      initialValue: courseList[0],
                      onSelected: (value){
                        setState(() {
                          photoCourseText = value;
                        });
                      },
                      itemBuilder: (context){
                        return courseList.map((String course){
                          return PopupMenuItem(
                            value: course,
                            child: Text(course),
                          );
                        }).toList();
                      },
                    ),
                    Text(photoCourseText, style: TextStyle(fontSize: 24),),
                  ],
                ),
              ),
              Column(
                children: <Widget>[
                  Text(dateTime.getTime(), style: TextStyle(fontSize: 40, letterSpacing: 4, fontWeight: FontWeight.bold, color: Colors.red),),
                  Text('${dateTime.weekday}, ${dateTime.getDate()}', style: TextStyle(fontSize: 24),),
                ],
              ),
              Column(
                children: <Widget>[
                  Text('VENUE', style: TextStyle(fontSize: 32, letterSpacing: 3),),
                  SizedBox(height: 10,),
                  Text('L4, LHC', style: TextStyle(fontSize: 26, letterSpacing: 2, fontWeight: FontWeight.bold),),
                ],
              ),
              openCameraButon,
            ],
          )
      ),
    );

   return Scaffold(
      appBar: AppBar(
        title: Text('Student'),
        backgroundColor: Colors.amber,
      ),
      body: photoClickWidget,
      bottomNavigationBar: bottomNavigationBar,
    );
  }
}