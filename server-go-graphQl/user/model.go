package user

type User struct {
	ID       string `json:"id"`
	Username string `json:"username"`
	Age      int    `json:"age"`
	Phone    string `json:"phone"`
	Email    string `json:"email"`
}
