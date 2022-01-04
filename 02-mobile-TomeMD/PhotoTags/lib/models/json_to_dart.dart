import 'dart:convert';

Welcome welcomeFromJson(String str) => Welcome.fromJson(json.decode(str));

String welcomeToJson(Welcome data) => json.encode(data.toJson());

class Welcome {
  Welcome({
    this.result,
    this.status,
  });

  Result result;
  Status status;

  factory Welcome.fromJson(Map<String, dynamic> json) => Welcome(
        result: Result.fromJson(json["result"]),
        status: Status.fromJson(json["status"]),
      );

  Map<String, dynamic> toJson() => {
        "result": result.toJson(),
        "status": status.toJson(),
      };
}

class Result {
  Result({
    this.tags,
  });

  List<TagElement> tags;

  factory Result.fromJson(Map<String, dynamic> json) => Result(
        tags: List<TagElement>.from(
            json["tags"].map((x) => TagElement.fromJson(x))),
      );

  Map<String, dynamic> toJson() => {
        "tags": List<dynamic>.from(tags.map((x) => x.toJson())),
      };
}

class TagElement {
  TagElement({
    this.confidence,
    this.tag,
  });

  double confidence;
  TagTag tag;

  factory TagElement.fromJson(Map<String, dynamic> json) => TagElement(
        confidence: json["confidence"].toDouble(),
        tag: TagTag.fromJson(json["tag"]),
      );

  Map<String, dynamic> toJson() => {
        "confidence": confidence,
        "tag": tag.toJson(),
      };
}

class TagTag {
  TagTag({
    this.en,
  });

  String en;

  factory TagTag.fromJson(Map<String, dynamic> json) => TagTag(
        en: json["en"],
      );

  Map<String, dynamic> toJson() => {
        "en": en,
      };
}

class Status {
  Status({
    this.text,
    this.type,
  });

  String text;
  String type;

  factory Status.fromJson(Map<String, dynamic> json) => Status(
        text: json["text"],
        type: json["type"],
      );

  Map<String, dynamic> toJson() => {
        "text": text,
        "type": type,
      };
}
