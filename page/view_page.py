from common.base import Base


class ViewPage(Base):
    """封装表现层: 制作定位器"""
    View_loc = ("xpath", "//*[contains(text(),'产品查看')]")  # 地区类目维护标签
    key_loc = ('xpath', "//input[@placeholder='请输入内容']")  # 关键字输入框
    search_loc = ("xpath", "//*[contains(text(),'查询')]")  # 搜索按钮
    first_product = ('xpath', "//div[@class='list']/div[1]/div[2]/div[1]/span")  # 获取产品名称
    region_pull_loc = ('xpath',
                       "//*[@id='scrollContent']/section/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/span/span/i")  # 地区下拉框
