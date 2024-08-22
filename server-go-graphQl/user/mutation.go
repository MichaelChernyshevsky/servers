package user

import (
	"fmt"

	"github.com/graphql-go/graphql"
)

var mutationType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Mutation",
	Fields: graphql.Fields{
		"createUser": &graphql.Field{
			Type:        userType,
			Description: "Create new user",
			Args: graphql.FieldConfigArgument{
				"username": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.String),
				},
				"age": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.Int),
				},
				"phone": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.String),
				},
				"email": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.String),
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				user := User{
					ID:       fmt.Sprintf("%d", nextID),
					Username: params.Args["username"].(string),
					Age:      params.Args["age"].(int),
					Phone:    params.Args["phone"].(string),
					Email:    params.Args["email"].(string),
				}
				nextID++
				userList = append(userList, user)
				return user, nil
			},
		},
		"editUser": &graphql.Field{
			Type:        userType,
			Description: "Edit existing user",
			Args: graphql.FieldConfigArgument{
				"id": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.String),
				},
				"username": &graphql.ArgumentConfig{
					Type: graphql.String,
				},
				"age": &graphql.ArgumentConfig{
					Type: graphql.Int,
				},
				"phone": &graphql.ArgumentConfig{
					Type: graphql.String,
				},
				"email": &graphql.ArgumentConfig{
					Type: graphql.String,
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				id := params.Args["id"].(string)
				for i, user := range userList {
					if user.ID == id {
						if username, ok := params.Args["username"].(string); ok {
							user.Username = username
						}
						if age, ok := params.Args["age"].(int); ok {
							user.Age = age
						}
						if phone, ok := params.Args["phone"].(string); ok {
							user.Phone = phone
						}
						if email, ok := params.Args["email"].(string); ok {
							user.Email = email
						}
						userList[i] = user
						return user, nil
					}
				}
				return nil, nil
			},
		},
		"deleteUser": &graphql.Field{
			Type:        userType,
			Description: "Delete user",
			Args: graphql.FieldConfigArgument{
				"id": &graphql.ArgumentConfig{
					Type: graphql.NewNonNull(graphql.String),
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				id := params.Args["id"].(string)
				for i, user := range userList {
					if user.ID == id {
						userList = append(userList[:i], userList[i+1:]...)
						return user, nil
					}
				}
				return nil, nil
			},
		},
	},
})
