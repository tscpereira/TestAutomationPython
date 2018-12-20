# encoding: utf-8

import xml.etree.ElementTree as ET
import os


class Utils:

    context = None

    def __init__(self, context):
        self.context = context
        pass

    def take_screenshot(self, finalfilename=None):
        if finalfilename is None:
            finalfilename = "screenshot"

        filename = finalfilename
        index = 1
        while os.path.exists(self.context.artifacts_dir + "\\" + filename + ".jpg"):
            index += 1
            filename = filename + "_" + str(index)

        if index > 1:
            finalfilename = finalfilename + "_" + str(index)

        self.context.browser.save_screenshot(self.context.artifacts_dir + "\\" + finalfilename + ".jpg")

    # Work in progress
    @staticmethod
    def read_xml_input_data(self):
        tree = ET.parse('C:\\test_data.xml')
        root = tree.getroot()

        for elem in root:
            for subelem in elem.findall('user'):
                print(subelem.attrib)
                print(subelem.get('name'))
