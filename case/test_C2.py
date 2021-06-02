# -*- coding: utf-8 -*-

# 调用page文件夹中的login_page.py
import time, os
import unittest

from page.login_page import LoginPage
from page.mould_manage_page import MouldManagePage
from page.group_category_page import GroupCategoryPage
from page.region_category_page import RegionCategoryPage
from page.product_page import ProductPage
from page.view_page import ViewPage
from common.base import open_browser

from BeautifulReport import BeautifulReport


class TestC2(unittest.TestCase):

    def save_img(self, test_method):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file \
            ('{}/{}.png'.format(img_path, test_method))

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()  # 打开浏览器
        cls.login = LoginPage(cls.driver)  # 实例化LoginPage
        cls.login.open_url("http://kit.longfor.uat/")  # 打开登录地址
        cls.login.input_username("liumeng6")
        cls.login.input_password("1")
        cls.login.click_submit()
        cls.mouldmanage = MouldManagePage(cls.driver)
        cls.GroupCategory = GroupCategoryPage(cls.driver)
        cls.RegionCategory = RegionCategoryPage(cls.driver)
        cls.ProductPage = ProductPage(cls.driver)
        cls.ViewPage = ViewPage(cls.driver)

    @BeautifulReport.add_test_img('test_C201_creat_mould')
    def test_C201_creat_mould(self):
        """
        C2模板管理页面:
        创建模板
        """
        # 1.点击新增模板
        self.mouldmanage.click_add_mould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("测试C2模板")
        # 3.输入属性组名称
        self.mouldmanage.input_attrgrp_name("测试C2属性组")
        # 4.点击保存按钮
        self.mouldmanage.click_save_button()
        # 5.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 6.输入属性名称
        self.mouldmanage.input_attr_name("测试C2属性名称")
        # 7.点击属性值类型下拉框
        self.mouldmanage.click_attr_type()
        time.sleep(1)
        # 8.选择属性值类型为输入类型
        self.mouldmanage.click_input_type()
        # 9.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 10.点击提交按钮
        self.mouldmanage.click_submit_button()
        time.sleep(1)
        # 11.判断创建后第一个模板名称为创建模板名称
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), '测试C2模板', msg='创建模板失败')

    @BeautifulReport.add_test_img('test_C202_edit_mould')
    def test_C202_edit_mould(self):
        """
        C2模板管理页面:
        编辑模板
        """
        # 1.点击第一个模板
        self.mouldmanage.click_first_moould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("C2编辑模板")
        # 3.点击编辑按钮
        self.mouldmanage.click_edit_button()
        # 4.输入属性组名称
        self.mouldmanage.input_attrgrp_name("C2编辑属性组")
        # 5.点击保存按钮
        self.mouldmanage.click_save_button()
        # 6.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 7.输入属性名称
        self.mouldmanage.input_attr_name("C2编辑属性名称")
        # 8.点击属性值类型下拉框
        self.mouldmanage.click_attr_type()
        time.sleep(1)
        # 9.选择属性值类型为枚举类型
        self.mouldmanage.click_eum_type()
        # 10.输入属性值
        self.mouldmanage.input_attr_value("C2_auto_enu")
        # 11.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 12.点击提交按钮
        self.mouldmanage.click_submit_button()
        time.sleep(3)
        # 13.判断编辑后第一个模板名称为编辑模板名称
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), 'C2编辑模板', msg='编辑模板失败')
        # 14.判断编辑后第一个模板属性组名称为编辑后属性组名称
        self.mouldmanage.click_first_moould()
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.attrgrp_name_text_loc), 'C2编辑属性组',
                         msg='编辑属性组名称失败')

    @BeautifulReport.add_test_img('test_C203_creat_groupCategory')
    def test_C203_creat_groupCategory(self):
        """
        C2集团类目页面:
        创建大立面模块集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        time.sleep(3)
        # # 2.刷新页面
        self.GroupCategory.refresh()
        time.sleep(3)
        # 3.鼠标移动到大立面模块
        self.GroupCategory.move_a_mouse(GroupCategoryPage.DaLiMian_loc)
        # 4.点击添加属地化模块二级类目按钮
        self.GroupCategory.click(GroupCategoryPage.add_DaLiMian_Subclass_loc)
        # 5.输入分类编码
        self.GroupCategory.input_category_code('test_code-C2')
        # 6.输入分类名称
        self.GroupCategory.input_category_name('C2测试分类')
        # 7.点击选择模板下拉框
        self.GroupCategory.click_mould_name_droplist()
        # 8.选择第一个模板
        # self.GroupCategory.click_first_mould()
        time.sleep(1)
        # 8.选择自定义模板
        self.GroupCategory.click(GroupCategoryPage.choose_C2mould_loc)
        # 9.输入分类名称举例
        self.GroupCategory.input_product_name('C2测试产品名称')
        # 10.点击提交按钮
        self.GroupCategory.click_submit_button()
        self.GroupCategory.refresh()
        time.sleep(3)
        # 11.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        self.assertEqual(text, 'C2测试分类', msg='创建C2集团类目失败')
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        time.sleep(3)
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_isRequired02_loc)
        self.assertEqual(text, '是', msg='默认是否必填项应为是')
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_multiple02_loc)
        self.assertEqual(text, '否', msg='单选默认应为否')

    @BeautifulReport.add_test_img('test_C204_edit_groupCategory')
    def test_C204_edit_groupCategory(self):
        """
        C2集团类目页面:
        编辑大立面模块集团类目
        """
        # 1.鼠标移动到自定义类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        # 2.点击自定义类目编辑按钮
        self.GroupCategory.click(GroupCategoryPage.category_C2edit_loc)
        # 3.输入分类编码
        self.GroupCategory.input_category_code('test_C2edit_code')
        # 4.输入分类名称
        self.GroupCategory.input_category_name('C2编辑分类')
        # 5.输入分类名称举例
        self.GroupCategory.input_product_name('C2编辑产品名称')
        # 6.点击第一条属性项编辑按钮
        self.GroupCategory.click(GroupCategoryPage.C2_attr01_edit_loc)
        # 7.编辑第一条属性项名称
        self.GroupCategory.input_attr_edit_name("C2集团属性项01")
        # 8.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 9.点击第二条属性项编辑按钮
        self.GroupCategory.click(GroupCategoryPage.C2_attr02_edit_loc)
        # 10.编辑第二条属性项名称
        self.GroupCategory.input_attr_edit_name("C2集团属性项02")
        # 11.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 12.勾选而二条属性项单选按钮
        self.GroupCategory.click(GroupCategoryPage.C2_multiple02_edit_loc)
        # 13.新增模块深度
        self.RegionCategory.click(RegionCategoryPage.add_attr_loc)
        self.GroupCategory.input_attr_edit_name("模块深度")
        self.RegionCategory.click(RegionCategoryPage.attr_type_pull_loc)
        time.sleep(1)
        self.GroupCategory.move_mouse(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.click(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.send_keys(RegionCategoryPage.input_attr_value_loc, 'test-模块深度')
        self.mouldmanage.click_add_attr_confirm_button()
        # 14.新增分供方
        self.RegionCategory.click(RegionCategoryPage.add_attr_loc)
        self.GroupCategory.input_attr_edit_name("分供方")
        self.RegionCategory.click(RegionCategoryPage.attr_type_pull_loc)
        time.sleep(1)
        self.GroupCategory.move_mouse(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.click(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.send_keys(RegionCategoryPage.input_attr_value_loc, 'test-分供方')
        self.mouldmanage.click_add_attr_confirm_button()
        # 15.新增推送节点
        self.RegionCategory.click(RegionCategoryPage.add_attr_loc)
        self.GroupCategory.input_attr_edit_name("推送节点")
        self.RegionCategory.click(RegionCategoryPage.attr_type_pull_loc)
        time.sleep(1)
        self.GroupCategory.move_mouse(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.click(GroupCategoryPage.C2_enu_type_loc)
        self.RegionCategory.send_keys(RegionCategoryPage.input_attr_value_loc, 'test-推送节点')
        self.mouldmanage.click_add_attr_confirm_button()
        # 16.点击提交按钮
        self.GroupCategory.click_submit_button()
        time.sleep(3)
        # 16.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        self.assertEqual(text, 'C2编辑分类', msg='创建集团类目失败')
        # 查看创建集团类目详情
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        # 第一条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname01_loc)
        self.assertEqual(text, 'C2集团属性项01', msg='第一条属性项名称错误')
        # 第一条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_isRequired01_loc)
        self.assertEqual(text, '是', msg='第一条属性项因为必填项')
        # 第一条属性项格式是否为文本
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_attrtype01_loc)
        self.assertEqual(text, '文本', msg='第一条属性项格式应为文本')
        # 第二条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname02_loc)
        self.assertEqual(text, 'C2集团属性项02', msg='第二条属性项名称错误')
        # 第二条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_isRequired02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为必填项')
        # 第二条属性项单选
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.C2_multiple02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为单选')
        # 第三条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname03_loc)
        self.assertEqual(text, '模块深度', msg='第三条属性项名称错误')
        # 第四条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname04_loc)
        self.assertEqual(text, '分供方', msg='第四条属性项名称错误')
        # 第五条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname05_loc)
        self.assertEqual(text, '推送节点', msg='第五条属性项名称错误')

    @BeautifulReport.add_test_img('test_C205_creat_product')
    def test_C205_creat_product(self):
        """
        C2产品入库页面:
        新增产品
        """
        time.sleep(3)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击新增产品按钮
        self.ProductPage.click_add_product()
        time.sleep(3)
        # 2.点击主责专业下拉框
        self.ProductPage.click(ProductPage.C2_major_pull)
        time.sleep(3)
        # 3.点击大立面模块
        self.ProductPage.click(GroupCategoryPage.DaLiMian_loc)
        # 4.点击选择分类，选择C2编辑分类
        self.ProductPage.click(ProductPage.C2_category_pull)
        element = self.ProductPage.find_element(ProductPage.C2_category_loc)
        self.driver.execute_script("arguments[0].click();", element)
        # 5.输入第一个属性值
        self.ProductPage.input_attr01_value("test_C2")
        # 6.点击第二个属性值下拉框
        self.ProductPage.click_attr02_value()
        # 7.选择属性值
        self.ProductPage.click(ProductPage.C2_choose_attr02_value_loc)
        # 8.点击功能分区下拉框
        self.ProductPage.click(ProductPage.C2_function_pull)
        # 9.鼠标移动到 前场
        self.GroupCategory.move_a_mouse(ProductPage.C2_choose_function_loc)
        # 10.选择前场
        self.ProductPage.click(ProductPage.C2_choose_function_loc)
        # 11.输入产品编码
        self.ProductPage.input_product_code("C2_auto_test_code")
        # 12.输入产品名称
        self.ProductPage.send_keys(ProductPage.C2_product_name_loc, "C2_test")
        # 13.点击模型图纸
        self.ProductPage.click(ProductPage.mould_img_loc)
        # 14.上传缩略图
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        file_path = root_dir + "/file/"
        element = self.ProductPage.find_element(ProductPage.upload_img_loc)
        self.driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            element)
        element.send_keys(file_path + "test_img.jpg")
        time.sleep(3)
        # 15.判断缩略图上传成功
        text = self.GroupCategory.get_ele_text(ProductPage.img_name_loc)
        self.assertEqual(text, 'test_img.jpg', msg='上传缩略图失败')
        # # 16.上传建筑2D文件
        element_2D = self.ProductPage.find_element(ProductPage.C2_upload_2D_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_2D)
        element_2D.send_keys(file_path + 'test_2D.dwg')
        # # 17.选择景观专业
        # self.ProductPage.click(ProductPage.major2D_pull_loc)
        # self.GroupCategory.move_mouse(ProductPage.major2D_loc)
        # self.ProductPage.click(ProductPage.major2D_loc)
        # # 18.选择G1-预案深度
        # self.ProductPage.click(ProductPage.depth2D_pull_loc)
        # self.GroupCategory.move_mouse(ProductPage.depth2D_loc)
        # self.ProductPage.click(ProductPage.depth2D_loc)
        # 19.判断2D图纸上传成功
        upload_status = False
        for i in range(100):
            ele = self.ProductPage.find_element(ProductPage.C2_upload_2D_status)
            value = ele.get_attribute('class')
            if value == 'percentage-ok':
                upload_status = True
                break
            else:
                time.sleep(3)
        self.assertTrue(upload_status, msg="文件一直上传中")
        text = self.GroupCategory.get_ele_text(ProductPage.C2_file_name_2D_loc)
        self.assertEqual(text, 'test_2D.dwg', msg='上传2D文件展示名称错误')
        # 20.点击提交按钮
        self.ProductPage.click(ProductPage.submit_loc)
        time.sleep(3)
        # 21.确认产品创建成功
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertEqual(text, 'C2_test', msg="创建产品失败")
        ele = self.ProductPage.find_element(ProductPage.product01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'status status_2', msg='创建后产品状态展示错误')

    @BeautifulReport.add_test_img('test_C206_detail_product')
    def test_C206_detail_product(self):
        """
        C2产品入库页面:
        查看产品详情
        """
        time.sleep(3)
        self.ProductPage.click(ProductPage.product_loc)
        # 1.点击第一条属性项名称进入产品详情页
        self.ProductPage.click(ProductPage.product01_name_loc)
        time.sleep(1)
        windows = self.ProductPage.driver.window_handles
        self.ProductPage.driver.switch_to.window(windows[-1])
        self.ProductPage.refresh()
        time.sleep(3)
        # 2.校验详情页信息正确
        try:
            product_name = self.GroupCategory.get_ele_text(ProductPage.detail_product_name_loc)
            self.assertEqual(product_name, 'C2_test', msg='C2详情页产品名称展示错误')
            product_filename = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_filename)
            self.assertEqual(product_filename, 'test_2D.dwg', msg='C2详情页产品文件名称展示错误')
            product_code = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_major)
            self.assertEqual(product_code, '大立面', msg='C2详情页产品主责专业展示错误')
            product_city = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_category)
            self.assertEqual(product_city, 'C2编辑分类', msg='C2详情页产品分类展示错误')
            product_category = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_function)
            self.assertEqual(product_category, '前场', msg='C2详情页产品功能分区展示错误')
            product_type = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_code)
            self.assertEqual(product_type, 'C2_auto_test_code', msg='详情页产品编码展示错误')
            product_value01 = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_value01)
            self.assertEqual(product_value01, 'test_C2', msg='C2详情页产品属性值1展示错误')
            product_value02 = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_value02)
            self.assertEqual(product_value02, 'C2_auto_enu', msg='C2详情页产品属性值2展示错误')
            file_value01 = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_file_01)
            self.assertEqual(file_value01, 'test-推送节点', msg="文件推送节点展示错误")
            file_value02 = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_file_02)
            self.assertEqual(file_value02, 'test-模块深度', msg="文件模块深度展示错误")
            file_value03 = self.GroupCategory.get_ele_text(ProductPage.C2_detail_product_file_03)
            self.assertEqual(file_value03, 'test-分供方', msg="文件分供方展示错误")
        finally:
            time.sleep(3)
            self.ProductPage.driver.close()
            self.ProductPage.driver.switch_to.window(windows[0])

    @BeautifulReport.add_test_img('test_C207_view_product')
    def test_C207_view_product(self):
        """
        C2产品查看页面:查看产品
        """
        time.sleep(3)
        self.ViewPage.click(ViewPage.View_loc)
        time.sleep(3)
        # 1.输入关键字点击搜索
        self.ViewPage.send_keys(ViewPage.key_loc, 'C2_test')
        time.sleep(1)
        self.ViewPage.click(ViewPage.search_loc)
        # 2.判断查询产品成功
        name = self.GroupCategory.get_ele_text(ViewPage.first_product)
        self.assertEqual(name, 'C2_test', msg='C2查看页筛选产品错误')
        time.sleep(3)

    @BeautifulReport.add_test_img('test_C208_del_product')
    def test_C208_del_product(self):
        """
        C2产品入库页面:删除产品
        """
        time.sleep(5)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击第二条产品删除按钮
        self.ProductPage.click(ProductPage.C2_del01_loc)
        # 2.点击确定按钮
        self.ProductPage.click(ProductPage.confirm_button_loc)
        time.sleep(2)
        # 3.判断删除成功
        self.ProductPage.refresh()
        time.sleep(1)
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertNotEqual(text, 'C2_test', msg="C2删除产品失败")

    @BeautifulReport.add_test_img('test_C209_del_groupCategory')
    def test_C209_del_groupCategory(self):
        """
        C2集团类目页面:删除集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        time.sleep(3)
        # 2.获取属地化模块最后一个类目名称
        text01 = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        # 3.鼠标移动到属地化模块最后一个类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        # 4.点击删除按钮
        self.GroupCategory.click(GroupCategoryPage.C2_last_Subclass_del_loc)
        time.sleep(3)
        # 5.点击确定按钮
        self.GroupCategory.click(GroupCategoryPage.category_del_confirm_loc)
        time.sleep(3)
        # 6.判断删除成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_DaLiMian_loc)
        self.assertNotEqual(text, text01, msg="删除集团类目失败")

    @BeautifulReport.add_test_img('test_C210_del_mould')
    def test_C210_del_mould(self):
        """
        C2模板管理页面:
        删除第一个模板
        """
        # 进入模板管理页面
        self.mouldmanage.click(MouldManagePage.mould_loc)
        time.sleep(3)
        # 1.获取第一个模板名称
        mould_name01 = self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc)
        # 2.鼠标移动到第一个模板
        self.mouldmanage.move_first_mould()
        # 3.点击删除按钮
        self.mouldmanage.click_first_mould_del()
        # 4.点击确认按钮
        self.mouldmanage.click_confirm_del_button()
        time.sleep(1)
        # 5.判断删除后第一个模板名称不为删除前第一个模板名称
        mould_name02 = self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc)
        self.assertNotEqual(mould_name02, mould_name01, msg='删除模板失败')

    @classmethod
    def tearDownClass(cls):
        cls.ProductPage.close()
