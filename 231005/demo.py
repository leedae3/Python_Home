import pymysql

# 1. connect
conn, cursor = None, None
try :
    conn = pymysql.connect(host='54.180.158.177', port=3306, user='root', password='pythonmysql')
    print(conn)

# 2. cursor
    cursor = conn.cursor()
# 3. SQL Statement
    sql = "SELECT NOW()"
    cursor.execute(sql)
# 4. fetch
    result = cursor.fetchone()
    print(result)
except Exception as err:
    print(err)
finally :
# 5. close
    cursor.close()
    conn.cursor()
    