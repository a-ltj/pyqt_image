# _*_ coding:utf-8 _*_
"""
 注册页面
"""
import sys


from PyQt5.QtWidgets import QWidget, QApplication

from ui.register_window import Ui_Form
from util.dbUtil import DBHelp
from util.commonUtil import msg_box,get_uuid1




class RegisterWindow(Ui_Form, QWidget):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('用户注册')
        # self.init_ui()美化界面
        self.register_pushButton.clicked.connect(self.register)

    def register(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        confirm = self.confirm_password_lineEdit.text()
        if '' in [username, password, confirm]:
            msg_box(self, '提示', '关键信息不能为空!')
            return
        db = DBHelp()
        count, res = db.query_super(table_name='user', column_name='username', condition=username)
        if count != 0:
            msg_box(self, '提示', '用户名已存在!')
            return
        if password != confirm:
            msg_box(self, '错误', '两次输入密码不一致!')
            return
        user_info = [get_uuid1(), username, password, 1]
        db.add_user(user_info)
        db.db_commit()
        db.db_close()
        msg_box(self, '提示', '注册成功!')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RegisterWindow()
    win.show()
    sys.exit(app.exec())