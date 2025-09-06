from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page_no = 1

while True:
    if page_no==1:
        driver.get('https://www.amazon.in/s?k=laptop&crid=14CB3RTX7VWW5&sprefix=laptop%2Caps%2C935&ref=nb_sb_noss_1')
    
    elems = driver.find_elements(By.XPATH, '//div[@role="listitem"]//div[@class="puisg-col-inner"]')

    # Create the directory if it doesn't exist
    directory = f'data/page_{page_no}'
    os.makedirs(directory, exist_ok=True)

    for i, elem in enumerate(elems):
        with open(f'data/page_{page_no}/laptop_{i+1}.html', 'w', encoding='utf-8') as file:
            file.write(elem.get_attribute('innerHTML'))

#     elems = driver.find_elements(By.XPATH, '//')
    try:
        # wait until element become clickable or 10sec else throw Timeout Exception
        nxt_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//li/span/a[contains(@class, "s-pagination-next")]'))
        )
        nxt_btn.click()
        time.sleep(random.randint(5,15)) # random delay (to make it human)
    except TimeoutException:
        break
    
    page_no += 1

driver.quit()