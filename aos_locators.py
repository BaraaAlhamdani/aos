from faker import Faker
fake = Faker(locale='en_CA')
# -------------- Locators section ---------------
AOS_url = 'https://advantageonlineshopping.com/#/'
AOS_title = '\xa0Advantage Shopping'
AOS_registration_url = 'https://advantageonlineshopping.com/#/register'
AOS_my_account_url = 'https://advantageonlineshopping.com/#/myAccount'

# -------- data section -------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name}{last_name}'
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
new_password1 = 'Password1'
email = f'{new_username}@{fake.free_email_domain()}'
phone = fake.phone_number()
country = fake.current_country()
#-------------------------------------------------------------