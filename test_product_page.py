import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.positive
class TestProductPagePositive():
    @pytest.mark.parametrize('promo_number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_guest_can_add_product_to_basket(self, browser, promo_number):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_name()
        product_page.should_be_product_price()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_alert_displayed()
        product_page.check_the_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.negative
class TestProductPageNegative():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link=LINK):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link=LINK):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link=LINK):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_disappeared_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link=LINK):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_that_basket_is_empty()
