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


class TestVR(unittest.TestCase):
    component_name = ""

    def save_img(self, test_method):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/img'
        print(img_path)
        self.driver.get_screenshot_as_file \
            ('{}/{}.png'.format(img_path, test_method))

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()  # 打开浏览器
        cls.login = LoginPage(cls.driver)  # 实例化LoginPage
        cls.login.open_url("http://kit.longfor.uat/")  # 打开登录地址
        cls.login.input_username("gaoxw")
        cls.login.input_password("1")
        cls.login.click_submit()
        cls.mouldmanage = MouldManagePage(cls.driver)
        cls.GroupCategory = GroupCategoryPage(cls.driver)
        cls.RegionCategory = RegionCategoryPage(cls.driver)
        cls.ProductPage = ProductPage(cls.driver)
        cls.ViewPage = ViewPage(cls.driver)

    @BeautifulReport.add_test_img('test_VR01_creat_mould')
    def test_VR01_creat_mould(self):
        """
        VR模板管理页面:
        创建模板
        """
        # 1.点击新增模板
        self.mouldmanage.click_add_mould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("测试VR模板")
        # 3.输入属性组名称
        self.mouldmanage.input_attrgrp_name("测试VR属性组")
        # 4.点击保存按钮
        self.mouldmanage.click_save_button()
        # 5.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 6.输入属性名称
        self.mouldmanage.input_attr_name("测试VR属性名称")
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
        self.mouldmanage.refresh()
        time.sleep(3)
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), '测试VR模板', msg='创建模板失败')

    @BeautifulReport.add_test_img('test_VR02_edit_mould')
    def test_VR02_edit_mould(self):
        """
        VR模板管理页面:
        编辑模板
        """
        # 1.点击第一个模板
        self.mouldmanage.click_first_moould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("VR编辑模板")
        # 3.点击编辑按钮
        self.mouldmanage.click_edit_button()
        # 4.输入属性组名称
        self.mouldmanage.input_attrgrp_name("VR编辑属性组")
        # 5.点击保存按钮
        self.mouldmanage.click_save_button()
        # 6.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 7.输入属性名称
        self.mouldmanage.input_attr_name("VR编辑属性名称")
        # 8.点击属性值类型下拉框
        self.mouldmanage.click_attr_type()
        time.sleep(1)
        # 9.选择属性值类型为枚举类型
        self.mouldmanage.click_eum_type()
        # 10.输入属性值
        self.mouldmanage.input_attr_value("VR_auto_enu")
        # 11.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 12.点击提交按钮
        self.mouldmanage.click_submit_button()
        time.sleep(3)
        # 13.判断编辑后第一个模板名称为编辑模板名称
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), 'VR编辑模板', msg='编辑模板失败')
        # 14.判断编辑后第一个模板属性组名称为编辑后属性组名称
        self.mouldmanage.click_first_moould()
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.attrgrp_name_text_loc), 'VR编辑属性组',
                         msg='编辑属性组名称失败')

    @BeautifulReport.add_test_img('test_VR03_creat_groupCategory')
    def test_VR03_creat_groupCategory(self):
        """
        VR集团类目页面:
        创建属地化模块集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        # # 2.点击确认离开
        # self.GroupCategory.click_confirm_leave()
        time.sleep(3)
        # 3.鼠标移动到虚拟仿真模块
        self.GroupCategory.move_a_mouse(GroupCategoryPage.XuNiFangZhen_loc)
        # 4.点击添加属地化模块二级类目按钮
        self.GroupCategory.click(GroupCategoryPage.add_XuNiFangZhen_Subclass_loc)
        # 5.输入分类编码
        self.GroupCategory.input_category_code('test_code-VR')
        # 6.输入分类名称
        self.GroupCategory.input_category_name('VR测试分类')
        # 7.点击选择模板下拉框
        self.GroupCategory.click_mould_name_droplist()
        # 8.选择第一个模板
        # self.GroupCategory.click_first_mould()
        time.sleep(1)
        # 8.选择自定义模板
        self.GroupCategory.click(GroupCategoryPage.choose_VRmould_loc)
        # 9.输入分类名称举例
        self.GroupCategory.input_product_name('VR测试产品名称')
        # 10.点击提交按钮
        self.GroupCategory.click_submit_button()
        self.GroupCategory.refresh()
        time.sleep(3)
        # 11.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        self.assertEqual(text, 'VR测试分类', msg='创建C2集团类目失败')
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        time.sleep(3)
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_isRequired02_loc)
        self.assertEqual(text, '是', msg='默认是否必填项应为是')
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_multiple02_loc)
        self.assertEqual(text, '否', msg='单选默认应为否')

    @BeautifulReport.add_test_img('test_VR04_edit_groupCategory')
    def test_VR04_edit_groupCategory(self):
        """
        VR集团类目页面:
        编辑虚拟仿真模块集团类目
        """
        # 1.鼠标移动到自定义类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        # 2.点击自定义类目编辑按钮
        self.GroupCategory.click(GroupCategoryPage.category_VRedit_loc)
        # 3.输入分类编码
        self.GroupCategory.input_category_code('test_VRedit_code')
        # 4.输入分类名称
        self.GroupCategory.input_category_name('VR编辑分类')
        # 5.输入分类名称举例
        self.GroupCategory.input_product_name('VR编辑产品名称')
        # 6.点击第一条属性项编辑按钮
        self.GroupCategory.click(GroupCategoryPage.VR_attr01_edit_loc)
        # 7.编辑第一条属性项名称
        self.GroupCategory.input_attr_edit_name("VR集团属性项01")
        # 8.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 9.点击第二条属性项编辑按钮
        self.GroupCategory.click(GroupCategoryPage.VR_attr02_edit_loc)
        # 10.编辑第二条属性项名称
        self.GroupCategory.input_attr_edit_name("VR集团属性项02")
        # 11.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 12.勾选而二条属性项单选按钮
        self.GroupCategory.click(GroupCategoryPage.VR_multiple02_edit_loc)
        # 13.点击提交按钮
        self.GroupCategory.click_submit_button()
        time.sleep(3)
        # 14.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        self.assertEqual(text, 'VR编辑分类', msg='创建集团类目失败')
        # 查看创建集团类目详情
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        # 第一条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname01_loc)
        self.assertEqual(text, 'VR集团属性项01', msg='第一条属性项名称错误')
        # 第一条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_isRequired01_loc)
        self.assertEqual(text, '是', msg='第一条属性项因为必填项')
        # 第一条属性项格式是否为文本
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_attrtype01_loc)
        self.assertEqual(text, '文本', msg='第一条属性项格式应为文本')
        # 第二条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname02_loc)
        self.assertEqual(text, 'VR集团属性项02', msg='第二条属性项名称错误')
        # 第二条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_isRequired02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为必填项')
        # 第二条属性项单选
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.VR_multiple02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为单选')

    @BeautifulReport.add_test_img('test_VR05_creat_product')
    def test_VR05_creat_product(self):
        """
        VR产品入库页面:
        新增集团产品
        """
        global component_name
        time.sleep(5)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击新增产品按钮
        self.ProductPage.click_add_product()
        time.sleep(3)
        # 2.点击分类下拉框
        self.ProductPage.click_choose_category()
        time.sleep(3)
        # 3.点击虚拟仿真模块
        self.ProductPage.click(GroupCategoryPage.XuNiFangZhen_loc)
        # 4.点击VR编辑分类
        element = self.ProductPage.find_element(ProductPage.VR_category_loc)
        self.driver.execute_script("arguments[0].click();", element)
        # 5.输入第一个属性值
        self.ProductPage.input_attr01_value("test_VR")
        # 6.点击第二个属性值下拉框
        self.ProductPage.click_attr02_value()
        # 7.选择属性值
        self.ProductPage.click(ProductPage.VR_choose_attr02_value_loc)
        # # 8.点击适用业态下拉框
        # self.ProductPage.click_applicable()
        # # 9.鼠标移动到住宅-独栋别墅业态
        # self.GroupCategory.move_a_mouse(ProductPage.choose_applicable_loc)
        # # 10.选择住宅-独栋别墅业态
        # self.ProductPage.click(ProductPage.choose_applicable_loc)
        # 11.输入产品名称
        self.ProductPage.send_keys(ProductPage.VR_product_name_loc, "VR_test")
        # 12.点击模型图纸
        self.ProductPage.click(ProductPage.mould_img_loc)
        # 13.上传缩略图
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        file_path = root_dir + "/file/"
        element = self.ProductPage.find_element(ProductPage.upload_img_loc)
        self.driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            element)
        element.send_keys(file_path + "test_img.jpg")
        time.sleep(3)
        # 14.判断缩略图上传成功
        text = self.GroupCategory.get_ele_text(ProductPage.img_name_loc)
        self.assertEqual(text, 'test_img.jpg', msg='上传缩略图失败')
        # # 15.上传3D文件夹
        # element_3D = self.ProductPage.find_element(ProductPage.upload_3Dfile_loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element_3D)
        # self.ProductPage.move_mouse(ProductPage.upload_3Dfile_loc)
        # time.sleep(2)
        # upload_folder_loc = self.ProductPage.find_element(ProductPage.upload_folder_loc)
        # # self.driver.execute_script("arguments[0].scrollIntoView();", upload_folder_loc)
        # upload_folder_loc.send_keys(file_path + 'folder')
        # time.sleep(10)
        # # 16.判断3D文件上传成功
        # upload_status = False
        # for i in range(100):
        #     ele01 = self.ProductPage.find_element(ProductPage.VR_3D01_status)
        #     value01 = ele01.get_attribute('class')
        #     ele02 = self.ProductPage.find_element(ProductPage.VR_3D02_status)
        #     value02 = ele02.get_attribute('class')
        #     if value01 == 'percentage-ok' and value02 == 'percentage-ok':
        #         upload_status = True
        #         break
        #     else:
        #         time.sleep(3)
        # self.assertTrue(upload_status, msg="文件一直上传中")
        # text01 = self.GroupCategory.get_ele_text(ProductPage.VR_file_name_3D01_loc)
        # self.assertEqual(text01, 'file01.rvt', msg='上传3D文件展示名称错误')
        # text02 = self.GroupCategory.get_ele_text(ProductPage.VR_file_name_3D02_loc)
        # self.assertEqual(text02, 'file02.rvt', msg='上传3D文件展示名称错误')
        # 17.点击关联元件
        self.ProductPage.click(ProductPage.component_loc)
        self.ProductPage.click(ProductPage.VR_component_loc)
        # 18.关联第一个元件
        self.ProductPage.click(ProductPage.first_component_loc)
        self.GroupCategory.move_mouse(ProductPage.VR_confirm_loc)
        self.ProductPage.click(ProductPage.VR_confirm_loc)
        component_name = self.GroupCategory.get_ele_text(ProductPage.component_name)
        # 19.点击提交按钮
        element = self.ProductPage.find_element(ProductPage.submit_loc)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.GroupCategory.refresh()
        time.sleep(3)
        # 20.确认产品创建成功
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertEqual(text, 'VR_test', msg="创建产品失败")
        ele = self.ProductPage.find_element(ProductPage.product01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'status status_2', msg='创建后产品状态展示错误')

    @BeautifulReport.add_test_img('test_VR06_detail_product')
    def test_VR06_detail_product(self):
        """
        VR产品入库页面:
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
            self.assertEqual(product_name, 'VR_test', msg='VR详情页产品名称展示错误')
            # folder_name = self.GroupCategory.get_ele_text(ProductPage.VR_folder_name)
            # self.assertEqual(folder_name, 'folder', msg='VR详情页产品文件夹名称展示错误')
            product_city = self.GroupCategory.get_ele_text(ProductPage.VR_detail_product_city_loc)
            self.assertEqual(product_city, '龙湖集团-龙湖集团', msg='VR详情页产品地区展示错误')
            product_category = self.GroupCategory.get_ele_text(ProductPage.VR_detail_product_category_loc)
            self.assertEqual(product_category, 'VR编辑分类', msg='VR详情页产品分类展示错误')
            product_value01 = self.GroupCategory.get_ele_text(ProductPage.VR_detail_product_value01)
            self.assertEqual(product_value01, 'test_VR', msg='C2详情页产品属性值1展示错误')
            product_value02 = self.GroupCategory.get_ele_text(ProductPage.VR_detail_product_value02)
            self.assertEqual(product_value02, 'VR_auto_enu', msg='C2详情页产品属性值2展示错误')
            # 3.点击产品组成，查看挂接元件展示
            self.ProductPage.click(ProductPage.VR_product_component)
            ele = self.ProductPage.find_element(ProductPage.VR_product_component_name)
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            name = self.GroupCategory.get_ele_text(ProductPage.VR_product_component_name)
            self.assertEqual(name, component_name, msg="挂接元件名称展示错误")
        finally:
            time.sleep(3)
            self.ProductPage.driver.close()
            self.ProductPage.driver.switch_to.window(windows[0])

    @BeautifulReport.add_test_img('test_VR07_del_product')
    def test_VR07_del_product(self):
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
        self.assertNotEqual(text, 'VR_test', msg="VR删除产品失败")

    @BeautifulReport.add_test_img('test_VR08_del_groupCategory')
    def test_VR08_del_groupCategory(self):
        """
        VR集团类目页面:删除集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        time.sleep(3)
        # 2.获取属地化模块最后一个类目名称
        text01 = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        # 3.鼠标移动到属地化模块最后一个类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        # 4.点击删除按钮
        self.GroupCategory.click(GroupCategoryPage.VR_last_Subclass_del_loc)
        time.sleep(3)
        # 5.点击确定按钮
        self.GroupCategory.click(GroupCategoryPage.category_del_confirm_loc)
        time.sleep(3)
        # 6.判断删除成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_XuNiFangZhen_loc)
        self.assertNotEqual(text, text01, msg="删除集团类目失败")

    @BeautifulReport.add_test_img('test_VR09_del_mould')
    def test_VR09_del_mould(self):
        """
        VR模板管理页面:
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
