import 'package:PhotoTags/ui/profile_data.dart';
import 'package:flutter/material.dart';
import 'package:PhotoTags/config/app_config.dart';

class UserProfile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        children: <Widget>[
          UserAccountsDrawerHeader(
            currentAccountPicture: CircleAvatar(
              backgroundImage: AssetImage('images/cabrero.jpeg'),
            ),
            accountEmail: Text('david.cabrero@udc.es'),
            accountName: Text('David Cabrero'),
          ),
          ListTile(
            title: Text('My Profile'),
            leading: new Icon(Icons.account_circle),
            onTap: () {
              Navigator.of(context).push(
                MaterialPageRoute(
                  builder: (BuildContext context) {
                    return ProfileData();
                  },
                ),
              );
            },
          ),
          AboutListTile(
            icon: Icon(Icons.info),
            applicationName: AppConfig.of(context).title,
            aboutBoxChildren: <Widget>[
              Text('The best IA Technology'),
            ],
          ),
        ],
      ),
    );
  }
}
