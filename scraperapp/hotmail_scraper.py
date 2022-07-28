from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

from pyvirtualdisplay import Display

from time import sleep

def checkHotmail(emailAddress):
    servicePath = "./geckodriver"

    display = Display(visible=0, size=(800, 600))
    display.start()

    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("-profile")
    options.add_argument("selenium-data/rust_mozprofile2mydzI")

    driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=options
        )

    driver.get("https://signup.live.com/")

    sleep(2)

    input_email = driver.find_element(By.ID, 'MemberName')
    input_email.send_keys(emailAddress)

    sleep(1)

    driver.find_element(By.ID, 'iSignupAction').click()

    sleep(2)

    try:
        driver.find_element(By.ID, 'MemberNameError')
        print("email exists")
    except NoSuchElementException:
        print("email not exists")

    driver.quit()

# checkHotmail("shakisa54@gmail.com")