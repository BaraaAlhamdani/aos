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
        driver.find_element(By.CLASS_NAME, 'logo').is_displayed()
        print('logo is displayed')
        sleep(0.25)


def contact_us():
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(0.25)
    assert driver.find_element(By.ID, 'supportCover').is_displayed()
    sleep(0.25)
    Select(driver.find_element(By.XPATH, '//*[contains(@name,"categoryListboxContactUs")]')).select_by_visible_text('Laptops')
    sleep(0.25)
    Select(driver.find_element(By.XPATH, '//*[contains(@name, "productListboxContactUs")]')).select_by_visible_text('HP Chromebook 14 G1(ES)')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(@name, "emailContactUs")]').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(@name, "subjectTextareaContactUs")]').send_keys(locators.description)
    sleep(0.25)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(., "Thank you for contacting Advantage support.")]').is_displayed()
    sleep(0.25)
    print('Thank you for contacting Advantage support. message is displayed')
    sleep(0.25)
    driver.find_element(By.XPATH, '//div[contains(., " CONTINUE SHOPPING ")]').click()
    sleep(0.25)
    print('CONTINUE SHOPPING button is clickable')
    assert driver.current_url == locators.AOS_url
    print('You are on homepage')


def social_media_link():
    #driver.find_element(By.XPATH, '//*[conatins(@h3, "FOLLOW US")]').is_displayed()
    driver.find_element(By.TAG_NAME, 'h3')
    #driver.find_element(By.LINK_TEXT, 'FOLLOW US').is_displayed()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_facebook")]').is_displayed()
    driver.find_element(By.XPATH, '//*[contains(@name, "follow_facebook")]').click()
    sleep(2)
    print('facebook link is clicked')
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_twitter")]').is_displayed()
    driver.find_element(By.XPATH, '//*[contains(@name, "follow_twitter")]').click()
    sleep(2)
    print('twitter link is clicked')
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_linkedin")]').is_displayed()
    driver.find_element(By.XPATH, '//*[contains(@name, "follow_linkedin")]').click()
    sleep(2)
    print('linkedin link is clicked')
    sleep(2)


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    print('You logged out\nThank you for shopping')
    sleep(3)

    


def tearDown():
    if driver is not None:
        print('------------------------------------------')
        print(f'The test completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


#setUp()
#check_homepage_texts()
#contact_us()
#social_media_link()
#new_account()
#log_out()
#log_in()
#delete_user_account()
#tearDown()
