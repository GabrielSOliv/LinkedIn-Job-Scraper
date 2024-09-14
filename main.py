from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")


search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('site:linkedin.com/jobs/view ("Python" OR "Desenvolvedor Python" OR "Desenvolvedor Jr Python") ' \
       '(intext:"remoto" OR intext:"Remote") ' \
       '(intext:"Brasil" OR intext:"Brazil") ' \
       '(intext:"júnior" OR intext:"trainee" OR intext:"estágio") ' \
       '(intext:"VBA" OR intext:"Python" OR intext:"SQL" OR intext:"Inglês" OR intext:"Excel" OR intext:"Power BI")')
search_box.send_keys(Keys.RETURN)

time.sleep(35)

tool_btn = driver.find_element(By.XPATH, '//*[@id="hdtb-tls"]')
tool_btn.send_keys(Keys.RETURN)

time.sleep(5)


date_picker = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[1]/span[2]/g-popup/div[1]/div')
date_picker.click()

time.sleep(5)

last_month = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[1]/span[2]/g-popup/div[2]/g-menu/g-menu-item[5]/div/a')
last_month.click()

time.sleep(5)


links = []
results = driver.find_elements(By.XPATH, '//*[@id="center_col"]')[:10]
for result in results:
    links.append(result.get_attribute('href'))

df = pd.DataFrame(links, columns=['Links'])
df.to_excel('resultados_google.xlsx', index=False)


driver.quit()