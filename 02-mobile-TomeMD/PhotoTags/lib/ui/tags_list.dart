import 'package:PhotoTags/ui/profile_data.dart';
import 'package:flutter/material.dart';
import 'package:PhotoTags/models/json_to_dart.dart';
import 'package:PhotoTags/blocs/tags_bloc.dart';
import 'package:PhotoTags/ui/show_camera.dart';

import 'package:PhotoTags/ui/app.dart';

class TagsList extends StatelessWidget {
  final imageFile;

  const TagsList({Key key, this.imageFile}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    bloc.fetchAllTags(imageFile);
    return StreamBuilder(
      stream: bloc.allTags,
      builder: (context, AsyncSnapshot<List<TagElement>> snapshot) {
        if (snapshot.hasData) {
          return buildList(snapshot, context);
        } else if (snapshot.hasError) {
          return Center(
            child: SingleChildScrollView(
              child: Column(
                children: <Widget>[
                  Image.asset('images/error.gif'),
                  Text('There was a network error'),
                ],
              ),
            ),
          );
        }
        return Center(child: CircularProgressIndicator());
      },
    );
  }

  Widget buildList(
      AsyncSnapshot<List<TagElement>> snapshot, BuildContext context) {
    var _index = 0;

    final TextStyle titleStyle = TextStyle(
        fontSize: Theme.of(context).textTheme.bodyText1.fontSize,
        fontStyle: Theme.of(context).textTheme.bodyText1.fontStyle);
    final TextStyle subtitleStyle = TextStyle(
        fontSize: Theme.of(context).textTheme.subtitle1.fontSize,
        fontStyle: Theme.of(context).textTheme.subtitle1.fontStyle);
    return Scaffold(
      appBar: AppBar(
        title: Text("Image Tags"),
      ),
      body: ListView.builder(
        itemCount: snapshot.data.length,
        itemBuilder: (BuildContext context, int i) => ListTile(
          title: Text(snapshot.data[i].tag.en, style: titleStyle),
          subtitle: Text(snapshot.data[i].confidence.toString(),
              style: subtitleStyle),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.home),
              // ignore: deprecated_member_use
              title: Text(
                "Home",
                style: TextStyle(fontSize: 20),
              )),
          BottomNavigationBarItem(
              icon: Icon(Icons.add_a_photo_sharp),
              // ignore: deprecated_member_use
              title: Text(
                "New Photo",
                style: TextStyle(fontSize: 20),
              )),
          BottomNavigationBarItem(
              icon: Icon(Icons.collections),
              backgroundColor: Colors.purple,
              // ignore: deprecated_member_use
              title: Text(
                "Gallery",
                style: TextStyle(fontSize: 20),
              )),
          BottomNavigationBarItem(
              icon: CircleAvatar(
                backgroundImage: AssetImage('images/cabrero.jpeg'),
              ),
              // ignore: deprecated_member_use
              title: Text(
                "User",
                style: TextStyle(fontSize: 20),
              )),
        ],
        onTap: (index) {
          _index = index;
          _navigateToScreens(context, index);
        },
        currentIndex: _index,
        type: BottomNavigationBarType.fixed,
        iconSize: 40,
      ),
    );
  }

  void _navigateToScreens(BuildContext context, var index) {
    if (index == 0) {
      Navigator.of(context).push(
        MaterialPageRoute(
          builder: (BuildContext context) {
            return PhotoTagsApp();
          },
        ),
      );
    } else if (index == 1) {
      Camera.getImage(context);
    }
    else if (index == 2) {
      Camera.openGallery(context);
    } else {
      Navigator.of(context).push(
          MaterialPageRoute(
            builder: (BuildContext context) {
              return ProfileData();
              },
          )
      );
    }
    }
  }

