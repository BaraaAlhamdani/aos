import unittest
import aos_locators as locators
import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod  # signal to Unittest that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.check_homepage_texts()
        methods.contact_us()
        methods.social_media_link()
        methods.new_account()
        methods.log_out()
        methods.log_in()
        methods.add_shopping_cart_item()
        methods.checkout_shopping_cart()
        methods.check_no_order()
        methods.delete_user_account()
        methods.tearDown()



