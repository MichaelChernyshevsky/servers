package user

import (
	"fmt"
	"net/http"
)

type RequestDeleteUserModel struct {
	UserModelId string `json:"UserModelId"`
}

func DeleteHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "UserModel endpoint")
}
