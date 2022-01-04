import 'package:rxdart/rxdart.dart';
import 'package:PhotoTags/resources/repository.dart';
import 'package:PhotoTags/models/json_to_dart.dart';

class TagsBloc {
  final _repository = Repository();
  final _tagsFetcher = PublishSubject<List<TagElement>>();

  Observable<List<TagElement>> get allTags => _tagsFetcher.stream;

  fetchAllTags(imageFile) async {
    List<TagElement> tags = await _repository.fetchAllTags(imageFile);
    _tagsFetcher.sink.add(tags);
  }

  dispose() {
    _tagsFetcher.close();
  }
}

final bloc = TagsBloc();
