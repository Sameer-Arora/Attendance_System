import 'package:flutter/material.dart';

class UserTypePage extends StatefulWidget {
  @override
  _UserTypePageState createState() => _UserTypePageState();
}

class _UserTypePageState extends State<UserTypePage> {

  Widget getUserTypeBtn(String userType, String routeName){
    Widget userTypeBtn = Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(30.0),
      color: Color(0xff01A0C7),
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
        onPressed: () {
          Navigator.pushNamed(context, routeName);
        },
        child: Text(userType,
            textAlign: TextAlign.center,
            style: TextStyle(
                fontSize: 20,
                color: Colors.white,
                fontWeight: FontWeight.bold)),
      ),
    );

    return userTypeBtn;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Type'),
        backgroundColor: Colors.amber,
      ),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            getUserTypeBtn('Student', '/studentHome'),
            SizedBox(height: 20,),
            getUserTypeBtn('Faculty', '/facultyHome'),
          ],
        ),

      ),
    );
  }
}