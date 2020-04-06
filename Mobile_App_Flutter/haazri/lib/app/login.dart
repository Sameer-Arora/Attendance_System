import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {

  // Formatting options
  TextStyle textStyle = TextStyle(fontSize: 20.0);
  EdgeInsets padding = EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0);
  OutlineInputBorder textFieldBorder = OutlineInputBorder(borderRadius: BorderRadius.circular(32.0));

  @override
  Widget build(BuildContext context) {

    // Email Text Field
    final emailField = TextField(
      obscureText: false,
      style: textStyle,
      decoration: InputDecoration(
        contentPadding: padding,
        hintText: "Email",
        border: textFieldBorder,
      ),
    );

    // Password Text Field
    final passwordField = TextField(
      obscureText: true,
      style: textStyle,
      decoration: InputDecoration(
          contentPadding: padding,
          hintText: "Password",
          border: textFieldBorder
      ),
    );

    // Login Button
    final loginButon = Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(30.0),
      color: Color(0xff01A0C7),
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: padding,
        onPressed: () {
          Navigator.pushNamed(context, '/userType');
        },
        child: Text("Login",
            textAlign: TextAlign.center,
            style: textStyle.copyWith(
                color: Colors.white, fontWeight: FontWeight.bold)),
      ),
    );

    // Animated Text to Display
//    final logoText = SizedBox(
//      width: MediaQuery.of(context).size.width,
//      child: RotateAnimatedTextKit(
//        onTap: () {
//          Navigator.pushNamed(context, '/about');
//        },
//        text: ["Attendance", "Management App", "Haazri"],
//        textStyle: TextStyle(fontSize: 38.0, ),
//        textAlign: TextAlign.start,
//        alignment: AlignmentDirectional.topStart, // or Alignment.topLeft
//        totalRepeatCount: 10,
//      ),
//    );

    // About icon button to display
    final aboutIcon = Row(
      mainAxisAlignment: MainAxisAlignment.end,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        IconButton(
            icon: Icon(Icons.info),
            iconSize: 32,
            onPressed: (){
              Navigator.pushNamed(context, '/about');
            })
      ],
    );

    return Scaffold(
      appBar: AppBar(
        title: Text('Login',),
        backgroundColor: Colors.amber,
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                aboutIcon,
                Padding(
                  padding: EdgeInsets.all(20.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: <Widget>[

                      // To add app logo
//                  SizedBox(
//                    height: 155.0,
//                    child: Image.asset(
//                      "assets/images/appLogo.png",
//                      fit: BoxFit.contain,
//                    ),
//                  ),

                      Text('HAAZRI',
                        style: TextStyle(
                            fontSize: 32,
                            fontWeight: FontWeight.bold,
                            letterSpacing: 3,
                        ),
                      ),
                      Text('Attendance Management',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          letterSpacing: 3,
                        ),
                      ),
                      SizedBox(height: 45.0),
                      emailField,
                      SizedBox(height: 25.0),
                      passwordField,
                      SizedBox(
                        height: 35.0,
                      ),
                      loginButon,
                      SizedBox(
                        height: 15.0,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}