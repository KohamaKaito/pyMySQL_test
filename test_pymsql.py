# モジュール読み込み
import pymysql.cursors

# mySQL
"""
mysql> SELECT * FROM user;
+----+--------+------+
| id | name   | age  |
+----+--------+------+
|  1 | John   |   29 |
|  2 | Jesika |   20 |
|  3 | Cookie |   52 |
+----+--------+------+
3 rows in set (0.00 sec)
"""

# MySQLに接続する
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test_pymysql',
                             charset='utf8',
                             # cursorclassを指定することで
                             # Select結果をtupleではなくdictionaryで受け取れる
                             cursorclass=pymysql.cursors.DictCursor)
# MySQLから切断する
#connection.close()


# SQLを実行する
with connection.cursor() as cursor:
    sql = "SELECT id, name FROM user WHERE age >= 50"
    cursor.execute(sql)

    # Select結果を取り出す
    results = cursor.fetchall()
    for r in results:
        print(r)
        # => {'name': 'Cookie', 'id': 3}


# Insert処理
with connection.cursor() as cursor:
    sql = "INSERT INTO user (id, name, age) VALUES (%s, %s, %s)"
    r = cursor.execute(sql, (4, "Shanky", 38))
    print(r) # -> 1
    # autocommitではないので、明示的にコミットする
    connection.commit()


# Update処理
with connection.cursor() as cursor:
    sql = "UPDATE user SET age = %s WHERE id = %s"
    r = cursor.execute(sql, (12, 1))
    print(r) # -> 1
    # autocommitではないので、明示的にコミットする
    connection.commit()