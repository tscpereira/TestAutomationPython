# encoding: utf-8
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.mobileby import MobileBy
from TestSDK import Log as log


class Element(object):

    def __init__(self, seletor, context, name=None, by=By.XPATH, mobileBy = MobileBy.XPATH, context_view = ""):
        self.seletor = seletor
        self.context = context
        self.by = by
        self.mobileBy = mobileBy
        if name is not None:
            self.name = name
        else:
            self.name = seletor

    def get_element(self, timeout=20):
        try:
            return WebDriverWait(self.context.browser, timeout).until(ec.presence_of_element_located((self.by, self.seletor)))
        except Exception:
            log.message("Element '" + str(self.name) + "' not found")
            raise

    def get_element_appium(self, timeout=20):
        try:
            return WebDriverWait(self.context.browser, timeout).until(
                ec.element_to_be_clickable((self.mobileBy, self.seletor)))
        except Exception:
            log.message("Element '" + str(self.name) + "' not found")
            raise

    def find(self):
        return self.context.browser.find_element_by_xpath(self.seletor)

    def get_select_element(self):
        element = self.get_element()
        element.wait_for_visible()
        return Select(element)

    def click(self):
        element = self.get_element()
        log.message("Clicking at element '" + self.name + "'")
        element.click()

    def clickAppium(self, context_view = None):
        self.__check_and_switch_context(context_view)
        element = self.get_element_appium()
        log.message("Clicking at element '" + self.name + "'")
        element.click()

    def tap(self):
        element = self.get_element_appium(self.seletor)
        log.message("Clicking at element '" + self.name + "'")
        element.tap()

    def is_available(self, timeout=5):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.context.browser, timeout).until(ec.presence_of_element_located((self.by, self.seletor)))
            return True
        except Exception:
            return False

    def is_visible(self, fail = True):
        element = self.get_element()
        # noinspection PyBroadException
        try:
            element.is_displayed()
            if fail:
                log.message("[PASSED] '" + self.name + "' was displayed")
            return True
        except Exception as ex:
            if fail:
                log.message(ex)
                log.message("[FAILED] '" + self.name + "' was not displayed")
                raise
            return False

    def is_enabled(self, fail = True):
        element = self.get_element()
        # noinspection PyBroadException
        try:
            element.is_enabled()
            if fail:
                log.message("[PASSED] '" + self.name + "' was enabled")
            return True
        except Exception:
            if fail:
                log.message("[FAILED] '" + self.name + "' was not enabled")
                raise
            return False

    def wait_for_visible(self, timeout=20):
        try:
            WebDriverWait(self.context.browser, timeout).until(ec.visibility_of_element_located((self.by, self.seletor)))
        except Exception:
            log.message("After '" + str(timeout) + "' secconds the element '" + self.name + "' was not displayed")
            raise

    def wait_for_visible_and_click(self, timeout=20):
        try:
            element = WebDriverWait(self.context.browser, timeout).until(ec.element_to_be_clickable((self.by, self.seletor)))
            element.click()
        except Exception:
            log.message("After '" + str(timeout) + "' secconds the element '" + self.name + "' was not displayed")
            raise

    def wait_for_invisible(self, timeout=20):
        WebDriverWait(self.context.browser, timeout).until(
            ec.invisibility_of_element_located((self.by, self.seletor)))
        raise Exception("After '" + str(timeout) + "' secconds the element '"
                        + self.name + "' is stiil being displayed")

    def wait_for_text(self, expected_text, attempts = 5):
        attempt = 0
        while attempt < attempts:
            if self.get_text() ==  expected_text:
                break
            else:
                attempt = attempt + 1
                log.message("Waiting for text '" + expected_text + "' attempt '" + str(attempt) + "' of '" + str(attempts) + "'")
                time.sleep(3)

    def get_text(self):
        element = self.get_element()
        return element.text

    def get_textbox_value(self, context_view = None):
        self.__check_and_switch_context(context_view)
        element = self.get_element()
        return element.get_attribute('value')

    def get_selected_text(self, context_view = None):
        self.__check_and_switch_context(context_view)
        element = self.get_element()
        select = Select(element)
        return select.first_selected_option.text

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

    def __check_and_switch_context(self, context_view):
        if context_view is not None and context_view not in self.context.browser.context:
            self.context.browser.switch_to.context(context_view)
