import 'package:flutter/material.dart';

class AppConfig extends InheritedWidget {
  AppConfig({this.title, this.breakPoint = 600, child}) : super(child: child);

  final String title;
  final int breakPoint;

  static AppConfig of(BuildContext context) =>
      context.inheritFromWidgetOfExactType(AppConfig) as AppConfig;

  @override
  bool updateShouldNotify(AppConfig old) => false;
}
