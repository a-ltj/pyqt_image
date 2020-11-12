# _*_ coding:utf-8 _*_
"""
 登录页面
"""
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel
import sys

from PyQt5.QtWidgets import QWidget

from ui.login_window import Ui_Form
from util.dbUtil import DBHelp
from view.register import RegisterWindow
from util.commonUtil import msg_box
from view.main import MainWindow


class LoginWindow(Ui_Form, QWidget):
    def __init__(self):
        """
        登陆界面类构造函数,初始化类属性等.
        """
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.main_window = None
        self.register_win = None
        self.init_slot()

    def init_ui(self):
        self.setWindowTitle('用户登录')
        self.setWindowIcon(QIcon("../img/login2.jpg"))
        #禁止最大化
        self.setFixedSize(self.width(), self.height())
        self.username_lineEdit.setPlaceholderText('请输入用户名')
        self.password_lineEdit.setPlaceholderText('请输入密码')
        # pixmap = QPixmap("../img/login1.jpg")
        # scaredPixmap = pixmap.scaled(650, 140)
        # self.label.setPixmap(scaredPixmap)
        pixmap = QPixmap("../img/login2.jpg")
        scaredPixmap1 = pixmap.scaled(80, 80)
        self.label_4.setPixmap(scaredPixmap1)
    def init_slot(self):
        """
        初始化信号槽连接
        """
        self.register_pushButton.clicked.connect(self.register)
        self.login_pushButton.clicked.connect(self.login)


    def register(self):
        self.register_win = RegisterWindow()
        self.register_win.show()

    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if '' in [username, password]:
            msg_box(self, '提示', '请输入用户名或密码!')
            return
        db = DBHelp()
        count, res = db.query_super(table_name='user', column_name='username', condition=username)
        if count == 0:
            msg_box(self, '提示', '用户名不存在,请重试!')
            return

        if password != res[0][2]:
            msg_box(self, '提示', '用户名或密码错误!')
            return
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec_())
