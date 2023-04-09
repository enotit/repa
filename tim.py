from mysql.connector import connect


def query(con, request):
    with con.cursor() as cursor:
        cursor.execute(request)
        return cursor.fetchall()


def insert(con, request):
    with con.cursor() as cursor:
        cursor.execute(request)
        con.commit()


def debug(con, text, place="base", type="INFO"):
    insert(
        con, f'INSERT INTO `Logs` (`place`, `text`, `type`) VALUES ("{place}", "{text}", "{type}");')

con = connect(
    host="server235.hosting.reg.ru",
    user="u1922448_timur",
    password="kB3pW6wY5xkO8cH7",
    database="u1922448_timur"
)
debug(con, 'START')