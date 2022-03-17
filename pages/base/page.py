import os
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:       
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find(self, locator: Tuple[str, str]) -> WebElement:
        """
        원하는 Web Element를 찾습니다. 
        
        없으면 오류를 내는 대신에 None을 반환합니다.
        """
        # https://stackoverflow.com/questions/9567069/checking-if-element-exists-with-python-selenium
        try:
            element = self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException as err:
            print(f'오류: 다음 요소를 찾을 수 없음 - {locator[1]}')
            return None
        return element
    
    def go_to_url(self, url: str):
        self.driver.get(url)

    def switch_window(self, target_title: str):
        # https://www.selenium.dev/documentation/webdriver/browser_manipulation/
        # window_handle은 브라우저 타이틀 X => 아래와 같은 고유 ID를 가짐
        # CDwindow-5B3C6A7CFB7405E93DF9899E9AF87311

        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)

                # Wait for the new tab to finish loading content
                # self.wait.until(EC.title_is("SeleniumHQ Browser Automation"))
                
                # 추가: 원하는 페이지 타이틀이 포함되어 있나 확인
                if target_title in self.driver.title:
                    return

        print('No such title:', target_title)

    def wait_to_see(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_to_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def make_directory(self, dir_path):
        # 폴더가 이미 있으면 오류, 없으면 새로 만들기
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
        except OSError as e:
            print(e)

        return dir_path
