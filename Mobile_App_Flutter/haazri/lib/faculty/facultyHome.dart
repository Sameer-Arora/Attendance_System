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

class FacultyHomePage extends StatefulWidget {
  @override
  _FacultyHomePageState createState() => _FacultyHomePageState();
}

class _FacultyHomePageState extends State<FacultyHomePage> {
  int currentNavBarIndex = 0;// index for currently selected icon from bottom navigation bar
  String photoCourseText = 'Select course'; // value to display for course in photo clicking


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

  final leaveFormKey = GlobalKey<FormState>(); // Global form key for leave application


  List<BottomNavigationBarItem> navBarItems = [
    BottomNavigationBarItem(icon: Icon(Icons.home), title: Text('Home')),
    BottomNavigationBarItem(icon: Icon(Icons.insert_chart), title: Text('Reports')),
    BottomNavigationBarItem(icon: Icon(Icons.notifications), title: Text('Notification')),
    BottomNavigationBarItem(icon: Icon(Icons.camera_alt), title: Text('Photo')),
  ];

  void _onItemTapped(int index) {
    setState(() {
      currentNavBarIndex = index;
    });
  }

  void openCamera() async{
    var picture = await ImagePicker.pickImage(
      source: ImageSource.camera,
    );
    Navigator.pushNamed(context, '/processPhoto', arguments: { 'image' : picture});
  }

  @override
  Widget build(BuildContext context) {

    _DateTime dateTime = _DateTime(DateTime.now());


    BottomNavigationBar bottomNavigationBar = BottomNavigationBar(
      currentIndex: currentNavBarIndex,
      onTap: _onItemTapped,
      items: navBarItems,
      showUnselectedLabels: true,
      selectedItemColor: Colors.amber[800],
      unselectedItemColor: Colors.black,
    );

    final openCameraButon = FlatButton.icon(
      icon: Icon(Icons.camera, color: Colors.black,),
      label: Text('Open Camera', style: TextStyle(fontSize: 20, color: Colors.black),),
      onPressed: (){ openCamera();},
      shape: RoundedRectangleBorder(
        borderRadius: new BorderRadius.circular(18.0),
        side: BorderSide(color: Colors.black, width: 2),

      ),
    );

    Widget homeWidget = Container(
        child: Center(
          child: Text('HOME', style: TextStyle(fontSize: 32),),
        )
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
                  currentNavBarIndex = 3;
                  photoCourseText = courseList[index];
                });
              },
            ),
          );
        },
      ),
    );

    Widget notificationWidget = Container(
        child: Center(
          child: Text('NOTIFICATION', style: TextStyle(fontSize: 32),),
        )
    );

    Widget photoClickWidget = Container(
      child: Padding(
          padding: EdgeInsets.symmetric(vertical: 8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Row(
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

    List<Widget> bodyWidgets = [
      homeWidget,
      reportsWidget,
      notificationWidget,
      photoClickWidget
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text('Student'),
        backgroundColor: Colors.amber,
      ),
      body: bodyWidgets[currentNavBarIndex],
      bottomNavigationBar: bottomNavigationBar,
    );
  }
}