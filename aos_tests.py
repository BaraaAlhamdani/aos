import unittest
import aos_locators as locators
import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod  # signal to Unittest that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.new_account()
        methods.log_out()
        methods.log_in()
        methods.log_out()
        methods.tearDown()
