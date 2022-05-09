from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element_by_class_name("btn-add-to-basket")
        button.click()

    def should_be_alert_success(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "Alert success is not presented"

    def should_be_alert_info(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "Alert info is not presented"

    def should_be_alert_displayed(self):
        self.should_be_alert_success()
        self.should_be_alert_info()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not displayed"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not displayed"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def check_the_success_message(self):
        success_message = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        assert len(success_message) == 3, "Success message is not displayed"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        success_message_name, success_message_price = success_message[0].text, success_message[2].text
        assert product_name == success_message_name, "Wrong product name in the basket"
        assert product_price == success_message_price, "Wrong product price in the basket"
