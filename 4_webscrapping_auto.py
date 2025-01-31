from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# Set up the Chrome driver
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=service, options=options)

# Start on the second screen
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(2)

driver.get('https://www.mercadolibre.com.ar/')

# Search for 'celular XIAOMI'
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('celular XIAOMI')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()

# Check for the filter to be clickable and get the URL
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[3]/aside/section[2]/div[10]/ul/li[5]/a')))
url = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/aside/section[2]/div[10]/ul/li[5]/a').get_attribute('href')

# Navigate to the found URl
driver.get(url)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[3]/section/ol')))
lista=driver.find_element(by=By.CSS_SELECTOR, value='ol.ui-search-layout.ui-search-layout--stack.shops__layout').find_elements(by=By.TAG_NAME, value='li')


for item in lista:
    text=item.get_attribute('innerHTML')
    soup=BeautifulSoup(text, 'html.parser')
    print(soup.findAll('h3')[0].string)
    print(soup.select('span.andes-money-amount__fraction')[0].string)  # Price without discount
    for url in soup.select('a.poly-component__title'):
        print(url['href'])

    print('\n')

# Sleep
time.sleep(500)  

# Close the driver
driver.quit()
