from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def get_ChromeDriver(
    autoquit:bool = True, 
    headless:bool = True, 
    user_agent = None, 
    os = "linux",
    ):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if headless == True :
        #pass
        options.add_argument('--headless')
    if autoquit == False :
        options.add_experimental_option("detach", True)
    if user_agent != None :
        options.add_argument(f"--user-agent={user_agent}")
    else :
        options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--mute-audio')
    if os == "linux" :
        driver = webdriver.Chrome(executable_path=r"/usr/lib/chromium/chromedriver", chrome_options=options)
    elif os == "mac":
        #driver = webdriver.Chrome(executable_path=r"/opt/homebrew/bin/chromedriver", chrome_options=options, desired_capabilities=dc)
        driver = webdriver.Chrome(executable_path=r"/opt/homebrew/bin/chromedriver", chrome_options=options)
    return driver
