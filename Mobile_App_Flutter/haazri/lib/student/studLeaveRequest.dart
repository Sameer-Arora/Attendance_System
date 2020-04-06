import 'package:flutter/material.dart';

class LeaveApplication {
  String subject;
  String body;
  String course;

}

class StudentLeaveRqstPage extends StatefulWidget {
  @override
  _StudentLeaveRqstPageState createState() => _StudentLeaveRqstPageState();
}

class _StudentLeaveRqstPageState extends State<StudentLeaveRqstPage> {


  // index for currently selected icon from bottom navigation bar
  // 0 for Home
  // 1 for Reports
  // 2 for Notifications
  // 3 for Leave Request
  int currentNavBarIndex = 3;

  // value to display for course in leave application
  String leaveCourseText = 'Select course';

  // Class object to store leave apllication data
  LeaveApplication leaveApplication = LeaveApplication();


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

  // Global form key for accessing leave application
  final leaveFormKey = GlobalKey<FormState>();

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

    Map passedData = ModalRoute.of(context).settings.arguments;
    if(passedData != null){
      leaveCourseText = passedData['course'];
    }

    BottomNavigationBar bottomNavigationBar = BottomNavigationBar(
      currentIndex: currentNavBarIndex,
      onTap: _onItemTapped,
      items: navBarItems,
      showUnselectedLabels: true,
      selectedItemColor: Colors.amber[800],
      unselectedItemColor: Colors.black,
    );

    Widget leaveApplicationWidget = SingleChildScrollView(
      child: Container(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Form(
            key: leaveFormKey,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children: <Widget>[
                      PopupMenuButton<String>(
                        initialValue: courseList[0],
                        onSelected: (value){
                          setState(() {
                            leaveApplication.course = value;
                            leaveCourseText = value;
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
                      Text(leaveCourseText),
                    ],
                  ),
                ),
                TextFormField(
                  decoration: InputDecoration(
                    labelText: 'Subject',
                  ),
                  validator: (value){
                    if(value.isEmpty){
                      return 'Please fill this field';
                    }
                    return null;
                  },
                  onSaved: (value){
                    leaveApplication.subject = value;
                  },
                ),
                TextFormField(
                  maxLines: 15,
                  decoration: InputDecoration(
                    labelText: 'Message',
                  ),
                  validator: (value){
                    if(value.isEmpty){
                      return 'Please fill this field';
                    }
                    return null;
                  },
                  onSaved: (value){
                    leaveApplication.body = value;
                  },
                ),
                Center(
                  child: FlatButton.icon(
                    icon: Icon(Icons.attach_file,),
                    label: Text('Attach File', style: TextStyle(fontSize: 18),),
                    onPressed: (){

                    },
                  ),
                ),
                Center(
                  child: FlatButton.icon(
                    icon: Icon(Icons.send,),
                    label: Text('Send Application', style: TextStyle(fontSize: 18),),
                    onPressed: (){
                      final form = leaveFormKey.currentState;
                      if(form.validate()){
                        form.save();
                        print(leaveApplication.course);
                        print(leaveApplication.subject);
                        print(leaveApplication.body);
                        //Do processing and show processing bar
                      }
                    },
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );

    return Scaffold(
      appBar: AppBar(
        title: Text('Student'),
        backgroundColor: Colors.amber,
      ),
      body: leaveApplicationWidget,
      bottomNavigationBar: bottomNavigationBar,
    );
  }
}