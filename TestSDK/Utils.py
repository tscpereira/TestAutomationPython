# encoding: utf-8

import os
from xml.dom import minidom


class Utils:

    def __init__(self, context):
        self.context = context
        pass

    def take_screenshot(self, final_file_name=None):
        if final_file_name is None:
            final_file_name = "screenshot"

        filename = final_file_name
        index = 1
        while os.path.exists(self.context.artifacts_dir + "\\" + filename + ".jpg"):
            index += 1
            filename = filename + "_" + str(index)

        if index > 1:
            final_file_name = final_file_name + "_" + str(index)

        self.context.browser.save_screenshot(self.context.artifacts_dir + "\\" + final_file_name + ".jpg")

    @staticmethod
    def read_test_settings_info(tag):
        mydoc = minidom.parse("..\\testSettings.xml")
        items = mydoc.getElementsByTagName(tag)
        return items[0].firstChild.data
