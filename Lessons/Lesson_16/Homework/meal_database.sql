CREATE DATABASE FoodIntake;

USE FoodIntake;

CREATE TABLE Meal(
    user_id INT PRIMARY KEY,
        /*
        I want user_id to store only numeric values and also be the primary key
        (it is good practice to make id via primary_key)
        */
    food_intake CHAR(5) CONSTRAINT must_be_time_format CHECK (food_intake LIKE '__:__') NOT NULL,
        /*
        In this example, food_intake is declared as CHAR(5) with a CHECK (must_be_time_format) constraint
        that checks the time format: two digits, then the : character, and two more digits.
        Thus, this constraint ensures that the food_intake column contains only digits and the : character
        in the format "hh:mm".
        */
    product VARCHAR(15) CONSTRAINT must_be_define CHECK (product NOT LIKE '%[0-9]%')  NOT NULL
        /*
        I want the product column to have a maximum of 15 characters, because I do not know the product
        with a large number of characters, I also made a check that the product column does not have numbers (0-9).
        and also NOT NULL, so that something in this column is stored yes
        */
);
