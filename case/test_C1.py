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
from page.grid_page import GridPage
from common.base import open_browser

from BeautifulReport import BeautifulReport


class TestC1(unittest.TestCase):

    def save_img(self, test_method):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file \
            ('{}/{}.png'.format(img_path, test_method))

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()  # 打开浏览器
        cls.login = LoginPage(cls.driver)  # 实例化LoginPage
        cls.login.open_url("http://memo.fangdichan.uat/")  # 打开登录地址
        cls.login.input_username("huangling1")
        cls.login.input_password("1")
        cls.login.click_submit()
        cls.mouldmanage = MouldManagePage(cls.driver)
        cls.GroupCategory = GroupCategoryPage(cls.driver)
        cls.RegionCategory = RegionCategoryPage(cls.driver)
        cls.ProductPage = ProductPage(cls.driver)
        cls.ViewPage = ViewPage(cls.driver)
        cls.GridPage = GridPage(cls.driver)

    @BeautifulReport.add_test_img('test_01_creat_mould')
    def test_01_creat_mould(self):
        """
        C1模板管理页面:
        创建模板
        """
        # 1.点击新增模板
        self.mouldmanage.click_add_mould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("测试模板")
        # 3.输入属性组名称
        self.mouldmanage.input_attrgrp_name("测试属性组")
        # 4.点击保存按钮
        self.mouldmanage.click_save_button()
        # 5.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 6.输入属性名称
        self.mouldmanage.input_attr_name("测试属性名称")
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
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), '测试模板', msg='创建模板失败')

    @BeautifulReport.add_test_img('test_02_edit_mould')
    def test_02_edit_mould(self):
        """
        C1模板管理页面:
        编辑模板
        """
        # 1.点击第一个模板
        self.mouldmanage.click_first_moould()
        time.sleep(1)
        # 2.输入模板名称
        self.mouldmanage.input_mould_name("编辑模板")
        # 3.点击编辑按钮
        self.mouldmanage.click_edit_button()
        # 4.输入属性组名称
        self.mouldmanage.input_attrgrp_name("编辑属性组")
        # 5.点击保存按钮
        self.mouldmanage.click_save_button()
        # 6.点击新增属性项按钮
        self.mouldmanage.click_add_attr_button()
        # 7.输入属性名称
        self.mouldmanage.input_attr_name("编辑属性名称")
        # 8.点击属性值类型下拉框
        self.mouldmanage.click_attr_type()
        time.sleep(1)
        # 9.选择属性值类型为枚举类型
        self.mouldmanage.click_eum_type()
        # 10.输入属性值
        self.mouldmanage.input_attr_value("auto_enu")
        # 11.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 12.点击提交按钮
        self.mouldmanage.click_submit_button()
        time.sleep(3)
        # 13.判断编辑后第一个模板名称为编辑模板名称
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.first_mould_loc), '编辑模板', msg='编辑模板失败')
        # 14.判断编辑后第一个模板属性组名称为编辑后属性组名称
        self.mouldmanage.click_first_moould()
        self.assertEqual(self.mouldmanage.get_ele_text(MouldManagePage.attrgrp_name_text_loc), '编辑属性组', msg='编辑属性组名称失败')

    @BeautifulReport.add_test_img('test_03_creat_groupCategory')
    def test_03_creat_groupCategory(self):
        """
        C1集团类目页面:
        创建属地化模块集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        # # 2.点击确认离开
        # self.GroupCategory.click_confirm_leave()
        time.sleep(3)
        # 3.鼠标移动到属地化模块
        self.GroupCategory.move_a_mouse(GroupCategoryPage.ShuDihua_loc)
        # 4.点击添加属地化模块二级类目按钮
        self.GroupCategory.click_add_ShuDihua_Subclass()
        # 5.输入分类编码
        self.GroupCategory.input_category_code('test_code-autotest')
        # 6.输入分类名称
        self.GroupCategory.input_category_name('测试分类')
        # 7.点击选择模板下拉框
        self.GroupCategory.click_mould_name_droplist()
        # 8.选择第一个模板
        # self.GroupCategory.click_first_mould()
        time.sleep(1)
        # 8.选择自定义模板
        self.GroupCategory.click(GroupCategoryPage.choose_mould_loc)
        # 9.点击是否有试用业态下拉框
        self.GroupCategory.click_needBusinessType_droplist()
        time.sleep(3)
        # 10.选择是有适用业态
        self.GroupCategory.click_needBusinessType()
        time.sleep(3)
        # 11.输入分类名称举例
        self.GroupCategory.input_product_name('测试产品名称')
        # 12.点击提交按钮
        self.GroupCategory.click_submit_button()
        time.sleep(3)
        # 13.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        self.assertEqual(text, '测试分类', msg='创建集团类目失败')
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        time.sleep(3)
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.inControl02_loc)
        self.assertEqual(text, '否', msg='默认管控值应为否')
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.isRequired02_loc)
        self.assertEqual(text, '是', msg='默认是否必填项应为是')
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.multiple02_loc)
        self.assertEqual(text, '否', msg='单选默认应为否')
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.useContact02_loc)
        self.assertEqual(text, '否', msg='名称生成项默认应为否')
        # text = self.GroupCategory.get_ele_text(GroupCategoryPage.needBusiness_loc)
        # self.assertEqual(text, '是', msg="是否有适用业态应为是")

    @BeautifulReport.add_test_img('test_04_edit_groupCategory')
    def test_04_edit_groupCategory(self):
        """
        C1集团类目页面:
        编辑属地化模块集团类目
        """
        # 1.鼠标移动到自定义类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        # 2.点击自定义类目编辑按钮
        self.GroupCategory.click(GroupCategoryPage.category_edit_loc)
        # 3.输入分类编码
        self.GroupCategory.input_category_code('test_C1edit_code')
        # 4.输入分类名称
        self.GroupCategory.input_category_name('编辑分类')
        # 5.输入分类名称举例
        self.GroupCategory.input_product_name('编辑产品名称')
        # 6.点击第一条属性项编辑按钮
        self.GroupCategory.click_attr01_edit()
        # 7.编辑第一条属性项名称
        self.GroupCategory.input_attr_edit_name("集团属性项01")
        # 8.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 9.勾选第一条属性项名称生成项勾选按钮
        self.GroupCategory.click(GroupCategoryPage.useContact01_edit_loc)
        # 10.点击第二条属性项编辑按钮
        self.GroupCategory.click(GroupCategoryPage.attr02_edit_loc)
        # 11.编辑第二条属性项名称
        self.GroupCategory.input_attr_edit_name("集团属性项02")
        # 12.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 13.勾选而二条属性项单选按钮
        self.GroupCategory.click(GroupCategoryPage.multiple02_edit_loc)
        # 14.勾选第二条属性项名称生成项按钮
        self.GroupCategory.click(GroupCategoryPage.useContact02_edit_loc)
        # 15.点击提交按钮
        self.GroupCategory.click_submit_button()
        time.sleep(3)
        # 16.判断创建成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        self.assertEqual(text, '编辑分类', msg='创建集团类目失败')
        # 查看创建集团类目详情
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        # 第一条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname01_loc)
        self.assertEqual(text, '集团属性项01', msg='第一条属性项名称错误')
        # 第一条属性项是否是名称生成项
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.useContact01_loc)
        self.assertEqual(text, '是', msg='第一条属性项应为名称生成项')
        # 第一条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.isRequired01_loc)
        self.assertEqual(text, '是', msg='第一条属性项因为必填项')
        # 第一条属性项格式是否为文本
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrtype01_loc)
        self.assertEqual(text, '文本', msg='第一条属性项格式应为文本')
        # 第二条属性项名称
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.attrname02_loc)
        self.assertEqual(text, '集团属性项02', msg='第二条属性项名称错误')
        # 第二条属性项是否是名称生成项
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.useContact02_loc)
        self.assertEqual(text, '是', msg='第二条属性项应为名称生成项')
        # 第二条属性项是否必填
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.isRequired02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为必填项')
        # 第一条属性项单选
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.multiple02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为单选')

    @BeautifulReport.add_test_img('test_05_edit_regionCategory')
    def test_05_edit_regionCategory(self):
        """
        C1地区类目维护页面:
        编辑地区类目
        """
        self.RegionCategory.click(RegionCategoryPage.RegionCategory_loc)
        time.sleep(3)
        # 1.点击地区类目维护
        self.RegionCategory.click(RegionCategoryPage.region_pull_loc)
        # 2.点击地区下拉框，选择北京太原地区
        self.GroupCategory.move_mouse(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJTY_loc)
        time.sleep(1)
        # 3.查看地区类目
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        time.sleep(1)
        # 4.点击提示确定按钮
        self.RegionCategory.click(RegionCategoryPage.confirm_button_loc)
        time.sleep(1)
        # 5.判断地区集团属性展示正确
        # 第一条属性项名称
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.attrname01_loc)
        self.assertEqual(text, '集团属性项01', msg='第一条属性项名称错误')
        # 第一条属性项是否是名称生成项
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.useContact01_loc)
        self.assertEqual(text, '是', msg='第一条属性项应为名称生成项')
        # 第一条属性项是否必填
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.isRequired01_loc)
        self.assertEqual(text, '是', msg='第一条属性项因为必填项')
        # 第一条属性项格式是否为文本
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.attrtype01_loc)
        self.assertEqual(text, '文本', msg='第一条属性项格式应为文本')
        # 第二条属性项名称
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.attrname02_loc)
        self.assertEqual(text, '集团属性项02', msg='第二条属性项名称错误')
        # 第二条属性项是否是名称生成项
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.useContact02_loc)
        self.assertEqual(text, '是', msg='第二条属性项应为名称生成项')
        # 第二条属性项是否必填
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.isRequired02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为必填项')
        # 第一条属性项单选
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.multiple02_loc)
        self.assertEqual(text, '是', msg='第二条属性项因为单选')
        # 6.点击编辑地区类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        self.RegionCategory.click(RegionCategoryPage.catgory_edit_loc)
        # 7.新增地区属性项01
        self.RegionCategory.click(RegionCategoryPage.add_attr_loc)
        # 8.输入地区属性项名称
        self.GroupCategory.input_attr_edit_name("地区属性项01")
        # 9.选择文本格式
        self.RegionCategory.click(RegionCategoryPage.datatype_pull_loc)
        time.sleep(3)
        self.GroupCategory.move_mouse(RegionCategoryPage.str_type_loc)
        self.RegionCategory.click(RegionCategoryPage.str_type_loc)
        # 10.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 11.新增地区属性项02
        self.RegionCategory.click(RegionCategoryPage.add_attr_loc)
        # 12.输入地区属性项名称
        self.GroupCategory.input_attr_edit_name("地区属性项02")
        # 13.选择枚举格式
        self.RegionCategory.click(RegionCategoryPage.attr_type_pull_loc)
        time.sleep(3)
        self.GroupCategory.move_mouse(RegionCategoryPage.enu_type_loc)
        self.RegionCategory.click(RegionCategoryPage.enu_type_loc)
        # 14.输入属性值
        self.RegionCategory.send_keys(RegionCategoryPage.input_attr_value_loc, 'test-region')
        # 15.点击确定按钮
        self.mouldmanage.click_add_attr_confirm_button()
        # 16.点击提交按钮
        self.GroupCategory.click_submit_button()
        # 17.判断编辑地区类目成功
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.attrname03_loc)
        self.assertEqual(text, '地区属性项01', msg='第三条属性项名称错误')
        text = self.GroupCategory.get_ele_text(RegionCategoryPage.attrname04_loc)
        self.assertEqual(text, '地区属性项02', msg='第四条属性项名称错误')

    @BeautifulReport.add_test_img('test_06_creat_product')
    def test_06_creat_product(self):
        """
        C1产品入库页面:
        新增集团产品
        """
        time.sleep(5)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击新增产品按钮
        self.ProductPage.click_add_product()
        time.sleep(3)
        # 2.点击分类下拉框
        self.ProductPage.click_choose_category()
        time.sleep(3)
        # 3.点击属地化模块
        self.ProductPage.click(GroupCategoryPage.ShuDihua_loc)
        # 4.点击编辑分类
        element = self.ProductPage.find_element(ProductPage.category_loc)
        self.driver.execute_script("arguments[0].click();", element)
        # 5.输入第一个属性值
        self.ProductPage.input_attr01_value("test_LHJT")
        # 6.点击第二个属性值下拉框
        self.ProductPage.click_attr02_value()
        # 7.选择属性值
        self.ProductPage.click(ProductPage.choose_attr02_value_loc)
        # 8.点击适用业态下拉框
        self.ProductPage.click_applicable()
        # 9.鼠标移动到住宅-独栋别墅业态
        self.GroupCategory.move_a_mouse(ProductPage.choose_applicable_loc)
        # 10.选择住宅-独栋别墅业态
        self.ProductPage.click(ProductPage.choose_applicable_loc)
        # 11.输入产品编码
        self.ProductPage.input_product_code("auto_test_code")
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
        # 15.上传2D文件
        element_2D = self.ProductPage.find_element(ProductPage.upload_2D_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_2D)
        element_2D.send_keys(file_path + 'test_2D.dwg')
        # 16.选择景观专业
        self.ProductPage.click(ProductPage.major2D_pull_loc)
        self.GroupCategory.move_mouse(ProductPage.major2D_loc)
        self.ProductPage.click(ProductPage.major2D_loc)
        # 17.选择G1-预案深度
        self.ProductPage.click(ProductPage.depth2D_pull_loc)
        self.GroupCategory.move_mouse(ProductPage.depth2D_loc)
        self.ProductPage.click(ProductPage.depth2D_loc)
        # 18.判断2D图纸上传成功
        upload_status = False
        for i in range(100):
            ele = self.ProductPage.find_element(ProductPage.upload_2D_status)
            value = ele.get_attribute('class')
            if value == 'percentage-ok':
                upload_status = True
                break
            else:
                time.sleep(3)
        self.assertTrue(upload_status, msg="文件一直上传中")
        text = self.GroupCategory.get_ele_text(ProductPage.file_name_2D_loc)
        self.assertEqual(text, 'test_2D.dwg', msg='上传2D文件展示名称错误')
        # 19.点击提交按钮
        element = self.ProductPage.find_element(ProductPage.submit_loc)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.GroupCategory.refresh()
        time.sleep(3)
        # 20.确认产品创建成功
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertEqual(text, '龙湖集团-test_LHJT-auto_enu', msg="创建产品失败")
        ele = self.ProductPage.find_element(ProductPage.product01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'status status_2', msg='创建后产品状态展示错误')

    @BeautifulReport.add_test_img('test_07_creat_zone_product')
    def test_07_creat_zone_product(self):
        """
        C1产品入库页面:
        新增地区产品
        """
        time.sleep(3)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击新增产品按钮
        self.ProductPage.click_add_product()
        time.sleep(3)
        # 2.选择北京太原
        self.ProductPage.click(ProductPage.region_pull_loc)
        self.GroupCategory.move_mouse(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJTY_loc)
        time.sleep(3)
        # 2.点击分类下拉框
        self.ProductPage.click_choose_category()
        time.sleep(3)
        # 3.点击属地化模块
        self.ProductPage.click(GroupCategoryPage.ShuDihua_loc)
        # 4.点击编辑分类
        element = self.ProductPage.find_element(ProductPage.category_loc)
        self.driver.execute_script("arguments[0].click();", element)
        # 5.输入第一个属性值
        self.ProductPage.input_attr01_value("test_ZONE")
        # 6.点击第二个属性值下拉框
        self.ProductPage.click_attr02_value()
        # 7.选择属性值
        self.ProductPage.click(ProductPage.choose_attr02_value_loc)
        # 8.输入第三项第四项属性值
        self.ProductPage.send_keys(ProductPage.attr03_value_loc, 'test')
        self.ProductPage.click(ProductPage.attr04_value_loc)
        self.ProductPage.click(ProductPage.choose_attr04_value_loc)
        # 9.点击适用业态下拉框
        self.ProductPage.click_applicable()
        # 10.鼠标移动到住宅-独栋别墅业态
        self.GroupCategory.move_a_mouse(ProductPage.choose_applicable_loc)
        # 11.选择住宅-独栋别墅业态
        self.ProductPage.click(ProductPage.choose_applicable_loc)
        # 12.输入产品编码
        self.ProductPage.input_product_code("zone_product_code")
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
        # 16.上传3D文件
        element_3D = self.ProductPage.find_element(ProductPage.upload_3Dfile_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_3D)
        self.ProductPage.move_mouse(ProductPage.upload_3Dfile_loc)
        time.sleep(2)
        upload_3D_loc = self.ProductPage.find_element(ProductPage.upload_3D_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", upload_3D_loc)
        upload_3D_loc.send_keys(file_path + 'test_3D.rvt')
        # 17.选择精装专业
        ele = self.ProductPage.find_element(ProductPage.major3D_pull_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        self.ProductPage.click(ProductPage.major3D_pull_loc)
        self.GroupCategory.move_mouse(ProductPage.major3D_loc)
        self.ProductPage.click(ProductPage.major3D_loc)
        # 18.选择G2-方案深度
        self.ProductPage.click(ProductPage.depth3D_pull_loc)
        self.GroupCategory.move_mouse(ProductPage.depth3D_loc)
        self.ProductPage.click(ProductPage.depth3D_loc)
        # 19.判断3D文件上传成功
        upload_status = False
        for i in range(100):
            ele = self.ProductPage.find_element(ProductPage.upload_3D_status)
            value = ele.get_attribute('class')
            if value == 'percentage-ok':
                upload_status = True
                break
            else:
                time.sleep(3)
        self.assertTrue(upload_status, msg="文件一直上传中")
        text = self.GroupCategory.get_ele_text(ProductPage.file_name_3D_loc)
        self.assertEqual(text, 'test_3D.rvt', msg='上传3D文件展示名称错误')
        # 20.关联集团产品
        self.ProductPage.click(ProductPage.relate_product_loc)
        self.ProductPage.click(ProductPage.relate_product)
        self.GroupCategory.move_mouse(ProductPage.relate_LHJT_product)
        self.ProductPage.click(ProductPage.relate_LHJT_product)
        time.sleep(1)
        self.ProductPage.send_keys(ProductPage.input_relate_product, 'LHJT-auto_enu')
        time.sleep(1)
        self.ProductPage.click(ProductPage.choose_relate_product)
        self.GroupCategory.move_mouse(ProductPage.confirm_loc)
        self.ProductPage.click(ProductPage.confirm_loc)
        # 21.校验关联产品展示
        text = self.GroupCategory.get_ele_text(ProductPage.relate_product_name)
        self.assertEqual(text, '龙湖集团-test_LHJT-auto_enu', msg='展示关联产品名称错误')
        text = self.GroupCategory.get_ele_text(ProductPage.relate_product_zone)
        self.assertEqual(text, '龙湖集团-龙湖集团', msg='展示关联产品地区错误')
        text = self.GroupCategory.get_ele_text(ProductPage.relate_product_feile)
        self.assertEqual(text, 'test_2D.dwg', msg='展示关联产品文件名称错误')
        # 22.点击提交按钮
        self.ProductPage.click(ProductPage.submit_loc)
        time.sleep(3)
        # 23.确认产品创建成功
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertEqual(text, '太原事业部-test_ZONE-auto_enu', msg="创建产品失败")
        ele = self.ProductPage.find_element(ProductPage.product01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'status status_2', msg='创建后产品状态展示错误')

    @BeautifulReport.add_test_img('test_08_detail_product')
    def test_08_detail_product(self):
        """
        C1产品入库页面:
        查看产品详情
        """
        time.sleep(3)
        # 1.点击第一条属性项名称进入产品详情页
        self.ProductPage.click(ProductPage.product01_name_loc)
        time.sleep(1)
        windows = self.ProductPage.driver.window_handles
        self.ProductPage.driver.switch_to.window(windows[-1])
        time.sleep(1)
        # 2.校验详情页信息正确
        try:
            product_name = self.GroupCategory.get_ele_text(ProductPage.detail_product_name_loc)
            self.assertEqual(product_name, '太原事业部-test_ZONE-auto_enu', msg='详情页产品名称展示错误')
            product_filename = self.GroupCategory.get_ele_text(ProductPage.detail_product_filename_loc)
            self.assertEqual(product_filename, 'test_3D.rvt', msg='详情页产品文件名称展示错误')
            product_code = self.GroupCategory.get_ele_text(ProductPage.detail_product_code_loc)
            self.assertEqual(product_code, 'zone_product_code', msg='详情页产品编码展示错误')
            product_city = self.GroupCategory.get_ele_text(ProductPage.detail_product_city_loc)
            self.assertEqual(product_city, '北京地区-太原事业部', msg='详情页产品地区展示错误')
            product_category = self.GroupCategory.get_ele_text(ProductPage.detail_product_category_loc)
            self.assertEqual(product_category, '编辑分类', msg='详情页产品分类展示错误')
            product_type = self.GroupCategory.get_ele_text(ProductPage.detail_product_type_loc)
            self.assertEqual(product_type, '住宅-独栋别墅', msg='详情页产品业态展示错误')
            product_value01 = self.GroupCategory.get_ele_text(ProductPage.detail_product_value01_loc)
            self.assertEqual(product_value01, 'test_ZONE', msg='详情页产品属性值1展示错误')
            product_value02 = self.GroupCategory.get_ele_text(ProductPage.detail_product_value02_loc)
            self.assertEqual(product_value02, 'auto_enu', msg='详情页产品属性值2展示错误')
            product_value03 = self.GroupCategory.get_ele_text(ProductPage.detail_product_value03_loc)
            self.assertEqual(product_value03, 'test', msg='详情页产品属性值3展示错误')
            product_value04 = self.GroupCategory.get_ele_text(ProductPage.detail_product_value04_loc)
            self.assertEqual(product_value04, 'test-region', msg='详情页产品属性值4展示错误')
        finally:
            time.sleep(3)
            self.ProductPage.driver.close()
            self.ProductPage.driver.switch_to.window(windows[0])

    @BeautifulReport.add_test_img('test_09_view_product')
    def test_09_view_product(self):
        """
        C1产品查看页面:查看产品
        """
        time.sleep(3)
        self.ViewPage.click(ViewPage.View_loc)
        time.sleep(3)
        # 1.输入关键字点击搜索
        self.ViewPage.send_keys(ViewPage.key_loc, '龙湖集团-test_LHJT-auto_enu')
        time.sleep(1)
        self.ViewPage.click(ViewPage.search_loc)
        # 2.判断查询产品成功
        name = self.GroupCategory.get_ele_text(ViewPage.first_product)
        self.assertEqual(name, '龙湖集团-test_LHJT-auto_enu', msg='查看页筛选产品错误')
        time.sleep(3)

    @BeautifulReport.add_test_img('test_10_del_product')
    def test_10_del_product(self):
        """
        C1产品入库页面:删除产品
        """
        time.sleep(5)
        self.ProductPage.click(ProductPage.product_loc)
        time.sleep(3)
        # 1.点击第二条产品删除按钮
        self.ProductPage.click(ProductPage.del02_loc)
        # 2.勾选关联删除产品
        self.ProductPage.click(ProductPage.relate_del_product)
        time.sleep(2)
        # 3.点击确定按钮
        self.ProductPage.click(MouldManagePage.add_attr_confirm_button_loc)
        time.sleep(1)
        self.ProductPage.click(ProductPage.confirm_button_loc)
        time.sleep(2)
        # 4.判断删除成功
        self.ProductPage.refresh()
        time.sleep(1)
        text = self.GroupCategory.get_ele_text(ProductPage.product01_name_loc)
        self.assertNotEqual(text, '龙湖集团-test_LHJT-auto_enu', msg="删除产品失败")
        self.assertNotEqual(text, '太原事业部-test_ZONE-auto_enu', msg="删除产品失败")

    @BeautifulReport.add_test_img('test_11_del_groupCategory')
    def test_11_del_groupCategory(self):
        """
        C1集团类目页面:删除集团类目
        """
        # 1.点击集团类目标签
        self.GroupCategory.click_Group_Category()
        time.sleep(3)
        # 2.获取属地化模块最后一个类目名称
        text01 = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        # 3.鼠标移动到属地化模块最后一个类目
        self.GroupCategory.move_a_mouse(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        # 4.点击删除按钮
        self.GroupCategory.click(GroupCategoryPage.last_Subclass_del_loc)
        time.sleep(3)
        # 5.点击确定按钮
        self.GroupCategory.click(GroupCategoryPage.category_del_confirm_loc)
        time.sleep(3)
        # 6.判断删除成功
        text = self.GroupCategory.get_ele_text(GroupCategoryPage.last_Subclass_ShuDihua_loc)
        self.assertNotEqual(text, text01, msg="删除集团类目失败")

    @BeautifulReport.add_test_img('test_12_del_mould')
    def test_12_del_mould(self):
        """
        C1模板管理页面:
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

    @BeautifulReport.add_test_img('test_13_creat_grid')
    def test_13_creat_grid(self):
        """
        C1产品网格页面:
        创建产品网格产品
        """
        time.sleep(5)
        # 1.进入产品网格页面
        self.GridPage.click(GridPage.Grid_loc)
        time.sleep(3)
        # 2.选择北京太原
        self.GridPage.click(GridPage.region_pull_loc)
        self.GroupCategory.move_mouse(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJ_loc)
        self.RegionCategory.click(RegionCategoryPage.BJTY_loc)
        # 3.勾选第一个产品网格
        self.GridPage.click(GridPage.grid01_loc)
        yetai = self.GroupCategory.get_ele_text(GridPage.grid01_type_loc)
        jushishu = self.GroupCategory.get_ele_text(GridPage.grid01_jushishu_loc)
        mianjiduan = self.GroupCategory.get_ele_text(GridPage.grid01_mianjiduan_loc)
        # 4.点击新增产品按钮
        self.GridPage.click(GridPage.add_product_loc)
        time.sleep(3)
        # 5.输入产品网格内容
        text = self.GroupCategory.get_ele_text(GridPage.type_loc)
        self.assertEqual(text, yetai, msg='产品网格新增默认带出业态错误')
        text = self.GroupCategory.get_ele_text(GridPage.mianjiduan_value)
        self.assertEqual(text, mianjiduan, msg='产品网格新增默认带出面积段错误')
        text = self.GroupCategory.get_ele_text(GridPage.jushishu_value)
        self.assertEqual(text, jushishu, msg='产品网格新增默认带出居室数错误')
        self.GridPage.click(GridPage.attr03_value_loc)
        self.GridPage.click(GridPage.choose_attr03_value_loc)
        self.GridPage.click(GridPage.attr04_value_loc)
        self.GridPage.click(GridPage.choose_attr04_value_loc)
        self.GridPage.click(GridPage.attr05_value_loc)
        self.GridPage.click(GridPage.choose_attr05_value_loc)
        self.GridPage.click(GridPage.attr07_value_loc)
        self.GridPage.click(GridPage.choose_attr07_value_loc)
        # 6.输入产品编码
        self.ProductPage.input_product_code("test-grid1")
        # 7.点击模型图纸
        self.ProductPage.click(ProductPage.mould_img_loc)
        # 8.上传缩略图
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        file_path = root_dir + "/file/"
        element = self.ProductPage.find_element(ProductPage.upload_img_loc)
        self.driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            element)
        element.send_keys(file_path + "test_grid.jpg")
        time.sleep(3)
        # 9.判断缩略图上传成功
        text = self.GroupCategory.get_ele_text(ProductPage.img_name_loc)
        self.assertEqual(text, 'test_grid.jpg', msg='上传缩略图失败')
        # 10.点击提交按钮
        self.ProductPage.click(ProductPage.submit_loc)
        time.sleep(3)
        # 11.判断新增产品网格成功
        text = self.GroupCategory.get_ele_text(GridPage.grid01_name_loc)
        self.assertEqual(text, '太原事业部-105-114-3-2-2-3面宽-2T4-Z1-T2专属', msg='产品网格产品名称展示错误')
        ele = self.GridPage.find_element(GridPage.grid01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'proStatus proStatus_2', msg='产品网格产品状态展示错误')

    @BeautifulReport.add_test_img('test_14_change_grid')
    def test_14_change_grid(self):
        """
        C1产品网格页面:
        变更产品状态
        """
        # # 1.进入产品网格页面
        # time.sleep(5)
        # self.GridPage.click(GridPage.Grid_loc)
        # time.sleep(3)
        # # 2.选择北京太原
        # self.GridPage.click(GridPage.region_pull_loc)
        # self.GroupCategory.move_mouse(RegionCategoryPage.BJ_loc)
        # self.RegionCategory.click(RegionCategoryPage.BJ_loc)
        # self.RegionCategory.click(RegionCategoryPage.BJTY_loc)
        # 1.变更产品状态
        self.GroupCategory.move_mouse(GridPage.grid01_name_loc)
        time.sleep(1)
        self.GridPage.click(GridPage.change_status_loc)
        time.sleep(1)
        # 2.判断变更状态成功
        ele = self.GridPage.find_element(GridPage.grid01_status_loc)
        status = ele.get_attribute('class')
        self.assertEqual(status, 'proStatus proStatus_1', msg='产品网格产品状态展示错误')

    @BeautifulReport.add_test_img('test_15_del_grid')
    def test_15_del_grid(self):
        """
        C1产品网格页面:
        删除产品
        """
        # # 1.进入产品网格页面
        # time.sleep(5)
        # self.GridPage.click(GridPage.Grid_loc)
        # time.sleep(3)
        # # 2.选择北京太原
        # self.GridPage.click(GridPage.region_pull_loc)
        # self.GroupCategory.move_mouse(RegionCategoryPage.BJ_loc)
        # self.RegionCategory.click(RegionCategoryPage.BJ_loc)
        # self.RegionCategory.click(RegionCategoryPage.BJTY_loc)
        # 1.删除产品
        self.GridPage.refresh()
        time.sleep(3)
        self.GroupCategory.move_mouse(GridPage.grid01_name_loc)
        time.sleep(1)
        self.GridPage.click(GridPage.grid01_del_loc)
        self.GridPage.click(GridPage.grid_del_confirm_loc)
        time.sleep(1)
        # 2.删除产品成功
        text = self.GroupCategory.get_ele_text(GridPage.grid01_sapce_loc)
        self.assertEqual(text, '', msg='产品网格删除产品失败')

    @classmethod
    def tearDownClass(cls):
        cls.ProductPage.close()
# if __name__ == '__main__':
#
# TestC1