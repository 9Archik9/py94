from config import host, user, database, password, port

from db_requests import insert_product_name, update_product_details

import psycopg2


def db_connect():
    connection = None

    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port ,
            database=database,
        )

        cursor = connection.cursor()

        product_id = insert_product_name(cursor)
        connection.commit()
        print('Column ProductName successfully inserted')

        update_product_details(cursor, product_id)
        connection.commit()
        print('Data successfully added to the database')

    except psycopg2.Error as error:
        print('Error with connection to PostgreSQL', error)

    finally:
        if connection:
            connection.close()
            print('Connection with PostgreSQL closed')


db_connect()
