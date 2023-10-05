import pymysql

host = '54.180.158.177'
port = 3306
user = 'root'
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
cursor = conn.cursor()
sql = "SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor. execute(sql)
results = cursor.fetchall()
for emp in results :
    print(emp[1], emp[3], sep='\t')
cursor.close()
conn.close()