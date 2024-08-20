package main

import (
	"fmt"
	"net/http"
	"server-go/db"
	_ "server-go/docs"

	httpSwagger "github.com/swaggo/http-swagger"
	// packages
	user "server-go/user"
)

// @title Timefill API Go
// @version 2.0
// @description This is a server server
// @termsOfService http://swagger.io/terms/
// @contact.name Timefill Api
// @contact.url http://www.swagger.io/support
// @contact.email support@swagger.io
// @license.name Apache 2.0
// @license.url http://www.apache.org/licenses/LICENSE-2.0.html
// @host localhost:8000
// @BasePath /

func main() {
	// db
	if err := db.Init(); err != nil {
		fmt.Println("Error connecting to database:", err)
		return
	}
	// api
	user.Register()
	http.Handle("/swagger/", httpSwagger.WrapHandler)
	fmt.Println("Swagger: http://localhost:8080/swagger/index.html")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}

}
