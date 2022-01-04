import 'package:flutter/material.dart';
import 'package:PhotoTags/config/app_config.dart';
import 'package:PhotoTags/ui/user_profile.dart';
import 'package:PhotoTags/ui/show_camera.dart';

import 'show_camera.dart';

class VerticalScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final TextStyle fontStyle = TextStyle(
        fontSize: Theme.of(context).textTheme.headline5.fontSize,
        fontWeight: FontWeight.bold);
    return Scaffold(
      appBar: AppBar(
        title: Text(AppConfig.of(context).title),
      ),
      drawer: UserProfile(),
      body: Container(
          child: Column(mainAxisAlignment: MainAxisAlignment.start, children: [
        Image.asset("images/background.jpg"),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
              '¡Use our photo tagging technology! Press the button '
              'below to start',
              style: fontStyle,
              textAlign: TextAlign.center),
        ),
      ])),
      persistentFooterButtons: <Widget>[
        RaisedButton(
        color: Colors.purple,
        onPressed: () => Camera.openGallery(context),
        child: const Icon(Icons.collections, size: 40.0),
      ),
        const SizedBox(width: 10,),
        RaisedButton(
          color: Colors.purple,
          onPressed: () => Camera.getImage(context),
          child: const Icon(Icons.add_a_photo, size: 40.0),
        ),
        const SizedBox(width: 10,),
      ],

      backgroundColor: Colors.blueGrey.shade200,
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
    );
  }
}
