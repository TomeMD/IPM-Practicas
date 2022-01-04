import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:PhotoTags/models/json_to_dart.dart';

class TagsApiProvider {
  Future<List<TagElement>> getTags(imageFile) async {
    final response = await httpPost(imageFile);
    var _tags = List<TagElement>();

    if (response.statusCode == 200) {
      List data = json.decode(response.body)['result']['tags'];
      for (var tag in data) {
        _tags.add(TagElement.fromJson(tag));
      }
    } else {
      throw Exception(
          'Failed to load post $response.statusCode' + response.body);
    }
    return _tags;
  }

  Future<http.Response> httpPost(File imageFile) {
    return http.post(
      'https://api.imagga.com/v2/tags',
      headers: {
        HttpHeaders.authorizationHeader:
            "Basic YWNjX2IzZDJhNTg5NWE2ZWIyZjoxNmVjNjg2NzFmNWI5ZDRjMTczNGU4NWQ3MWZiMDBiZQ=="
      },
      body: {"image_base64": base64Encode(imageFile.readAsBytesSync())},
    );
  }
}
