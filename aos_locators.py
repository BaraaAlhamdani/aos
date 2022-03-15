from faker import Faker
fake = Faker(locale='en_CA')
import random
# -------------- Locators section ---------------
AOS_url = 'https://advantageonlineshopping.com/#/'
AOS_title = '\xa0Advantage Shopping'
AOS_registration_url = 'https://advantageonlineshopping.com/#/register'
AOS_my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
AOS_chat_with_us_url = 'https://advantageonlineshopping.com/chat.html'
AOS_chat_with_us_title = 'Advantage Online Shopping Demo Support Chat'
AOS_order_payment = 'https://advantageonlineshopping.com/#/orderPayment'


# -------- data section -------------
first_name = fake.first_name()[:7]
last_name = fake.last_name()[:7]
middle_name = fake.first_name()
full_name = f'{first_name}{""} {last_name}'
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
new_password1 = 'Password1'
email = f'{new_username}@{fake.free_email_domain()}'
phone = fake.phone_number()[:10]
country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province()[:10]
postal_code = fake.postcode()
description = fake.sentence(nb_words=20)
random_product = random.randint(1, 34)
AOS_items = f'https://advantageonlineshopping.com/#/product/{random_product}'

#-------------------------------------------------------------