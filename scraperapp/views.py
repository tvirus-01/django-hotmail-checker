from django.shortcuts import render
from django.http import HttpResponse as hre

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from time import sleep

# Create your views here.

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
        return "email dose not exists"

    return "email exists"

def scraper(request):

    hotMail = request.GET.get("email", 1)

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return hre(checkHotMail(hotMail, driver))