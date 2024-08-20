package user

import (
	"encoding/json"
	"net/http"
)

type RequestSignIn struct {
	UserModelname string `json:"email"`
	Password string `json:"password"`
}

func SignInHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		return
	}

	var request RequestSignIn
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
}
