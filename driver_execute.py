import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs4

from driver_config import get_ChromeDriver
try :
    from secret_account import account, password, grafana
except :
    from secrets.secret_account_local import account, password, grafana
from time_generator import ts_generator


# serverId
# Wking 9
# Dobet 103
def get_Image(now, before_hours, serverId):
    pwd = os.getcwd()
    #driver = get_ChromeDriver(os="mac", headless=False)
    driver = get_ChromeDriver(headless=False, os="mac")
    driver.get(f"http://{grafana}/login")
    locator_loginpage = (By.XPATH, '//*[@id="pageContent"]/div/div/div[3]/div/div/div[1]/img')
    try :
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(locator_loginpage)) #最長等待10秒，每0.5秒檢查一次條件是否成立
    except :
        return
    # Account 位置
    account_input = driver.find_element(By.XPATH, "//*[@id='pageContent']/div/div/div[3]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div/div/input")
    account_input.click()
    account_input.send_keys(account)
    # Password 位置
    password_input = driver.find_element(By.XPATH, "//*[@id='current-password']")
    password_input.click()
    password_input.send_keys(password)
    # submit
    password_input = driver.find_element(By.XPATH, "//*[@id='pageContent']/div/div/div[3]/div/div/div[2]/div/div/form/button")
    password_input.click()
    time.sleep(2)
    locator_loginafter = (By.XPATH, '//*[@id=":r1:"]/div/div[3]/div/h1')
    try :
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(locator_loginafter)) #最長等待10秒，每0.5秒檢查一次條件是否成立
    except :
        return
    targetRenderUrl = f"http://{grafana}/d/93LKRJP4z/es-goedge-log-traffic?orgId=1&refresh=1m&var-serverId={serverId}&var-host=All&var-XFF=All&var-nid=&from={before_hours}&to={now}&viewPanel=88&width=1000&height=500&tz=Asia%2FTaipei"
    #print(targetRenderUrl)
    #driver.get(f"http://{grafana}/render/d-solo/93LKRJP4z/es-goedge-log-traffic?orgId=1&refresh=30s&var-serverId={serverId}&from={before_hours}&to={now}&panelId=69&width=1000&height=500&tz=Asia%2FTaipei")
    driver.get(targetRenderUrl)
    locator_screenshot = (By.XPATH, "//*[@id='pageContent']/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div")
    try :
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(locator_screenshot)) #最長等待10秒，每0.5秒檢查一次條件是否成立
        webdriver.ActionChains(driver).move_by_offset(0,0).perform()
        driver.set_window_size(1920,1080)
        driver.get_screenshot_as_file(f"{pwd}/png/throughput-{now}-{serverId}.png")
    except :
        print("screenshot load timeout !")
        #driver.get_screenshot_as_file(f"{pwd}/png/throughput-{now}-{serverId}.png")
    finally :
        driver.quit()
        return "throughput-" + now + "-" + str(serverId) + ".png"

if __name__ == "__main__" :
    now, before = ts_generator()
    get_Image(now, before, serverId=103)