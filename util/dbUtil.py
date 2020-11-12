# _*_ coding:utf-8 _*_
"""
 数据库操作类  登陆注册页面只需增加和查找用户数据库即可
"""
import pymysql
class DBHelp:

    def __init__(self, host='localhost', port=3306, user='root', pwd='123456', db='book3', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset=charset)
        self.cur = self.conn.cursor()

    def query_all(self, table_name):
        sql = 'select * from {}'.format(table_name)
        count = self.cur.execute(sql)
        res = self.cur.fetchall()
        return count, res

    def query_super(self, table_name, column_name, condition):
        sql = "select * from {} where {}='{}'".format(table_name, column_name, condition)
        count = self.cur.execute(sql)
        res = self.cur.fetchall()
        return count, res

    def add_user(self, data):
        sql = "insert into user (id, username, password, role) values (%s, %s, %s, %s)"
        self.cur.execute(sql, data)

    def db_commit(self):
        self.conn.commit()

    def db_close(self):
        self.cur.close()
        self.conn.close()
    def db_close2(self):
        self.conn.close()

    def db_rollback(self):
        self.conn.rollback()
