from selenium.common.exceptions import TimeoutException

from Test_suite.pages.base_page import BasePage
from Test_suite.pages.selectors import DashboardPageSelectors, AddNewProductCartSelectors


class AdminProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def open_product_tab(self):
        catalog_link = self.find_element(DashboardPageSelectors.CATALOG_LINK)
        catalog_link.click()
        product_link = self.find_element(DashboardPageSelectors.PRODUCT_LINK)
        product_link.click()
        try:
            return self.find_elements(DashboardPageSelectors.PRODUCT_TAB)
        except TimeoutException:
            return 'TimeoutException'

    def add_new_product(self, p_name='Mouse', m_tag='pereferi', model='M23-546S'):
        self.open_product_tab()
        add_new_product_button = self.find_element(DashboardPageSelectors.ADD_NEW)
        add_new_product_button.click()
        product_name = self.find_element(AddNewProductCartSelectors.PRODUCT_NAME)
        product_name.send_keys(p_name)
        meta_tag = self.find_element(AddNewProductCartSelectors.META_TAG)
        meta_tag.send_keys(m_tag)
        self.find_element(AddNewProductCartSelectors.DATA_TAB).click()
        model_field = self.find_element(AddNewProductCartSelectors.MODEL)
        model_field.send_keys(model)
        save_button = self.find_element(AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()

    def is_product_in_tab(self, p_name='Mouse'):
        products_tab = self.open_product_tab()
        product_name_field = self.find_element(DashboardPageSelectors.PRODUCT_NAME_FIELD)
        product_name_field.send_keys(p_name)
        filter_button = self.find_element(DashboardPageSelectors.FILTER_BUTTON)
        filter_button.click()
        products_tab = self.find_elements(DashboardPageSelectors.PRODUCT_TAB)
        for el in products_tab:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                return True
        return False

    def get_checkbox_by_product_name(self, p_name='Mouse'):
        products_tab = self.open_product_tab()
        for el in products_tab:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                checkbox = el.find_element_by_css_selector('tr td:nth-child(1)')
                return checkbox

        return False

    def get_edit_button_by_product_name(self, p_name='Mouse'):
        products_tab = self.open_product_tab()
        for el in products_tab:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                edit_button = el.find_element_by_css_selector('tr td:nth-child(8)')
                return edit_button

    def delete_product_from_tab(self, p_name='Mouse'):
        products_tab = self.open_product_tab()
        checkbox = self.get_checkbox_by_product_name(p_name)
        checkbox.click()
        delete_button = self.find_element(DashboardPageSelectors.DELETE)
        delete_button.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()
