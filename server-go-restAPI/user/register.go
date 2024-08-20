package user

import (
	"net/http"
	db "server-go/db"
)

func Register() {
	http.HandleFunc("/UserModel", Handler)
	http.HandleFunc("/signin", SignInHandler)
	http.HandleFunc("/signup", SignUpHandler)
	http.HandleFunc("/signout", SignOutHandler)
	http.HandleFunc("/delete", DeleteHandler)
	http.HandleFunc("/users", GetAllUsersHandler)
	http.HandleFunc("/user", GetUserByIDHandler)

	db.DB.AutoMigrate(&UserModel{})
	db.DB.AutoMigrate(&InfoModel{})

}
