import 'package:flutter/material.dart';

class AboutPage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('About',),
        backgroundColor: Colors.amber,
      ),
      body: Container(
          width: MediaQuery.of(context).size.width,
          child: Padding(
              padding: EdgeInsets.all(10.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  Text('Software Engineering Project', style: TextStyle(fontSize: 22),),
                  SizedBox( height: 15,),
                  Text('Haazri', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),),
                  SizedBox( height: 10,),
                  Text('Attendance Managment', style: TextStyle(fontSize: 22,),),
                  SizedBox( height: 15,),
                  Text('Team Members', style: TextStyle(fontSize: 20),),
                  SizedBox( height: 10,),
                  Text('Akansha Singh', style: TextStyle(fontSize: 20),),
                  Text('Harshit Malik', style: TextStyle(fontSize: 20),),
                  Text('Hersh Dhillon', style: TextStyle(fontSize: 20),),
                  Text('Sameer Arora', style: TextStyle(fontSize: 20),),
                  SizedBox( height: 15,),
                  Text('Under the Guidance of', style: TextStyle(fontSize: 20),),
                  Text('Dr. Balwinder Sodhi', style: TextStyle(fontSize: 20),),
                  Text('at IIT Ropar', style: TextStyle(fontSize: 20),),
                ],
              )
          )
      ),
    );
  }
}