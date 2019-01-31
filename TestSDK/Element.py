# encoding: utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Element(object):

    seletor = None
    context = None
    name = None
    by = None

    def __init__(self, seletor, context, name=None, by=By.XPATH):
        self.seletor = seletor
        self.context = context
        self.by = by
        if name is not None:
            self.name = name
        else:
            self.name = seletor

    def get_element(self, timeout=20):
        try:
            return WebDriverWait(self.context.browser, timeout).until(ec.presence_of_element_located((self.by, self.seletor)))
        except Exception:
            print("Element '" + str(self.name) + "' not found")
            raise

    def get_select_element(self):
        element = self.get_element()
        element.wait_for_visible()
        return Select(element)

    def click(self):
        element = self.get_element()
        element.click()

    def is_available(self, timeout=5):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.context.browser, timeout).until(ec.presence_of_element_located((self.by, self.seletor)))
            return True
        except Exception:
            return False

    def is_visible(self):
        element = self.get_element()
        # noinspection PyBroadException
        try:
            element.is_displayed()
            return True
        except Exception:
            return False

    def is_enabled(self):
        element = self.get_element()
        # noinspection PyBroadException
        try:
            element.is_enabled()
            return True
        except Exception:
            return False

    def wait_for_visible(self, timeout=20):
        try:
            WebDriverWait(self.context.browser, timeout).until(ec.visibility_of_element_located((self.by, self.seletor)))
        except Exception:
            print("After '" + str(timeout) + "' secconds the element '" + self.name + "' was not displayed")
            raise

    def wait_for_visible_and_click(self, timeout=20):
        try:
            element = WebDriverWait(self.context.browser, timeout).until(ec.element_to_be_clickable((self.by, self.seletor)))
            element.click()
        except Exception:
            print("After '" + str(timeout) + "' secconds the element '" + self.name + "' was not displayed")
            raise

    # TODO: Inlcude By option thru parameter instead of hardcoded find_element_by_xpath
    def wait_for_invisible(self, timeout=20):
        element = self.context.browser.find_element_by_xpath(self.seletor)
        attempt = 0

        while attempt < timeout:
            if not element.is_displayed():
                return
            else:
                attempt += 1
        raise Exception("After '" + str(timeout) + "' secconds the element '"
                        + self.name + "' is stiil being displayed")

    def get_text(self):
        element = self.get_element()
        return element.text

    def type(self, keys):
        element = self.get_element()
        return element.send_keys(keys)
    
    def select_by_index(self, index):
        return self.get_select_element().select_by_index(index)

    def select_by_value(self, value):
        return self.get_select_element().select_by_value(value)

    def select_by_text(self, text):
        return self.get_select_element().select_by_visible_text(text)

    def deselect_by_index(self, index):
        return self.get_select_element().deselect_by_index(index)

    def deselect_by_value(self, value):
        return self.get_select_element().deselect_by_value(value)

    def deselect_by_text(self, text):
        return self.get_select_element().deselect_by_visible_text(text)

    def send_keys(self, keys):
        element = self.get_element()
        return element.send_keys(keys)