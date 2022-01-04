import 'dart:async';
import 'package:PhotoTags/resources/tags_api_provider.dart';
import 'package:PhotoTags/models/json_to_dart.dart';

class Repository {
  final tagsApiProvider = TagsApiProvider();

  Future<List<TagElement>> fetchAllTags(imageFile) =>
      tagsApiProvider.getTags(imageFile);
}
