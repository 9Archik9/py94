def insert_product_name(cursor):
    product_name = input('Enter product name: ')
    cursor.execute(
        'INSERT INTO products (ProductName) VALUES (%s) RETURNING Id;',  # '%s' used to prevent SQL-injections :)))
        (product_name,)
    )
    return cursor.fetchone()[0]


def update_product_details(cursor, product_id):
    protein_value = float(input('Enter protein value: '))
    carbohydrates_value = float(input('Enter carbohydrates value: '))
    fats_value = float(input('Enter fats value: '))

    cursor.execute(
        'UPDATE products SET Protein = %s, Carbohydrates = %s, Fats = %s WHERE Id = %s;',
        (protein_value, carbohydrates_value, fats_value, product_id)
    )
