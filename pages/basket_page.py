from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert self.in_current_url("basket"), "Substring 'basket' doesn't exist in current url"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
