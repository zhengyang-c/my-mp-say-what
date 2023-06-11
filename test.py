import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

HANSARD_HOME = "https://sprs.parl.gov.sg/search/#/home"

def wait_for(condition_function):
	start_time = time.time()
	while time.time() < start_time + 10:
		if condition_function():
			return True
		else:
			time.sleep(0.1)
	raise Exception('Timeout waiting for {}'.format(condition_function.__name__))


class wait_for_page_load(object):
	def __init__(self, browser):
		self.browser = browser
	def __enter__(self):
		self.old_page = self.browser.find_element(By.TAG_NAME, 'html')
	def page_has_loaded(self):
		new_page = self.browser.find_element(By.TAG_NAME, 'html')
		return new_page.id != self.old_page.id
	def __exit__(self, *_):
		wait_for(self.page_has_loaded)

driver = webdriver.Firefox()

driver.get(HANSARD_HOME)
driver.implicitly_wait(10)
kw = driver.find_element(By.XPATH, "//input[@type='text']")
kw.send_keys("climate change")
time.sleep(5)

time_period = driver.find_element(By.XPATH, "//select[@size='11']/option[last()]" ) #so hacky lol
time_period.click()

search_match = driver.find_element(By.XPATH, "//option[@value='2: exact phrase search']")
search_match.click()


with wait_for_page_load(driver):
	driver.find_element(By.XPATH, "//button[@label='Search']").click()

time.sleep(10)


driver.close()