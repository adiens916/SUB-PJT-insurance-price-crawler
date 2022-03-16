from base.elements import DOWNLOAD_FOLDER
from base.page import BasePage
from . import elements
from . import locators


class LinaDirectDentalPage(BasePage):
    def scrape(self, input_pairs):
        self.go_to_url(elements.URL)

        cur_download_folder = DOWNLOAD_FOLDER + f'/{__class__.__name__}'
        self.make_directory(cur_download_folder)

        for age, birthdate, gender in input_pairs:
            self.input_info(birthdate, gender)
            try:
                self.check()
            except:
                print(f'{age}세는 가입 연령에서 벗어남.')
