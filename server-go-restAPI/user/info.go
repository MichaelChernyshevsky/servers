package user

import (
	"fmt"
	"net/http"
)

type RequestInfoUserModel struct {
	UserModelId string `json:"UserModelId"`
}

func InfoHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "UserModel endpoint")
}
