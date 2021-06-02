from common.base import Base


class ProductPage(Base):
    product_loc = ("xpath", "//*[contains(text(),'产品入库')]")  # 产品入库菜单
    add_product_loc = ("xpath", "//*[contains(text(),'新增')]")  # 新增产品按钮
    region_pull_loc = (
        'xpath', "//*[@id='scrollContent']/div/div/section/div[1]/div/form/div[1]/div/div/div/span/span/i")  # 地区下拉框
    choose_category_loc = ("xpath", "//input[@placeholder='请选选择分类']")  # 选则分类
    category_loc = ("xpath", "//*[contains(text(),'编辑分类')]/../label/span[1]/input")  # 选则编辑分类
    attr01_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input")  # 第一个属性值
    attr02_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/input")  # 第二个属性值
    choose_attr02_value_loc = ("xpath", "//*[contains(text(),'auto_enu')]")  # 选择第二个属性值
    attr03_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[3]/td[2]/div/div/div/input")  # 第三个属性值
    attr04_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[4]/td[2]/div/div/div/div/input")  # 第四个属性值
    choose_attr04_value_loc = ("xpath", "//*[contains(text(),'test-region')]")  # 选择第四个属性值
    applicable_loc = ("xpath", "//div[@class='el-select__tags']/../div[2]/input")  # 点击适用业态下拉框
    choose_applicable_loc = ("xpath", "//*[contains(text(),'住宅-独栋别墅')]")  # 选择业态
    product_code_loc = ("xpath", "//input[@placeholder='请输入产品编码']")  # 产品编码输入框
    save_loc = ("xpath", "//*[contains(text(),'暂存')]")  # 暂存按钮
    submit_loc = ("xpath", "//*[contains(text(),'提交')]")  # 提交按钮
    product01_name_loc = ("xpath", "//table[@class='el-table__body']/tbody/tr[1]/td[3]/div/div/div[1]/a")  # 第一条产品名称
    product01_status_loc = ("xpath", "//table[@class='el-table__body']/tbody/tr[1]/td[2]/div/div/div[2]")  # 第一条产品状态
    del02_loc = ("xpath", "//table[@class='el-table__body']/tbody/tr[2]/td[4]/div/div/button[2]")  # 第二条产品删除按钮
    relate_del_product = ("xpath",
                          "//*[@id='scrollContent']/div/div/section/section/section[4]/div/div/div[2]/div/form/div[2]/div/div/p/label/span[1]/span")  # 勾选关联删除产品
    confirm_button_loc = ('xpath', "//*[contains(text(),'确定')]")  # 删除确定按钮
    mould_img_loc = ('xpath', "//*[contains(text(),'模型图纸')]")  # 模型图纸
    upload_img_loc = ("xpath", "//section[@class='imgUpload']/div/div/input")  # 上传缩略图按钮
    img_name_loc = ("xpath", "//section[@class='imgUpload']/div/ul/li[1]/div/div[2]")  # 缩略图名称
    upload_2D_loc = ("xpath", "//*[contains(text(),'支持扩展名：dwg，dxf')]/../div[1]/div/div/div/div/input")  # 上传2D文件
    upload_3Dfile_loc = ("xpath", "//*[contains(text(),'支持扩展名：.rvt,.max,.zip,.rar')]/../div[1]/div/div/button/span")  # 上传3D文件
    upload_3D_loc = ("xpath", "/html/body/ul[1]/li[1]/div/div/div/input")  # 上传3D文件
    upload_folder_loc = ("xpath", "//div[@class='uploadBox']/input")  # 上传3D文件夹
    major2D_pull_loc = ("xpath",
                        "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[2]/div/div/div/div[2]/span/span/i")  # 2D专业下拉框
    major3D_pull_loc = ("xpath",
                        "//*[@id='pane-imgM']/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[2]/span/span/i")  # 3D专业下拉框
    major2D_loc = ('xpath', "//*[contains(text(),'景观')]")  # 选择景观专业
    major3D_loc = ('xpath', "//*[contains(text(),'精装')]")  # 选择精装专业
    depth2D_pull_loc = ("xpath",
                        "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[3]/div/div/div/div/span/span/i")  # 2D模块深度下拉框
    depth3D_pull_loc = ("xpath",
                        "//*[@id='pane-imgM']/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div[1]/span/span/i")  # 3D模块深度下拉框
    depth2D_loc = ('xpath', "//*[contains(text(),'G1-轮廓')]")  # 选择G1-预案深度
    depth3D_loc = ('xpath', "//*[contains(text(),'G2-方案')]")  # 选择G2-方案深度
    upload_2D_status = ('xpath',
                        "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div/span")  # 2D图纸上传状态
    upload_3D_status = ('xpath',
                        "//*[@id='pane-imgM']/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div/span")  # 3D图纸上传状态
    file_name_2D_loc = ('xpath',
                        "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div")  # 获取2D文件名称
    file_name_3D_loc = ('xpath',
                        "//*[@id='pane-imgM']/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div")  # 获取3D文件名称

    relate_product_loc = ('xpath', "//*[contains(text(),'关联产品')]")  # 关联产品
    relate_product = ('xpath', "//*[contains(text(),'关联产品-已入库产品')]/../div/span")  # 关联产品
    relate_LHJT_product = ('xpath', "//*[contains(text(),'关联集团产品')]")  # 点击关联集团产品按钮
    input_relate_product = ("xpath", "//input[@placeholder='请输入产品名称']")  # 请输入产品名称输入框
    relate_product_name = (
        "xpath", "//*[contains(text(),'关联产品-已入库产品')]/../../div[2]/div[3]/table/tbody/tr[1]/td[1]/div/span")
    relate_product_zone = (
        "xpath", "//*[contains(text(),'关联产品-已入库产品')]/../../div[2]/div[3]/table/tbody/tr[1]/td[2]/div/span")
    relate_product_feile = (
        "xpath", "//*[contains(text(),'关联产品-已入库产品')]/../../div[2]/div[3]/table/tbody/tr[1]/td[3]/div")
    choose_relate_product = (
        'xpath', "//div[@class='proListWrapHasData']/div[1]/div/div[2]/label/span[1]/span")  # 勾选关联产品
    confirm_loc = ('xpath', "//*[@id='pane-config']/section/div[3]/div/div[3]/span/button[2]")

    detail_product_name_loc = ("xpath", "//div[@class='s-right']/div/div[1]/div/div/div/div[2]")  # 详情页产品名称
    detail_product_filename_loc = ("xpath", "//*[@id='pane-0']/div/div[2]/div/div/div[2]/div/div[1]")  # 详情页产品三维模型名称
    detail_product_code_loc = ("xpath", "//div[@class='detail-content']/div[1]/div/div[2]")  # 详情页产品编码
    detail_product_city_loc = ("xpath", "//div[@class='detail-content']/div[2]/div/div[2]")  # 详情页产品地区
    detail_product_category_loc = ("xpath", "//div[@class='detail-content']/div[3]/div/div[2]")  # 详情页产品分类
    detail_product_type_loc = ("xpath", "//div[@class='detail-content']/div[4]/div/div[2]")  # 详情页产品业态
    detail_product_value01_loc = ("xpath", "//div[@class='detail-content']/div[5]/div/div[2]")  # 详情页产品属性值1
    detail_product_value02_loc = ("xpath", "//div[@class='detail-content']/div[6]/div/div[2]")  # 详情页产品属性值2
    detail_product_value03_loc = ("xpath", "//div[@class='detail-content']/div[7]/div/div[2]")  # 详情页产品属性值3
    detail_product_value04_loc = ("xpath", "//div[@class='detail-content']/div[8]/div/div[2]")  # 详情页产品属性值4

    ####################################################################################################################
    C2_major_pull = ("xpath", "//input[@placeholder='请选择']")  # 主责专业下拉框
    C2_category_pull = ("xpath", "//input[@placeholder='请选选择分类']")  # 选择分类下拉框
    C2_category_loc = ("xpath", "//*[contains(text(),'C2编辑分类')]/../label/span[1]/input")  # 选则C2编辑分类
    C2_choose_attr02_value_loc = ("xpath", "//*[contains(text(),'C2_auto_enu')]")  # 选择第二个属性值
    C2_function_pull = ("xpath", "//input[@placeholder='请选择功能分区']")  # 选择功能分区下拉框
    C2_choose_function_loc = ("xpath", "//*[contains(text(),'前场')]")  # 选择业态
    C2_product_name_loc = ("xpath", "//input[@placeholder='例：C2编辑产品名称']")  # 产品名称输入框
    C2_upload_2D_loc = ("xpath", "//*[contains(text(),'2D图纸:')]/../../div[2]/div[2]/div/div/div/div/input")  # 上传2D文件
    C2_upload_2D_status = ("xpath",
                           "//*[contains(text(),'2D图纸:')]/../../div[2]/div[4]/div/div[3]/table/tbody/tr/td[1]/div/div/span")  # 2D图纸上传状态
    C2_file_name_2D_loc = ('xpath',
                           "//*[contains(text(),'2D图纸:')]/../../div[2]/div[4]/div/div[3]/table/tbody/tr/td[1]/div/div")  # 获取2D文件名
    C2_detail_product_major = ("xpath", "//div[@class='detail-content']/div[1]/div/div[2]")  # 详情页主责专业
    C2_detail_product_category = ("xpath", "//div[@class='detail-content']/div[2]/div/div[2]")  # 详情页分类
    C2_detail_product_function = ("xpath", "//div[@class='detail-content']/div[3]/div/div[2]")  # 详情页功能分区
    C2_detail_product_code = ("xpath", "//div[@class='detail-content']/div[4]/div/div[2]")  # 详情页产品编码
    C2_detail_product_value01 = ("xpath", "//div[@class='detail-content']/div[5]/div/div[2]")  # 详情页产品属性值1
    C2_detail_product_value02 = ("xpath", "//div[@class='detail-content']/div[6]/div/div[2]")  # 详情页产品属性值2
    C2_detail_product_filename = ("xpath", "//*[@id='pane-0']/div/div[1]/div/div/div[1]")  # 详情页产品2D建筑维模型名称
    C2_detail_product_file_01 = ("xpath", "//*[@id='pane-0']/div/div[1]/div/div/span[1]")  # 详情页产品2D建筑维模型推送节点
    C2_detail_product_file_02 = ("xpath", "//*[@id='pane-0']/div/div[1]/div/div/span[2]")  # 详情页产品2D建筑维模型模块深度
    C2_detail_product_file_03 = ("xpath", "//*[@id='pane-0']/div/div[1]/div/div/span[3]")  # 详情页产品2D建筑维模型分供方
    C2_del01_loc = ("xpath", "//table[@class='el-table__body']/tbody/tr[1]/td[4]/div/div/button[2]")  # 第二条产品删除按钮

    ###################################################################################################################
    VR_category_loc = ("xpath", "//*[contains(text(),'VR编辑分类')]/../label/span[1]/input")  # 选则VR编辑分类
    VR_choose_attr02_value_loc = ("xpath", "//*[contains(text(),'VR_auto_enu')]")  # 选择第二个属性值
    VR_product_name_loc = ("xpath", "//input[@placeholder='例：VR编辑产品名称']")  # VR产品名称输入框
    VR_detail_product_city_loc = ("xpath", "//div[@class='detail-content']/div[1]/div/div[2]")  # 详情页产品地区
    VR_detail_product_category_loc = ("xpath", "//div[@class='detail-content']/div[2]/div/div[2]")  # 详情页产品分类
    VR_detail_product_value01 = ("xpath", "//div[@class='detail-content']/div[3]/div/div[2]")  # 详情页产品属性值1
    VR_detail_product_value02 = ("xpath", "//div[@class='detail-content']/div[4]/div/div[2]")  # 详情页产品属性值2
    VR_file_name_3D01_loc = ('xpath',
                             "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div")  # 获取3D文件名称
    VR_file_name_3D02_loc = ('xpath',
                             "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/div")  # 获取3D文件名称
    VR_3D01_status = ('xpath',
                      "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/span")  # 3D图纸上传状态
    VR_3D02_status = ('xpath',
                      "//*[@id='pane-imgM']/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/div/span")  # 3D图纸上传状态
    VR_folder_name = ('xpath', "//*[@id='pane-0']/div/div[2]/div/div/div/div/div[1]/span")  # 文件夹名字
    component_loc = ('xpath', "//*[contains(text(),'挂接元件')]")  # 挂接元件
    VR_component_loc = ('xpath', "//*[@id='pane-zhi']/div/div[1]/button")  # 挂接元件
    first_component_loc = ('xpath',
                           "//*[@id='pane-zhi']/div/section/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/label/span/span")  # 挂接第一个元件
    VR_confirm_loc = ('xpath', "//*[@id='pane-zhi']/div/section/div/div/div[2]/div/div[2]/div[2]/div[2]/button")
    component_name = ('xpath', "//*[@id='pane-zhi']/div/div[2]/div/div[2]/span")
    VR_product_component = ('xpath', "//*[contains(text(),'产品组成')]")  # 产品组成
    VR_product_component_name = ('xpath', "//*[@id='pane-second2']/div/div/p/span")  # 产品组成

    def click_add_product(self):
        """
        点击新增产品按钮
        """
        self.click(self.add_product_loc)

    def click_choose_category(self):
        """
        点击分类下拉框
        :return:
        """
        self.click(self.choose_category_loc)

    def input_attr01_value(self, text):
        """
        输入第一个属性值
        :return:
        """
        self.send_keys(self.attr01_value_loc, text)

    def click_attr02_value(self):
        """
        点击第二个属性值
        :return:
        """
        self.click(self.attr02_value_loc)

    def click_applicable(self):
        """
        点击适用业态下拉框
        :return:
        """
        self.click(self.applicable_loc)

    def input_product_code(self, text):
        """
        输入产品编码
        :return:
        """
        self.send_keys(self.product_code_loc, text)

    def click_save(self):
        """
        点击暂存按钮
        :return:
        """
        self.click(self.save_loc)
