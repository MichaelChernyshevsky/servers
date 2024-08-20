package user

import (
	"fmt"
	"net/http"
)

func SignOutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "UserModel endpoint")
}
