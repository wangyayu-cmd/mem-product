# -*- coding: utf-8 -*-

from common.base import Base
from selenium.webdriver.common.by import By


class GroupCategoryPage(Base):
    """封装表现层: 制作定位器"""
    yy = (By.CSS_SELECTOR,)
    GroupCategory_loc = ("xpath", "//*[contains(text(),'类目维护')]")  # 集团类目维护标签
    ShuDihua_loc = ('xpath', "//*[contains(text(),'属地化模块')]")  # 属地化模块
    last_Subclass_ShuDihua_loc = (
        'xpath',
        "//*[contains(text(),'属地化模块')]/../../../div[2]/div[last()]/div[1]/span[2]/span")  # 属地化模块最后一个子类目
    last_Subclass_del_loc = ('xpath',
                             "//*[contains(text(),'属地化模块')]/../../../div[2]/div[last()]/div/span[2]/div/span[3]")  # 属地化模块最后子类目删除按钮
    confirm_leave_loc = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')  # 确认离开按钮
    category_del_confirm_loc = ('xpath', "//div[@aria-label='提示']/div/div[3]/button[2]")  # 删除确认按钮
    add_ShuDihua_Subclass_loc = ('xpath', "//*[contains(text(),'属地化模块')]/following-sibling::div/span")  # 添加属地化模块二级类目按钮
    input_category_code_loc = ('xpath', "//input[@placeholder='请输入编码']")  # 分类编码输入框
    input_category_name_loc = ('xpath', "//input[@placeholder='请输入名称']")  # 输入分类名称
    mould_name_droplist_loc = ('xpath', "//input[@placeholder='请选择']")  # 选择模板下拉框
    first_mould_loc = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')  # 第一个模板
    choose_mould_loc = ('xpath', "//*[contains(text(),'编辑模板')]")  # 选择自定义模板
    needBusinessType_droplist_loc = ('xpath',
                                     '//*[@id="scrollContent"]/section/div[1]/div/div/div[1]/form/div[2]/div[1]/div/div/div/input')  # 适用业态下拉框
    needBusinessType_loc = ('xpath', "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")  # 选择有适用业态
    product_name = ('xpath', "//input[@placeholder='请输入名称' and @maxlength='80']")  # 产品名称举例输入框
    submit_button_loc = ('xpath', "//*[contains(text(),'提交')]")  # 提交按钮
    attrname01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[1]")  # 属性项名称
    attrname02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[1]")  # 属性项名称
    attrname03_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[3]/td[1]")  # 属性项名称
    attrname04_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[4]/td[1]")  # 属性项名称
    attrname05_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[5]/td[1]")  # 属性项名称
    inControl02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[4]")  # 管控属性值
    isRequired01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[5]")  # 是否必填
    isRequired02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[5]")  # 是否必填
    multiple02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[6]")  # 是否单选
    useContact01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[7]")  # 名称生成项
    useContact02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[7]")  # 名称生成项
    attrtype01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[8]")  # 属性值格式
    category_edit_loc = ('xpath', "//*[contains(text(),'测试分类')]/following-sibling::div/span[2]")  # 类目编辑按钮
    needBusiness_loc = ('xpath', "//*[contains(text(),'是否有适用业态')]/following-sibling::\"")
    attr01_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[9]/div/span[1]")  # 第一条属性项编辑按钮
    attr02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[9]/div/span[1]")  # 第二条属性项编辑按钮
    attr_edit_name_loc = ('xpath', "//input[@placeholder='请输入属性项']")  # 编辑属性项属性名称输入框
    useContact01_edit_loc = ('xpath',
                             "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[7]/div/label/span/span")  # 名称生成项勾选按钮
    useContact02_edit_loc = ('xpath',
                             "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[7]/div/label/span/span")  # 名称生成项勾选按钮
    multiple02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[6]/div/span/label/span/span")  # 勾选第二条属性项单选按钮

    ###################################################################################################################

    DaLiMian_loc = ('xpath', "//*[contains(text(),'大立面')]")  # 大立面模块
    add_DaLiMian_Subclass_loc = ('xpath', "//*[contains(text(),'大立面')]/following-sibling::div/span[1]")  # 添加大立面模块二级类目按钮
    choose_C2mould_loc = ('xpath', "//*[contains(text(),'C2编辑模板')]")  # 选择自定义模板
    last_Subclass_DaLiMian_loc = ('xpath', "//*[contains(text(),'大立面')]/../../../div[2]/div[last()]")  # 大立面模块最后一个子类目
    C2_isRequired01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[4]")  # 是否必填
    C2_isRequired02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[4]")  # 是否必填
    C2_multiple02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[5]")  # 是否单选
    C2_attrtype01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[6]")  # 属性值格式
    category_C2edit_loc = ('xpath', "//*[contains(text(),'C2测试分类')]/following-sibling::div/span[2]")  # 类目编辑按钮
    C2_multiple02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[5]/div/span/label/span/span")  # 勾选第二条属性项单选按钮
    C2_attr01_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[7]/div/span[1]")  # 第一条属性项编辑按钮
    C2_attr02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[7]/div/span[1]")  # 第二条属性项编辑按钮
    C2_enu_type_loc = ("xpath", "/html/body/div[3]/div[1]/div[1]/ul/li[2]")  # 枚举类型
    C2_last_Subclass_del_loc = ('xpath',
                                "//*[contains(text(),'大立面')]/../../../div[2]/div[last()]/div/span[2]/div/span[3]")  # 大立面模块最后子类目删除按钮

    ####################################################################################################################
    XuNiFangZhen_loc = ('xpath', "//*[contains(text(),'虚拟仿真')]")  # 虚拟仿真模块
    add_XuNiFangZhen_Subclass_loc = (
        'xpath', "//*[contains(text(),'虚拟仿真')]/following-sibling::div/span[1]")  # 添加大立面模块二级类目按钮
    choose_VRmould_loc = ('xpath', "//*[contains(text(),'VR编辑模板')]")  # 选择自定义模板
    last_Subclass_XuNiFangZhen_loc = (
        'xpath', "//*[contains(text(),'虚拟仿真')]/../../../div[2]/div[last()]")  # 大立面模块最后一个子类目
    VR_isRequired01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[5]")  # 是否必填
    VR_isRequired02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[5]")  # 是否必填
    VR_multiple02_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[6]")  # 是否单选
    VR_attrtype01_loc = (
        'xpath', "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[7]")  # 属性值格式
    category_VRedit_loc = ('xpath', "//*[contains(text(),'VR测试分类')]/../div/span[2]")  # 类目编辑按钮
    VR_attr01_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[1]/td[8]/div/span[1]")  # 第一条属性项编辑按钮
    VR_attr02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[8]/div/span[1]")  # 第二条属性项编辑按钮
    VR_multiple02_edit_loc = (
        'xpath',
        "//div[@class='el-table__body-wrapper is-scrolling-none']/table/tbody/tr[2]/td[6]/div/span/label/span/span")  # 勾选第二条属性项单选按钮
    VR_last_Subclass_del_loc = ('xpath',
                                "//*[contains(text(),'虚拟仿真')]/../../../div[2]/div[last()]/div/span[2]/div/span[3]")  # 虚拟仿真模块最后子类目删除按钮

    """
        封装操作层: 元素操作
        每一个元素的操作,都写成一个方法
        低耦合性:
        """

    def click_Group_Category(self):
        """点击新增模板按钮"""
        self.click(self.GroupCategory_loc)

    def get_ele_text(self, loc):
        """
        获取元素文本
        :return:
        """
        text = self.find_element(loc).text
        return text

    def move_a_mouse(self, locator):
        """
        移动鼠标到元素
        :param locator:
        :return:
        """
        self.move_mouse(locator)

    def click_confirm_leave(self):
        """
        点击确认离开按钮
        :return:
        """
        self.click(self.confirm_leave_loc)

    def click_add_ShuDihua_Subclass(self):
        """
        添加属地化模块二级类目
        :return:
        """
        self.click(self.add_ShuDihua_Subclass_loc)

    def input_category_code(self, text):
        """
        输入分类编码
        :return:
        """
        self.send_keys(self.input_category_code_loc, text)

    def input_category_name(self, text):
        """
        输入分类编码
        :return:
        """
        self.send_keys(self.input_category_name_loc, text)

    def click_mould_name_droplist(self):
        """
        点击选择模板下拉框
        :return:
        """
        self.click(self.mould_name_droplist_loc)

    def click_first_mould(self):
        """
        点击第一个模板
        :return:
        """
        self.click(self.first_mould_loc)

    def click_needBusinessType_droplist(self):
        """
        点击是否有试用业态下拉框
        :return:
        """
        self.click(self.needBusinessType_droplist_loc)

    def click_needBusinessType(self):
        """
        选择有适用业态
        :return:
        """
        self.click(self.needBusinessType_loc)

    def input_product_name(self, text):
        """
        输入产品举例名称
        :return:
        """
        self.send_keys(self.product_name, text)

    def click_submit_button(self):
        """
        点击提交按钮
        :return:
        """
        self.click(self.submit_button_loc)

    def click_attr01_edit(self):
        """
        点击第一条属性项编辑按钮
        :return:
        """
        self.click(self.attr01_edit_loc)

    def input_attr_edit_name(self, text):
        """
        编辑第一条属性项名称
        :return:
        """
        self.send_keys(self.attr_edit_name_loc, text)

    def click_useContact_edit(self):
        """
        点击名称生成项勾选按钮
        :return:
        """
        self.click(self.useContact01_edit_loc)
