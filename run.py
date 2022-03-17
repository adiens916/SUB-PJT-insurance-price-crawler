import time

from drivers.helper import get_driver
from pages.lina.page import LinaDirectDentalPage
from user_settings import BROWSER
from utils.timer import Timer


def main_task():
    # 사용하는 브라우저에 맞춰 드라이버 실행
    driver = get_driver(BROWSER)  

    # 대상 연령대 (20세부터 65세까지)
    age_list = list(range(20, 66, 5))
    # 연령, 생년, 성별로 이루어진 리스트 반환
    input_pairs = Timer().get_birth_gender_pairs(age_list)

    # 라이나 다이렉트 치아보험 (기본형)
    LinaDirectDentalPage(driver).scrape(input_pairs)

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    main_task()
