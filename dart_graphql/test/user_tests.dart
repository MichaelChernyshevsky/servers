import 'package:dart_graphql/service.dart';
import 'package:test/scaffolding.dart';

void main() async {
  final graphqlService = GraphQLService();

  test('Create', () async {
    const mutation = '''
  mutation {
    createUser(username: "JohnDoe", age: 30, phone: "1234567890", email: "johndoe@example.com") {
      id
      username
      age
      phone
      email
    }
  }
''';

    final result = await graphqlService.mutate(mutation);

    if (result.hasException) {
      print('Error: ${result.exception.toString()}');
    } else {
      print('User Created: ${result.data}');
    }
  });
  test('Get by id', () async {
    const userId = '1';
    final query = '''
    query {
      user(id: "$userId") {
        id
        username
        age
        phone
        email
      }
    }
  ''';

    final result = await graphqlService.query(query);

    if (result.hasException) {
      print('Error: ${result.exception.toString()}');
    } else {
      print('User Data: ${result.data}');
    }
  });
}
