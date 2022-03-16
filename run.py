import time

from drivers.helper import get_driver
from pages.lina.page import LinaDental
from user_settings import BROWSER


def main_task():
    # 사용하는 브라우저에 맞춰 드라이버 실행
    driver = get_driver(BROWSER)  

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    main_task()
