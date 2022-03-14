from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # add this import for drop down list
from time import sleep
import datetime
import sys

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print('Launch AOS website')
    # make browser Full screen
    driver.maximize_window()
    # Give driver up to 30 second to respond
    driver.implicitly_wait(30)
    # Navigate to web page URL 'https://advantageonlineshopping.com/#/'
    driver.get(locators.AOS_url)
    # Check URL and home page title are as expected.
    if driver.current_url == locators.AOS_url and driver.title == locators.AOS_title:
        print('AOS website Launched successfully')
        print(f'AOS homepage URL: {driver.current_url}\nHome page Title: {driver.title}')
        sleep(1)
    else:
        print(f'AOS Website did not launch, check your code!')
        print(f'Current URL: {driver.current_url}\nHome page Title: {driver.title}')
        tearDown()


def new_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    assert driver.find_element(By.XPATH, '//label[contains(.,"OR")]').is_displayed()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.25)
    assert driver.current_url == locators.AOS_registration_url
    assert driver.title == locators.AOS_title
    print('You are on registration page')
    sleep(0.25)

    # Account details
    driver.find_element(By.XPATH, '//input[contains(@name,"usernameRegisterPage")]').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"emailRegisterPage")]').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"passwordRegisterPage")]').send_keys(locators.new_password1)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"confirm_passwordRegisterPage")]').send_keys(
        locators.new_password1)
    sleep(0.25)

    # Personal details
    driver.find_element(By.XPATH, '//input[contains(@name,"first_nameRegisterPage")]').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"last_nameRegisterPage")]').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"phone_numberRegisterPage")]').send_keys(locators.phone)
    sleep(0.25)

    # Address
    Select(driver.find_element(By.XPATH, '//*[contains(@name, "countryListboxRegisterPage")]')).select_by_visible_text(
        'Canada')
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "cityRegisterPage")]').send_keys(locators.city)
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "addressRegisterPage")]').send_keys(locators.address)
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "state_/_province_/_regionRegisterPage")]').send_keys(
        locators.province)
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(., "Postal Code")]').send_keys(locators.postal_code)
    sleep(1)
    driver.find_element(By.XPATH, '//input[@name="i_agree"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(.,"REGISTER")]').click()
    sleep(1)

    # Validate New Account created (new username is displayed in the top menu)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    print('New user account is created')




def add_shopping_cart_item():
    driver.find_element(By.ID, 'tabletsTxt').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'HP ElitePad 1000 G2 Tablet').click()
    sleep(2)
    driver.find_element(By.XPATH, '//button[contains(.,"ADD TO CART")]').click()
    sleep(0.25)
    print('New item is added to shopping cart')
    sleep(2)


def checkout_shopping_cart():
    print('Checkout shopping cart')
    driver.find_element(By.ID, 'menuCart').click()
    sleep(1)
    driver.find_element(By.ID, 'checkOutButton').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'next_btn').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(@name, "safepay_username")]').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(@name, "safepay_password")]').send_keys(locators.new_password1)
    sleep(0.25)
    driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
    sleep(0.25)
    driver.find_element(By.TAG_NAME, 'h2').is_displayed()
    print('Thank you for buying with Advantage Online Shopping')
    sleep(0.25)
    tr = driver.find_element(By.ID, 'trackingNumberLabel')
    print(f'Your tracking number is: {tr.text}')
    sleep(0.25)
    on = driver.find_element(By.ID, 'orderNumberLabel')
    print(f'Your order number is: {on.text}')
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    print(f'Name of customer: {locators.full_name}')
    driver.find_element(By.XPATH, f'//*[contains(., "{locators.address}")]').is_displayed()
    sleep(1)
    driver.find_element(By.XPATH, f'//*[contains(., "{locators.city}")]').is_displayed()
    sleep(1)
    driver.find_element(By.XPATH, f'//*[contains(., "{locators.province}")]').is_displayed()
    sleep(1)
    driver.find_element(By.XPATH, f'//*[contains(., "{locators.phone}")]').is_displayed()
    sleep(1)
    print(f'Customer address is: {locators.address}\n{locators.city}\n{locators.province}')
    print(f'Customer phone number is: {locators.phone}')
    total = driver.find_element(By. XPATH, '//label[contains(., "TOTAL")]/a[@class="floater ng-binding"]')
    print(f'Your total amount is: {total.text}')
    sleep(0.25)
    date_ordered = driver.find_element(By. XPATH, '//label[contains(., "Date ordered")]/a[@class="floater ng-binding"]')
    print(f'Date ordered: {date_ordered.text}')
    sleep(0.25)
    # view order
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    #driver.find_element(By.LINK_TEXT, 'My orders').click()
    sleep(5)
    view_order = driver.find_element(By. XPATH, f'//*[@class="left ng-binding"]')
    # driver.find_element(By.XPATH, f'//*[contains(.,"{on.text}")]').is_displayed()
    print(f'Your oder number is displayed')
    sleep(2)


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(3)
    print('You logged out\nThank you for shopping')
    sleep(3)




def tearDown():
    if driver is not None:
        print('------------------------------------------')
        print(f'The test completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()



#
# setUp()
# new_account()
# add_shopping_cart_item()
# checkout_shopping_cart()
# log_out()
tearDown()
