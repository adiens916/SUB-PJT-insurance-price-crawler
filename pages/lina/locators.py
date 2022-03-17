from selenium.webdriver.common.by import By


BIRTHDAY_INPUT = (By.ID, 'birthday')
MALE_BUTTON = (By.ID, 'main_btn_male')
FEMALE_BUTTON = (By.ID, 'main_btn_female')
CHECK_BUTTON = (By.ID, 'btn_direct_dental_cal')

STANDARD_PLAN_COST = (By.CSS_SELECTOR, 'td.inNum:nth-of-type(1) > strong')
PREMIUM_PLAN_COST = (By.CSS_SELECTOR, 'td.inNum:nth-of-type(2) > strong')
# PAGE_IMG = (By.XPATH, '//img[@class="background"]')
