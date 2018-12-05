# encoding: utf-8

from TestSDK.Element import Element
from TestSDK.Utils import Utils


class SamplePage:

    context, searchButton, searchField, overPage = None, None, None, None
    utils = None

    seletorSearchButton = "//*[@id='tsf']/div[2]/div/div[3]/center/input[1]"
    seletorSearchField = "//*[@class='gLFyf gsfi']"
    seletorOverPage = "//*[@id='lga']"

    def __init__(self, context):
        self.context = context
        self.searchField = Element(self.seletorSearchField, context, "Search field")
        self.searchButton = Element(self.seletorSearchButton, context, "Search button")
        self.overPage = Element(self.seletorOverPage, context, "Over page")
        self.utils = Utils(context)

    def search(self, item):
        self.searchField.type(item)
        self.overPage.click()
        self.searchButton.click()
