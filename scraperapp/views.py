from django.shortcuts import render
from django.http import HttpResponse as hre

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import re

from time import sleep

# Create your views here.

def checkValid(email):
 
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def checkHotMail(emailAddress, driver):

    driver.get("https://signup.live.com/")

    sleep(2)

    input_email = driver.find_element(By.ID, 'MemberName')
    input_email.send_keys(emailAddress)

    sleep(1)

    driver.find_element(By.ID, 'iSignupAction').click()

    sleep(2)

    try:
        driver.find_element(By.ID, 'MemberNameError')
    except NoSuchElementException:
        return "This email dose not exists"

    return "This email exists"

def scraper(request):

    hotMail = request.GET.get("email", 1)

    if hotMail == 1:
        return hre("Please enter an email")
    elif checkValid(hotMail) == False:
        return hre("This email is not valid")

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    result = checkHotMail(hotMail, driver)

    driver.quit()

    return hre(result)