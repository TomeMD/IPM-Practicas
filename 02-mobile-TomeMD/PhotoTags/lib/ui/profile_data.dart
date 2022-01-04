import 'package:flutter/material.dart';
import 'package:PhotoTags/config/app_config.dart';

class ProfileData extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("My Profile"),
        ),
        body: new ListView(children: [
          new ListTile(
            title: Text('Name'),
            subtitle: new Text('David'),
            leading: new Icon(Icons.account_box_rounded),
          ),
          new ListTile(
            title: Text('Surname'),
            subtitle: new Text('Cabrero'),
            leading: new Icon(Icons.account_box_outlined),
          ),
          new ListTile(
            title: Text('Address'),
            subtitle: new Text('C/ Emilia Pardo Bazán, 11'),
            leading: new Icon(Icons.map),
          ),
          new ListTile(
            title: Text('Email'),
            subtitle: new Text('david.cabrero@udc.es'),
            leading: new Icon(Icons.markunread),
          ),
          new ListTile(
            title: Text('Phone Number'),
            subtitle: new Text('981 54 23 19'),
            leading: new Icon(Icons.phone),
          ),
        ]));
  }
}