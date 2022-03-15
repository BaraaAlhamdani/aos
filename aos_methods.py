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
    sleep(1)
    assert driver.current_url == locators.AOS_registration_url
    assert driver.title == locators.AOS_title
    print('You are on registration page')
    sleep(1)

    # Account details
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password1)
    sleep(1)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password1)
    sleep(1)

    # Personal details
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(1)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(1)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(1)

    # Address
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
    sleep(1)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(1)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(1)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(
        locators.province)
    sleep(1)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(1)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(1)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)

    # Validate New Account created (new username is displayed in the top menu)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    print('New user account is created')
    #logger('created')


def log_in():
    print('-----------------')
    print('----- login -----')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password1)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    print(f'You are signed in with username: {locators.new_username}')
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    sleep(1)
    print(f'login is validated with username: {locators.new_username}')


def check_no_order():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//label[contains(., " - No orders - ")]').is_displayed():
        print('No orders Found')
        sleep(2)
        driver.find_element(By.XPATH, '//*[contains(., "CONTINUE SHOPPING")]').click()
        sleep(1)
    else:
        driver.find_element(By.XPATH, '//*[@translate = "REMOVE"]').click()
        sleep(1)
        driver.find_element(By.ID, 'confBtn_1').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@translate = "CONTINUE_SHOPPING"]').click()
        sleep(1)


def check_homepage_texts():
    assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    print('SPEAKER text is displayed')
    sleep(1)
    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    print('TABLETS text is displayed')
    sleep(1)
    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    print('LAPTOPS text is displayed')
    sleep(1)
    assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    print('MICE text is displayed')
    sleep(1)
    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    print('HEADPHONES text is displayed')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    sleep(1)
    assert driver.find_element(By.CLASS_NAME, 'container ').is_displayed()
    print('OUR PRODUCTS Link is clickable')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(1)
    assert driver.find_element(By.ID, 'special_offer_items').is_displayed()
    print('SPECIAL OFFER Link is clickable')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(1)
    assert driver.find_element(By.ID, 'popular_items').is_displayed()
    print('POPULAR ITEMS Link is clickable')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(1)
    assert driver.find_element(By.ID, 'supportCover').is_displayed()
    print('CONTACT US Link is clickable')
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'logo').is_displayed()
    print('logo is displayed')
    sleep(1)


def contact_us():
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(1)
    assert driver.find_element(By.ID, 'supportCover').is_displayed()
    sleep(1)
    Select(driver.find_element(By.XPATH, '//*[contains(@name,"categoryListboxContactUs")]')).select_by_visible_text(
        'Laptops')
    sleep(1)
    Select(driver.find_element(By.XPATH, '//*[contains(@name, "productListboxContactUs")]')).select_by_visible_text(
        'HP Chromebook 14 G1(ES)')
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "emailContactUs")]').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "subjectTextareaContactUs")]').send_keys(locators.description)
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(., "Thank you for contacting Advantage support.")]').is_displayed()
    sleep(1)
    print('Thank you for contacting Advantage support. message is displayed')
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(., " CONTINUE SHOPPING ")]').click()
    sleep(1)
    print('CONTINUE SHOPPING button is clickable')
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'logo').click()
    sleep(2)
    print('You are on homepage')


def social_media_link():
    driver.find_element(By.TAG_NAME, 'h3').is_displayed()
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_facebook")]').is_displayed()
    sleep(2)
    print('facebook link is clicked')
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_twitter")]').is_displayed()
    sleep(2)
    print('twitter link is clicked')
    assert driver.find_element(By.XPATH, '//*[contains(@name, "follow_linkedin")]').is_displayed()
    sleep(2)
    print('linkedin link is clicked')
    sleep(5)


def add_shopping_cart_item():
    if locators.random_product != 13:
        driver.get(locators.AOS_items)
        sleep(1)
        driver.find_element(By.XPATH, '//button[contains(.,"ADD TO CART")]').click()
        sleep(1)
        print(f'Product number {locators.random_product} is added to shopping cart')
        sleep(2)
    else:
        add_shopping_cart_item()


def checkout_shopping_cart():
    print('Checkout shopping cart')
    driver.find_element(By.ID, 'menuCart').click()
    sleep(1)
    driver.find_element(By.ID, 'checkOutButton').click()
    sleep(1)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    sleep(1)
    driver.find_element(By.ID, 'next_btn').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "safepay_username")]').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@name, "safepay_password")]').send_keys(locators.new_password1)
    sleep(1)
    driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
    sleep(1)
    driver.find_element(By.TAG_NAME, 'h2').is_displayed()
    print('Thank you for buying with Advantage Online Shopping')
    sleep(1)
    tr = driver.find_element(By.ID, 'trackingNumberLabel')
    print(f'Your tracking number is: {tr.text}')
    sleep(1)
    on = driver.find_element(By.ID, 'orderNumberLabel')
    print(f'Your order number is: {on.text}')
    sleep(1)
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
    sleep(1)
    date_ordered = driver.find_element(By. XPATH, '//label[contains(., "Date ordered")]/a[@class="floater ng-binding"]')
    print(f'Date ordered: {date_ordered.text}')
    sleep(1)
    # view order
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    sleep(5)
    driver.find_element(By. XPATH, f'//*[@class="left ng-binding"]').is_displayed()
    print(f'Your order number is displayed')
    sleep(2)


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(3)
    print('You logged out\nThank you for shopping')
    sleep(3)


def delete_user_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
    sleep(1)
    driver.find_element(By.ID, 'hrefUserIcon').is_displayed()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'deletePopupBtn').click()
    sleep(2)
    print(f'User {locators.new_username} is deleted')
    sleep(1)
    #logger('deleted')
    #sleep(1)


def validate_user_deleted():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password1)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    sign_in_result_msg = driver.find_element(By.ID, 'signInResultMessage')
    if sign_in_result_msg.is_displayed():
        print('User delete validated')
        sleep(1)
    else:
        print('User is not deleted')


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
# check_homepage_texts()
# contact_us()
# social_media_link()
# new_account()
# log_out()
# log_in()
# add_shopping_cart_item()
# checkout_shopping_cart()
# check_no_order()
# delete_user_account()
# tearDown()
