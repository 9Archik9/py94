CREATE DATABASE Meal;

CREATE TABLE IF NOT EXISTS Products (
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(15) CONSTRAINT must_be_define CHECK (Products.ProductName NOT LIKE '%[0-9]%')  NOT NULL,
    Protein DECIMAL(6, 2),
    Carbohydrates DECIMAL(6, 2),
    Fats DECIMAL(6, 2)
);
