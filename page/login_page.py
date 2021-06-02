# -*- coding: utf-8 -*-

from common.base import Base



class LoginPage(Base):
    """封装表现层: 制作定位器"""
    username_loc = ("id", "username")  # 用户名输入框
    password_loc = ("id", "password")  # 密码输入框
    submit_loc = ("name", "submit")  # 登录按钮

    """
    封装操作层: 元素操作
    每一个元素的操作,都写成一个方法
    低耦合性
    """
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def click_submit(self):
        """点击登录"""
        self.click(self.submit_loc)



