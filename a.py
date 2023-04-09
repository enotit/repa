from mysql.connector import connect, Error

try:
    with connect(
        host="server235.hosting.reg.ru",
        user="u1922448_root",
        password="BYMRK42euh3TrBc7",
        database="u1922448_volsu"
    ) as connection:
        select_movies_query = "SELECT * FROM boy"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
               print(row)
except Error as e:
    print(e)