# encoding: utf-8

from TestSDK.Element import Element
from TestSDK.Utils import Utils
from selenium.webdriver.common.keys import Keys


class SamplePage:

    def __init__(self, context):
        self.context = context
        self.searchField = Element("//*[@title='Pesquisar']", context, "Search field")
        self.searchButton = Element("//*[@class='gLFyf gsfi']", context, "Search button")
        self.overPage = Element("//*[@id='lga']", context, "Over page")
        self.spanTitle = Element("//span[text()='%s']", context, "Span Title")
        self.utils = Utils(context)

    def search(self, item):
        self.searchField.type(item)
        self.searchField.send_keys(Keys.RETURN)

