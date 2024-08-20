package user

import (
	"encoding/json"
	"net/http"
	db "server-go/db"
)

// GetAllUsersHandler handles requests to get all users.
// @Summary Get all users
// @Description Fetch all users from the database
// @Tags user
// @Accept json
// @Produce json
// @Success 200 {array} UserModel "List of users"
// @Failure 500 {string} string "Internal server error"
// @Router /users [get]
func GetAllUsersHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		return
	}

	var users []UserModel
	result := db.DB.Preload("Info").Find(&users)
	if result.Error != nil {
		http.Error(w, "Failed to fetch users", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
	if err := json.NewEncoder(w).Encode(users); err != nil {
		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		return
	}
}
