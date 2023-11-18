from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.adamchoi.co.uk/bttsresult/detailed")

# Click on the "All Matches" button
all_matches_button = driver.find_element(By.XPATH,"//label[@class='btn btn-sm btn-primary ng-pristine ng-untouched ng-valid ng-not-empty']")
all_matches_button.click()
container = driver.find_element(By.XPATH, '//div[@class="row ng-scope"][2]')
time.sleep(5)
driver.quit()