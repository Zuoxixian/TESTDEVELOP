import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    _base_url = ""

    # 通过复用方法通过登录
    def __init__(self, base_driver = None):
        if base_driver is None:
            # 通过remote复用浏览器
            # chrome --remote-debugging-port=9222
            opt = webdriver.ChromeOptions()
            # 加入调试地址
            opt.debugger_address = "127.0.0.1:9222"
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=opt)
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(3)
        else:
            self.driver: WebDriver = base_driver

    # 通过cookie方式通过登录
    def test_cookie_login(self):
        driver = webdriver.Chrome
        driver.implicitly_wait(10)
        driver.get(self._base_url)
        cookies = self.driver.get_cookies()
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookies,f)
        with open("data.yaml",encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(self._base_url)
        driver.quit()

    def find(self,by,locator = None):
        #如果只传一个元组参数
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by,value=locator)