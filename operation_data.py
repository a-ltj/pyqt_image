# _*_ coding:utf-8 _*_
"""
 数据库操作
"""
import pymysql

host = ''
port = 0
user = ''
password = ''
print('Starting the create database operation, please enter the information required for the database.')
print('------------------------------------')
host = input('please input database host:')
port = input('please input database port:')
user = input('please input database user:')
password = input('please input database password:')
print('------------------------------------')
try:
    conn = pymysql.connect(host=host, port=int(port), user=user, password=password)

    print('create database...')
    cur = conn.cursor()
    cur.execute('create database if not exists book3')
    print('database created done.')
    print('------------------------------------')
    conn.select_db('book3')

    print('create user table...')
    cur.execute("CREATE TABLE IF NOT EXISTS user ("
                "id varchar(50) PRIMARY KEY,"
                "username varchar(255),"
                "password varchar(255),"
                "role int(11))")
    conn.commit()
    cur.close()
    conn.close()
    print('user table created done.')
    print('------------------------------------')
    print('operate done.')
    print('create database successful.')
except Exception as e:
    print('the require information of database is correct, please check it and retry.')
    print(e.args)
    import traceback
    traceback.print_exc()
    print('create database failed.')
