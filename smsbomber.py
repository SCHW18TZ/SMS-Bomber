from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import asyncio
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.maximize_window()


username = ''
password = 'schwitz'

driver.get("https://www.tnesevai.tn.gov.in/citizen/LoginWithMobile.aspx")


driver.find_element(
    "name", "ctl00$ContentPlaceHolderTop$txtMobileNumber").send_keys(username)
driver.find_element(
    "name", "ctl00$ContentPlaceHolderTop$btnGenerateOTP").click()

# UBER

driver.get("https://auth.uber.com/v2/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fm.uber.com%2F&state=QmkIBgpRkBk7CIw7elYarNmFSTu9uapHKUnWa1E9-R0%3D")


driver.find_element(
    "id", "PHONE_NUMBER_or_EMAIL_ADDRESS").send_keys(username)
driver.find_element(
    "xpath", "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button").click()

# SWIGGY

driver.get("https://swiggy.com/")

driver.find_element(
    "xpath", "/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]").click()
driver.find_element(
    'name', 'mobile').send_keys(username)

driver.find_element(
    "xpath", "/html/body/div[2]/div/div/div[2]/div/div/div/form/div[2]/a").click()

# JIOMART

driver.get("https://www.jiomart.com/customer/account/login")

driver.find_element(
    'xpath', "/html/body/app-root/app-layout/div/main/div/app-login/div[1]/div/div[1]/div[2]/div/div[1]/form/div[1]/input").send_keys(username)

driver.find_element(
    'xpath', "/html/body/app-root/app-layout/div/main/div/app-login/div[1]/div/div[1]/div[2]/div/div[1]/form/div[2]/button[1]").click()


AMAZON

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")


driver.find_element(
    'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]"
).send_keys(username)


driver.find_element(
    'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input").click()
driver.find_element(
    'xpath', "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[3]/form/span/span/input").click()


driver.get("https://pizzaonline.dominos.co.in")

driver.find_element(
    "xpath", "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[2]/div[1]/div[2]").click()
driver.find_element(
    'name', 'loginNumber').send_keys(username)

driver.find_element(
    "xpath", "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input").click()


driver.get("https://accounts.snapchat.com/accounts/password_reset/phone")


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "reset-password-by-phone"))
    )
    driver.find_element(
        "xpath", "/html/body/div/div/div/div[3]/article/div/div[3]/form/div[1]/div/div[2]/div/input").send_keys(username)

    driver.find_element(
        "xpath", "/html/body/div/div/div/div[3]/article/div/div[3]/form/div[3]/button").click()

finally:
    print("s")
