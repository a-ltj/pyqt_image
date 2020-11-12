# _*_ coding:utf-8 _*_
"""
 获取id字符串 密码加密  提示框  验证密码  验证邮件
"""
import uuid

from PyQt5.QtWidgets import QMessageBox


def get_uuid1():
    """
    生成随机序列
    get the uuid str
    :return: the uuid1 object
    """
    return str(uuid.uuid1())

def msg_box(widget, title, msg):

    QMessageBox.warning(widget, title, msg, QMessageBox.Yes)