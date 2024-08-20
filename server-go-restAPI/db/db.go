package db

import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Глобальная переменная для подключения к базе данных
var DB *gorm.DB

// Инициализация подключения к базе данных
func Init() error {
	var err error
	dsn := "host=localhost port=6500 dbname=postgres sslmode=disable password=yourpassword"

	DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		return err
	}

	// Проверка подключения
	sqlDB, err := DB.DB()
	if err != nil {
		return err
	}

	err = sqlDB.Ping()
	if err != nil {
		return err
	}

	return nil

}
