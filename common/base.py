"""
base.py  对selenium做二次封装
1.打开浏览器
2.输入网址
3.元素定位
4.元素操作
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def open_browser(browser="chrome"):
    """
    打开浏览器
    :param browser: 浏览器名称
    :return:
    """
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # 无头模式
        # options.add_argument('--disable-gpu')  # 禁用GPU加速
        # options.add_argument('blink-settings=imagesEnabled=false')  # 禁止加载图片
        # options.add_argument('--no-sandbox')  # 以最高权限运行
        # # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--window-size=1920,1080')  # 设置窗口大小
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        print("请输入正确的浏览器名称,例如'Chrome','Firefox','ie'")
        driver = None
    return driver


class Base:
    def __init__(self, driver):
        """
        初始化浏览器
        :param driver:
        """
        self.driver = driver

    def open_url(self, url):
        """
        打开网址
        :param url: 网址
        :return:
        """
        self.driver.get(url)
        # 浏览器最大化
        self.driver.maximize_window()

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def refresh(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def find_element(self, locator: tuple, timeout=10):
        """
        定位单个元素
        :param:locator:定位器,元组格式 例如("id","id属性值")
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素
        :param locator: 定位器
        :param timeout: 最大等待时间
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f"元素{locator}没找到")
            return False

    def click(self, locator):
        """
        点击元素
        :return:
        """
        element = self.find_element(locator)
        try:
            element.click()
        except Exception as msg:
            print(msg)

    def send_keys(self, locator, text):
        """
        输入
        :param locator: 定位器,元组
        :param text: 需要输入的文本
        :return:
        """
        element = self.find_element(locator)
        try:
            element.clear()
            element.send_keys(text)
        except Exception as msg:
            print(msg)

    def move_mouse(self, locator):
        """
        移动鼠标到目标元素
        :param locator: 定位器，元组
        :return:
        """
        element = self.find_element(locator)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as msg:
            print(msg)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否在元素的文本中,如果在,返回True,如果不在返回False
        :param locator: 定位器,元组
        :param text: 文本
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            # result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        """
        判断value值是否是元素value属性对应的值,如果是,返回True,否则返回False
        :param locator: 定位器
        :param value: 文本
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_selected(self, locator):
        """
        判断元素是否被选中:如果选中,返回True,否则返回False
        """
        element = self.find_element(locator)
        try:
            result = element.is_selected()
            return result
        except:
            return False
