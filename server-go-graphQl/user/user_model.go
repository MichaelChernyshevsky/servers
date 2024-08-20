package user

import (
	"gorm.io/gorm"
)

type UserModel struct {
	gorm.Model
	// cred
	Email    string `gorm:"size:250"`
	Password string `gorm:"size:250"`
	Phone    string `gorm:"size:250"`
	// PackagesId int
	Subscribed bool

	// info
	Info InfoModel `gorm:"foreignKey:UserID"`
}

func (u *UserModel) Serialize() map[string]interface{} {
	return map[string]interface{}{
		"id":       u.ID,
		"email":    u.Email,
		"password": u.Password,
		"phone":    u.Phone,
		// "packagesId": u.Packages,
		"info":       u.Info.Serialize(),
		"subscribed": u.Subscribed,
	}
}

// Методы поиска пользователя
func FindUserModelByEmail(db *gorm.DB, email string) (*UserModel, error) {
	var model UserModel
	result := db.Where("email = ?", email).First(&model)
	return &model, result.Error
}

func FindUserModelByID(db *gorm.DB, id uint) (*UserModel, error) {
	var model UserModel
	result := db.First(&model, id)
	return &model, result.Error
}
