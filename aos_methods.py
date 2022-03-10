from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import aos_locators as locators
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import sys

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


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
    sleep(0.5)
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
    driver.find_element(By.XPATH, '//input[@name="i_agree"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"REGISTER")]').click()
    sleep(0.25)

    # Validate New Account created (new username is displayed in the top menu)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    print('New user account is created')
    #logger('created')


def log_in():
    print('-----------------')
    print('----- login -----')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.XPATH, '//input[contains(@name,"username")]').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name,"password")]').send_keys(locators.new_password1)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.25)
    print(f'You are signed in with username: {locators.new_username}')
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    sleep(0.25)
    print(f'login is validated with username: {locators.new_username}')


def check_homepage_texts():
    if driver.current_url == locators.AOS_url and driver.title == locators.AOS_title:
        assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
        print('SPEAKER text is displayed')
        sleep(0.25)
        assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        print('TABLETS text is displayed')
        sleep(0.25)
        assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
        print('LAPTOPS text is displayed')
        sleep(0.25)
        assert driver.find_element(By.ID, 'miceTxt').is_displayed()
        print('MICE text is displayed')
        sleep(0.25)
        assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
        print('HEADPHONES text is displayed')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
        sleep(0.25)
        assert driver.find_element(By.CLASS_NAME, 'container ').is_displayed()
        print('OUR PRODUCTS Link is clickable')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        sleep(0.25)
        assert driver.find_element(By.ID, 'special_offer_items').is_displayed()
        print('SPECIAL OFFER Link is clickable')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        sleep(0.25)
        assert driver.find_element(By.ID, 'popular_items').is_displayed()
        print('POPULAR ITEMS Link is clickable')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(0.25)
        assert driver.find_element(By.ID, 'supportCover').is_displayed()
        print('CONTACT US Link is clickable')
        sleep(0.25)



def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    print('You logged out\nThank you for shopping')


def delete_user_account():
    driver.find_element(By.ID, 'menuUser').click()
    assert driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]').is_displayed()
    driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').click()
    assert driver.find_element(By.XPATH, '//*[contains(.,"My account")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
    driver.find_element(By.ID, 'hrefUserIcon').click()
    java_script = driver.find_element(By.XPATH, '//label[contains(.,"My account")]')
    driver.execute_script("arguments[0].click();", java_script)
    sleep(0.5)
    assert driver.current_url == locators.AOS_my_account_url
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(5)
    #assert driver.find_element(By.CLASS_NAME, 'deleteAccountPopupContent').is_displayed()
    #sleep(2)
    driver.find_element(By.XPATH, '//div[contains(., "yes")]').click()
    sleep(5)

    #assert driver.current_url == locators.AOS_url
    #sleep(0.25)
    print(f'User {locators.new_username} is deleted')
    #logger('deleted')


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
# #check_homepage_texts()
# new_account()
# log_out()
# log_in()
# #log_out()
# #delete_user_account()
# tearDown()
