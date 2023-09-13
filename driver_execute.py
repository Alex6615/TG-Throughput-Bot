import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs4

from driver_config import get_ChromeDriver
try :
    from secret_account import account, password, grafana
except :
    from secret_account_local import account, password, grafana
from time_generator import ts_generator



def get_Image(now, before_hours):
    pwd = os.getcwd()
    driver = get_ChromeDriver(autoquit=False)
    driver.get(f"http://{grafana}/login")
    # Account 位置
    account_input = driver.find_element(By.XPATH, "//*[@id='reactRoot']/div[1]/main/div/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input")
    account_input.click()
    account_input.send_keys(account)
    # Password 位置
    password_input = driver.find_element(By.XPATH, "//*[@id='current-password']")
    password_input.click()
    password_input.send_keys(password)
    # submit
    password_input = driver.find_element(By.XPATH, "//*[@id='reactRoot']/div[1]/main/div/div[3]/div/div[2]/div/div/form/button/span")
    password_input.click()
    time.sleep(1)
    driver.get(f"http://{grafana}/render/d-solo/93LKRJP4z/es-goedge-log-traffic?orgId=1&refresh=30s&from={before_hours}&to={now}&panelId=69&width=1000&height=500&tz=Asia%2FTaipei")
    driver.get_screenshot_as_file(f"{pwd}/png/throughput-{now}.png")
    driver.quit()
    return "throughput-" + now + ".png"

if __name__ == "__main__" :
    now, before = ts_generator()
    get_Image(now, before)