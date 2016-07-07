import MySQLdb
import MySQLdb.cursors


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='3926',
                                 db='books',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def insert_books(values):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Books (title, ISBN) VALUES (%s, %s)", values)


def select(**kwargs):
    connection = get_connection()
    cursor = connection.cursor()
    if kwargs:
        q = "SELECT * FROM Books WHERE "
        for key, value in kwargs.items():
            select_id = key
            val = value
            q += "{}={} AND" .format(select_id, val)
        q = q[:len(q) - 3]
        print(q)
    else:
        q = "SELECT * FROM Books"
    cursor.execute(q)
    return cursor.fetchall()


insert_books([
      ('Book1', 'qwe-123'),
      ('Book2', 'qwe-1212'),
    ])


print(select(book_id="2"))
