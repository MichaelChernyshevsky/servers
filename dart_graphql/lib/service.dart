import 'package:graphql/client.dart';

class GraphQLService {
  final String _apiUrl = 'http://localhost:8080/graphql';

  GraphQLClient _client() {
    final Link link = HttpLink(_apiUrl);

    return GraphQLClient(
      cache: GraphQLCache(store: InMemoryStore()),
      link: link,
    );
  }

  Future<QueryResult> query(String query) async {
    final options = QueryOptions(
      document: gql(query),
    );

    final result = await _client().query(options);
    return result;
  }

  Future<QueryResult> mutate(String mutation) async {
    final options = MutationOptions(
      document: gql(mutation),
    );

    final result = await _client().mutate(options);
    return result;
  }
}
