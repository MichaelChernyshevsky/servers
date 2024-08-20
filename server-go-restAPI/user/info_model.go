package user

import "gorm.io/gorm"

// InfoModel represents additional user information.
type InfoModel struct {
	gorm.Model
	UserID  uint   // Foreign key for UserModel
	Sex     string `gorm:"size:250"`
	Name    string `gorm:"size:250"`
	Name2   string `gorm:"size:250"`
	Age     int
	Admin   bool
	Creator bool
}

// Serialize converts InfoModel to a map.
func (i *InfoModel) Serialize() map[string]interface{} {
	return map[string]interface{}{
		"id":      i.ID,
		"sex":     i.Sex,
		"name":    i.Name,
		"name2":   i.Name2,
		"age":     i.Age,
		"admin":   i.Admin,
		"creator": i.Creator,
	}
}
