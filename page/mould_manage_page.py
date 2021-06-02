# -*- coding: utf-8 -*-

from common.base import Base


class MouldManagePage(Base):
    """封装表现层: 制作定位器"""
    mould_loc = ("xpath", "//*[contains(text(),'模板管理')]")  # 保存按钮
    add_mould_loc = ("xpath", "//*[contains(text(),'新增模板')]")  # 新增模板按钮
    mould_name_loc = ("xpath", "//input[@placeholder='请输入模板名称']")  # 模板名称输入框
    attrgrp_name_loc = ("xpath", "//input[@placeholder='请输入属性组名称']")  # 属性组名称输入框
    attrgrp_name_text_loc = ('xpath', '//*[@class="el-collapse-item is-active"]/div/div/strong')  # 属性组名称
    save_button_loc = ("xpath", "//*[contains(text(),'保存')]")  # 保存按钮
    add_attr_button_loc = ('xpath', "//*[contains(text(),'新增属性项')]")  # 新增属性项按钮
    attr_name_loc = ('xpath', "//input[@placeholder='请输入属性名称']")  # 新增属性项属性名称输入框
    attr_type_loc = ('xpath', "//input[@placeholder='请选择']")  # 属性值类型下拉框
    input_type_loc = ('xpath', "//*[contains(text(),'输入类型')]")  # 输入型选项
    eum_type_loc = ('xpath', "//*[contains(text(),'枚举类型')]")  # 枚举型选项
    attr_value_loc = ('xpath',
                      '//*[@id="scrollContent"]/section/div[1]/section[2]/div/div[2]/div/div[2]/div/form/div[3]/div/div/div[1]/input')  # 属性值输入框
    add_attr_confirm_button_loc = ('xpath', "//*[contains(text(),'确 定')]")  # 新增属性项弹窗确定按钮
    submit_button_loc = ('xpath', "//*[contains(text(),'提交')]")  # 提交按钮
    first_mould_loc = ('xpath',
                       '//div[@class="tabPositionClass el-scrollbar"]/div[1]/div/div/div[1]')  # 第一个模板
    first_mould_del_loc = ('xpath', '//div[@class="tabPositionClass el-scrollbar"]/div[1]/div/div/div[1]/i')
    confirm_del_button_loc = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
    edit_button_loc = ('xpath', '//*[@class="el-collapse-item is-active"]/div/div/button[1]/span')  # 编辑按钮

    """
    封装操作层: 元素操作
    每一个元素的操作,都写成一个方法
    低耦合性:
    """

    def click_add_mould(self):
        """点击新增模板按钮"""
        self.click(self.add_mould_loc)

    def input_mould_name(self, text):
        """输入模板名称"""
        self.send_keys(self.mould_name_loc, text)

    def input_attrgrp_name(self, text):
        """输入属性组名称"""
        self.send_keys(self.attrgrp_name_loc, text)

    def click_save_button(self):
        """点击保存按钮"""
        self.click(self.save_button_loc)

    def click_add_attr_button(self):
        """点击新增属性项按钮"""
        self.click(self.add_attr_button_loc)

    def input_attr_name(self, text):
        """输入属性项名称"""
        self.send_keys(self.attr_name_loc, text)

    def click_attr_type(self):
        """点击属性项类型下拉框"""
        self.click(self.attr_type_loc)

    def click_input_type(self):
        """选择属性项类型为输入类型"""
        self.click(self.input_type_loc)

    def click_eum_type(self):
        """选择属性项类型为枚举类型"""
        self.click(self.eum_type_loc)

    def input_attr_value(self, text):
        """
        输入属性值
        :param text:
        :return:
        """
        self.send_keys(self.attr_value_loc, text)

    def click_add_attr_confirm_button(self):
        """点击添加属性项弹窗确认按钮"""
        self.click(self.add_attr_confirm_button_loc)

    def click_submit_button(self):
        """点击立即登录"""
        self.click(self.submit_button_loc)

    def move_first_mould(self):
        """
        移动鼠标到第一个模板
        :return:
        """
        self.move_mouse(self.first_mould_loc)

    def click_first_moould(self):
        """
        点击第一个模板
        :return:
        """
        self.click(self.first_mould_loc)

    def get_ele_text(self, loc):
        """
        获取元素文本
        :return:
        """
        text = self.find_element(loc).text
        return text

    def click_first_mould_del(self):
        """
        点击第一个模板删除按钮
        :return:
        """
        self.click(self.first_mould_del_loc)

    def click_confirm_del_button(self):
        """
        点击确认删除按钮
        :return:
        """
        self.click(self.confirm_del_button_loc)

    def click_edit_button(self):
        """
        点击编辑按钮
        :return:
        """
        self.click(self.edit_button_loc)
