import os
from pathlib import Path
from urllib.request import urlretrieve
from selenium.webdriver.support import expected_conditions as EC

from ..base.page import BasePage
from . import elements
from . import locators


class BookPage(BasePage):
    def go(self, book_id):
        book_link = f'{elements.BOOK_LINK_PREFIX}/{book_id}/index.html'
        self.driver.get(book_link)
        self.wait.until(EC.presence_of_element_located(locators.PAGE_IMG))

    def get_img_url_root(self):
        # 이미지 주소 틀만 가져오기
        # 예) ... /assets/page-images/page-e68dc697-5daf221c-0077.jpg
        # =>  ... /assets/page-images/page-e68dc697-5daf221c
        first_image = self.driver.find_elements(*locators.PAGE_IMG)[0]
        image_url = first_image.get_attribute('src')
        image_url_root = image_url.rsplit(sep='-', maxsplit=1)[0]
        return image_url_root
    
    def get_total_page_number(self):
        # 총 페이지 수 구하기
        page_numbers = self.find(locators.PAGE_NUMBERS)
        total_page_number = page_numbers.text.split()[-1]
        total_page_number = int(total_page_number)
        return total_page_number

    def make_download_directory(self, book_name):
        # 새로운 폴더의 경로
        sub_dir = elements.BOOK_DOWNLOAD_FOLDER + f'/{book_name}'
        dir_path = self.make_directory(sub_dir)
        return dir_path

    def download(self, book_id):
        # 교재 링크로 이동
        self.go(book_id)

        # 이미지 주소와 개수를 구함
        image_url_root = self.get_img_url_root()
        total_page_number = self.get_total_page_number()

        # 이미지 저장할 폴더 만들기
        dir_name = self.make_download_directory(self.driver.title)

        # 페이지 수만큼 돌며 스크린샷으로 저장
        for i in range(1, total_page_number + 1):
            url = f'{image_url_root}-{i:04}.jpg'
            self.driver.get(url)
            self.driver.save_screenshot(f'{dir_name}/{i:04}.jpg')
