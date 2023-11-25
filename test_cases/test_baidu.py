import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestBaiduSearch(unittest.TestCase):

    def setUp(self):
        # 前置条件: 用户打开百度搜索页面
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_search_valid_keyword(self):
        # 测试步骤:
        # 1. 在搜索输入框中输入一个有效关键字（例如："测试"）
        search_input = self.driver.find_element(By.ID, "kw")
        search_input.send_keys("测试")

        # 2. 点击搜索按钮
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()

        sleep(12)
        # 预期结果: 显示搜索结果页面。
        self.assertIn("百度为您找到相关结果约", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
