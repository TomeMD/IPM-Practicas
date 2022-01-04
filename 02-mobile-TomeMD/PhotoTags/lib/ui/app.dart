import 'package:PhotoTags/ui/horizontal_screen.dart';
import 'package:PhotoTags/ui/vertical_screen.dart';
import 'package:flutter/material.dart';

import 'package:PhotoTags/config/app_config.dart';

class PhotoTagsApp extends StatelessWidget {
  final String title;

  PhotoTagsApp({
    this.title = "PhotoTags App",
  });

  @override
  Widget build(BuildContext context) {
    return AppConfig(
      title: title,
      child: MaterialApp(
          title: title,
          theme: ThemeData(
            primarySwatch: Colors.purple,
            visualDensity: VisualDensity.adaptivePlatformDensity,
          ),
          home: Orientacion()),
    );
  }
}

class Orientacion extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: OrientationBuilder(
        // ignore: missing_return
        builder: (context, orientation) {
          if (orientation == Orientation.portrait) {
            return VerticalScreen();
          } else {
            return HorizontalScreen();
          }
        },
      ),
    );
  }
}
