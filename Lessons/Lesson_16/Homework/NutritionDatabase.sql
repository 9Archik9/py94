-- create database
CREATE DATABASE NutritionDatabase;

-- Table Users
CREATE TABLE IF NOT EXISTS Users (
    /*
     IF NOT EXISTS means that the operation will be performed only if the corresponding object
     does not yet exist in the database
     */
    UserID SERIAL PRIMARY KEY,
    /* SERIAL - specification in PSQL for a column in a database table
    that automatically increases its value when new rows are added. it is convenient to use it with primary key value
       SERIAL already includes the INT data type

       PRIMARY KEY - it is good to assign columns with id to a value that will be referenced by other tables later
     */
    UserName VARCHAR(15) NOT NULL,
    /*
     VARCHAR - character limit for UserName
     NOT NULL - column value must necessarily have the value
     */
    Age INT NOT NULL,
    /*
     INT - only numbers can be written in the column, which is what you're supposed to do.
     */
    Gender VARCHAR(10) NOT NULL
    /*
     there are only two genders 🙂
     */
);

-- Table product
CREATE TABLE IF NOT EXISTS Products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(15) CONSTRAINT must_be_define CHECK (Products.ProductName NOT LIKE '%[0-9]%')  NOT NULL,
    /*
      I want the product column to have a maximum of 15 characters, because I do not know the product
        with a large number of characters, I also made a check that the product column does not have numbers (0-9).
        and also NOT NULL, so that something in this column is stored yes
     */
    Calories INT NOT NULL,
    /*
     if ProductName have constraint, then it is logical that this column should also have such a constraint
     */
    Protein DECIMAL(6, 2) NOT NULL,
    /*
     DECIMAL - indicates a numeric data type with fixed precision and scale.
     DECIMAL(6, 2) indicates that a number can have up to 6 digits in total and up to 2 digits after the decimal point
     */
    Carbohydrates DECIMAL(6, 2) NOT NULL,
    Fats DECIMAL(6, 2) NOT NULL
);

-- Table Consumption (meal)
CREATE TABLE IF NOT EXISTS Consumption (
    ConsumptionID SERIAL PRIMARY KEY,
    UserID INT,
    ProductID INT NOT NULL,
    Quantity DECIMAL(6, 2) NOT NULL,
    ConsumedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    /*
     CURRENT_TIMESTAMP - specifies that the default will be the current date and time at the time the row is inserted,
     unless the value of this column is explicitly specified when adding a new record to the table.

     TIMESTAMP -
     */
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    /*
     This means that the UserID column in the Consumption table is a foreign key
     that references the UserID column in the Users table.
     */
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
