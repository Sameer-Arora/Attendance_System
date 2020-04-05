import 'package:flutter/material.dart';

class LeaveApplication {
  String subject;
  String body;
  String course;

}

class StudentHomePage extends StatefulWidget {
  @override
  _StudentHomePageState createState() => _StudentHomePageState();
}

class _StudentHomePageState extends State<StudentHomePage> {

  int currentNavBarIndex = 0; // index for currently selected icon from bottom navigation bar
  String leaveCourseText = 'Select course'; // value to display for course in leave application
  LeaveApplication leaveApplication = LeaveApplication(); // Class object to store leave apllication data

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
    BottomNavigationBarItem(icon: Icon(Icons.mail), title: Text('Leave')),
  ];

  void _onItemTapped(int index) {
    setState(() {
      currentNavBarIndex = index;
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
                  leaveApplication.course = courseList[index];
                  leaveCourseText = courseList[index];
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
                Row(
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

    List<Widget> bodyWidgets = [
      homeWidget,
      reportsWidget,
      notificationWidget,
      leaveApplicationWidget
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