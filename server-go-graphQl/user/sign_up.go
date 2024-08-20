package user

import (
	"encoding/json"
	"net/http"
	db "server-go/db"
)

// RequestSignUp represents the sign-up request payload.
type RequestSignUp struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

// SignUpHandler handles user sign-up requests.
// @Summary Sign up a new user
// @Description Create a new user with email and password
// @Tags user
// @Accept json
// @Produce json
// @Param request body RequestSignUp true "Sign up request"
// @Success 201 {object} UserModel "User created"
// @Failure 400 {string} string "Invalid request"
// @Failure 500 {string} string "Internal server error"
// @Router /signup [post]

func SignUpHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		return
	}

	var request RequestSignUp
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	newUser := UserModel{
		Email:    request.Email,
		Password: request.Password,
		Phone:    "",
		// Packages:   1,
		Info: InfoModel{
			Sex:     "",
			Name:    "",
			Name2:   "",
			Age:     30,
			Admin:   false,
			Creator: false,
		},
		Subscribed: false,
	}

	result := db.DB.Create(&newUser)
	if result.Error != nil {
		http.Error(w, "Failed to create user", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	if err := json.NewEncoder(w).Encode(newUser); err != nil {
		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		return
	}
}
