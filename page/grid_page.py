from common.base import Base


class GridPage(Base):
    """封装表现层: 制作定位器"""
    Grid_loc = ("xpath", "//*[contains(text(),'产品网格')]")  # 产品网格标签
    region_pull_loc = ('xpath', "//input[@placeholder='请选择地区']")  # 地区下拉框
    grid01_loc = (
        "xpath",
        "//*[@id='scrollContent']/div/div[4]/table/tr[1]/td[3]/div/div[1]/div[1]/div/label/span/span")  # 勾选第一个产品网格
    grid01_type_loc = ("xpath", "//*[contains(text(),'居室数')]/../div[3]/div/div[1]")  # 第一个产品网格业态
    grid01_mianjiduan_loc = ("xpath", "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[1]")  # 第一个产品网格面积段
    grid01_jushishu_loc = ("xpath", "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[2]")  # 第一个产品网格面积段
    grid01_name_loc = (
        "xpath",
        "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[3]/div/div[2]/div[1]/div/div[2]/p[1]")  # 第一个产品名称
    grid01_sapce_loc = (
        "xpath",
        "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[3]/div/div")  # 第一个产品网格
    grid01_status_loc = (
        "xpath",
        "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[3]/div/div[2]/div[1]/div/div[2]/div")  # 第一个产品状态
    grid01_del_loc = (
        "xpath",
        "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[3]/div/div[2]/div[1]/div/div[2]/div[2]/i[2]")  # 删除第一个产品
    change_status_loc = (
        "xpath",
        "//*[contains(text(),'居室数')]/../../div[4]/table/tr[1]/td[3]/div/div[2]/div[1]/div/div[2]/div[2]/i[3]")  # 更改第一个产品状态
    add_product_loc = ("xpath", "//*[contains(text(),'新增产品')]")  # 点击新增产品按钮
    attr03_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[3]/td[2]/div/div/div/div/input")  # 第3个属性值
    choose_attr03_value_loc = ("xpath", "//*[contains(text(),'3面宽')]")  # 选择第3个属性值
    attr04_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[4]/td[2]/div/div/div/div/input")  # 第4个属性值
    choose_attr04_value_loc = ("xpath", "//*[contains(text(),'2T4')]")  # 选择第4个属性值
    attr05_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[5]/td[2]/div/div/div/div/input")  # 第5个属性值
    choose_attr05_value_loc = ("xpath", "//*[contains(text(),'Z1')]")  # 选择第5个属性值
    attr07_value_loc = ("xpath",
                        "//div[@class='el-table el-table--fit el-table--striped el-table--enable-row-hover el-table--enable-row-transition']/div[3]/table/tbody/tr[7]/td[2]/div/div/div/div/input")  # 第7个属性值
    choose_attr07_value_loc = ("xpath", "//*[contains(text(),'T2专属')]")  # 选择第7个属性值
    type_loc = (
        "xpath", "//*[@id='scrollContent']/div/div/section/div[1]/div/form/div[3]/div/div/div[1]/span/span/span")
    mianjiduan_value = ("xpath",
                        "//*[@id='pane-details']/section/div/form/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[1]/span/span/span")
    jushishu_value = ("xpath",
                      "//*[@id='pane-details']/section/div/form/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span/span/span")

    grid_del_confirm_loc = ('xpath', "//*[contains(text(),'确定')]")  # 删除确认按钮
