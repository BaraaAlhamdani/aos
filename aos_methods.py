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
    logger('created')



def check_no_order():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(., " - No orders - ")]').is_displayed()
    print('No orders Found')
    sleep(0.25)



def delete_user_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'hrefUserIcon').is_displayed()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'deleteBtnContainer').click()
    sleep(2)
    print(f'User {locators.new_username} is deleted')
    sleep(0.5)
    logger('deleted')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"username")]').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.ID, 'signInResultMessage').is_displayed()
    print('User delete validated')
    sleep(0.25)


def tearDown():
    if driver is not None:
        print('------------------------------------------')
        print(f'The test completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('../aos/message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setUp()
# new_account()
# check_no_order()
# delete_user_account()
# tearDown()
# add_shopping_cart_item()
# checkout_shopping_cart()
#log_out()
# check_homepage_texts()
# contact_us()
# social_media_link()
# new_account()
# log_out()
# log_in()
# delete_user_account()
#tearDown()
