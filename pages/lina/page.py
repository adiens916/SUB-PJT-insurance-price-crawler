import csv
import time

from ..base.elements import DOWNLOAD_FOLDER
from ..base.exceptions import NotEligibleAgeError
from ..base.page import BasePage
from . import elements
from . import locators


class LinaDirectDentalPage(BasePage):
    def scrape(self, input_pairs):
        self.go_to_url(elements.URL)

        download_folder = self.make_directory(DOWNLOAD_FOLDER)

        file = open(f'{download_folder}/{__class__.__name__}.csv', 'w', newline='')
        csv_writer = csv.writer(file)
        
        for age, birthdate, gender in input_pairs:
            self.__input_info(birthdate, gender)
            time.sleep(2)

            try:
                self.__check_eligibility(age)
                cost = self.__gather_data()
                csv_writer.writerow([age, gender, cost])
            except NotEligibleAgeError as e:
                print(e)
            except Exception as e:
                print(e)
        
        file.close()

    def __input_info(self, birthdate: str, gender: int):
        """
        생년월일과 성별 정보 입력
        - 각 보험마다 따로 구현 필요
        """
        birthday_input = self.find(locators.BIRTHDAY_INPUT)
        birthday_input.clear()
        birthday_input.send_keys(birthdate)

        if gender == 1:
            self.wait_to_click(locators.MALE_BUTTON)
            select_button = self.find(locators.MALE_BUTTON)
        elif gender == 2:
            self.wait_to_click(locators.FEMALE_BUTTON)
            select_button = self.find(locators.FEMALE_BUTTON)
        select_button.click()
        
        check_button = self.find(locators.CHECK_BUTTON)
        check_button.click()
    
    def __check_eligibility(self, age):
        """
        해당 연령으로 가입이 가능한지 확인.
        - 틀릴 경우 예외를 돌려준다.
        - 각 보험마다 따로 구현 필요.
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            raise NotEligibleAgeError('', age)
        except:
            pass
        
    def __gather_data(self):
        """
        데이터를 찾아서 반환.
        - 각 보험마다 따로 구현 필요.
        """
        cost = self.find(locators.STANDARD_PLAN_COST).text
        # cost = self.find(locators.PREMIUM_PLAN_COST).text
        data = int(cost.replace(',', ''))

        return data
    
