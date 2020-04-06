import 'package:flutter/material.dart';

class ShowImage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {

    Map image = ModalRoute.of(context).settings.arguments;

    return Scaffold(
      appBar: AppBar(
        title: Text('Image Clicked'),
        backgroundColor: Colors.amber,
      ),
      body: Center(
        child: image == null
            ? Text('No image selected.')
            : Image.file(image['image']),
      ),
    );
  }
}