import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:PhotoTags/ui/tags_list.dart';

class Camera {
  static void openGallery(BuildContext context) async {
    File imageFile;

    try {
      var picture = await ImagePicker.pickImage(source: ImageSource.gallery);
      imageFile = picture;
      if (imageFile != null) {
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (BuildContext context) {
              return TagsList(imageFile: imageFile);
            },
          ),
        );
      }
    } catch (e) {
      print(e);
    }
  }
  static Future getImage(BuildContext context) async {
    final picker = ImagePicker();
    File imageFile;

    var picture = await picker.getImage(source: ImageSource.camera);

    try {
      if (picture != null) {
        imageFile = File(picture.path);
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (BuildContext context) {
              return TagsList(imageFile: imageFile);
            },
          ),
        );
      }
    } catch (e) {
      print(e);
    }
  }
}
