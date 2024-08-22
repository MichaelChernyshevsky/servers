package user

import "github.com/graphql-go/graphql"

var queryType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Query",
	Fields: graphql.Fields{
		"user": &graphql.Field{
			Type:        userType,
			Description: "Get single user",
			Args: graphql.FieldConfigArgument{
				"id": &graphql.ArgumentConfig{
					Type: graphql.String,
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				id, ok := params.Args["id"].(string)
				if ok {
					for _, user := range userList {
						if user.ID == id {
							return user, nil
						}
					}
				}
				return nil, nil
			},
		},
		"list": &graphql.Field{
			Type:        graphql.NewList(userType),
			Description: "Get all users",
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				return userList, nil
			},
		},
	},
})
