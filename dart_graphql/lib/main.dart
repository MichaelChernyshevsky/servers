import 'package:dart_graphql/service.dart';

void main() async {
  final graphqlService = GraphQLService();

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
}
