# -*- coding: utf-8 -*-

from common.base import Base


class RegionCategoryPage(Base):
    """封装表现层: 制作定位器"""
    RegionCategory_loc = ("xpath", "//*[contains(text(),'地区类目维护')]")  # 地区类目维护标签
    region_pull_loc = ('xpath', "//i[@class='el-input__icon el-icon-arrow-down']")  # 地区下拉框
    BJ_loc = ("xpath", "//*[contains(text(),'北京地区')]")  # 北京地区
    BJTY_loc = ("xpath", "//*[contains(text(),'太原事业部')]")  # 太原事业部
    catgory_edit_loc = (
    'xpath', "//*[contains(text(),'属地化模块')]/../../../div[2]/div[last()]/div[1]/span[2]/div/span")  # 类目编辑按钮
    confirm_button_loc = ('xpath', "//*[contains(text(),'确定')]")  # 删除确定按钮
    attrname01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[1]")  # 属性项名称
    attrname02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[1]")  # 属性项名称
    attrname03_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[3]/td[1]")  # 属性项名称
    attrname04_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[4]/td[1]")  # 属性项名称
    isRequired01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[4]")  # 是否必填
    isRequired02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[4]")  # 是否必填
    multiple02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[5]")  # 是否单选
    useContact01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[6]")  # 名称生成项
    useContact02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[6]")  # 名称生成项
    attrtype01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[7]")  # 属性值格式
    add_attr_loc = ("xpath", "//*[contains(text(),'新增属性项')]")  # 点击新增属性项
    attr_type_pull_loc = ('xpath', "//label[@for='attrType']/../div/div/div[1]/span/span/i")  # 属性值类型下拉框
    enu_type_loc = ("xpath", "/html/body/div[5]/div[1]/div[1]/ul/li[2]/span")  # 枚举类型
    datatype_pull_loc = ('xpath', "//label[@for='dataType']/../div/div/div[1]/span/span/i")  # 属性格式下拉框
    str_type_loc = ("xpath", "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span")  # 文本格式
    input_attr_value_loc = ("xpath", "//input[@placeholder='请输入属性值']")  # 属性值输入框
