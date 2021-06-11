# encoding: utf-8


from selenium import webdriver
from TestSDK.Logger import Logger
from os.path import basename
from TestSDK.Utils import Utils
import os
import time
import datetime
import sys
import zipfile

zipOutput = True
execution_failed = False
webDriver = None
webDriverMobile = None
webDriverAppium = None
path = ""
dc = {}


def before_all(context):
    global path
    path = os.getcwd() + "\\..\\TestResults"
    date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    path = path + "\\Execution_" + date
    if not os.path.exists(path):
        os.makedirs(path)
        context.artifacts_dir = path
    else:
        absolutepath = os.path.abspath(path)
        raise Exception("Unable to start the test, folder already exist: '" + absolutepath + "'")

    sys.stdout = Logger(path)
    print("Test Execution Date: " + str(datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')))


def before_feature(context, feature):
    print("-------------- Starting Feature Test Execution --------------")
    print("Feature '" + str(feature.name) + "' with '" + str(len(feature.scenarios)) + "' scenarios")
    print("-------------------------------------------------------------")


def before_scenario(context, scenario):
    print("\nExecuting scenario: " + str(scenario.name) + "\n")


def after_scenario(context, scenario):
    status = None
    if context.failed:
        status = "FAILED"
    else:
        status = "PASSED"
    print("\nFinishing scenario: '" + str(scenario.name) + "' TEST STATUS: " + status)
    if scenario.status == "failed":
        global execution_failed
        execution_failed = True


def after_feature(context, feature):
    print("\n------------- Finishing Feature Test Execution --------------")
    count = 1
    for scenario in feature.scenarios:
        print(str(count) + "º Scenario: '" + str(scenario.name) + "': " + str(scenario.status))
        count += 1
    print("-------------------------------------------------------------")


def after_all(context):
    if webDriver is not None:
        webDriver.quit()
    if webDriverMobile is not None:
        webDriverMobile.quit()
    if webDriverAppium is not None:
        webDriverAppium.quit()
    if execution_failed:
        result = "FAILED"
    else:
        result = "PASSED"

    print("Saving the test output at folder '" + os.path.abspath(path) + "'")
    sys.stdout = Logger(path).close()
    os.rename(path + "\TestLog.txt", path + "\TestLog_" + result + ".txt")

    if zipOutput:
        zpFile = zipfile.ZipFile(path + '\\Output.zip', 'w')
        files = __get_files()

        for file in files:
            if not '.zip' in file:
                zpFile.write(file, basename(file), compress_type=zipfile.ZIP_DEFLATED)
                os.remove(file)
        zpFile.close()


def before_tag(context, tag):
    global webDriver
    global webDriverMobile
    global webDriverAppium

    if tag.startswith("UI-WEB-MOBILE"):
        if webDriverMobile is None:
            mobile_emulation = {"deviceName": "Galaxy S5"}
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            context.browser = webdriver.Chrome(chrome_options=chrome_options)
            webDriverMobile = context.browser
        else:
            context.browser = webDriverMobile
    elif tag.startswith("UI-APP-MOBILE"):
        if webDriverAppium is None:
            utils = Utils(context)
            dc['app'] = utils.read_test_settings_info("apkPath")
            dc['appPackage'] = utils.read_test_settings_info("appPackage")
            dc['appActivity'] = utils.read_test_settings_info("appActivity")
            dc['platformName'] = utils.read_test_settings_info("platformName")
            dc['deviceName'] = utils.read_test_settings_info("deviceName")
            context.browser = webdriver.Remote("http://localhost:4723/wd/hub", dc)
            webDriverAppium = context.browser
        else:
            context.browser = webDriverAppium
    elif tag.startswith("UI"):
        if webDriver is None:
            context.browser = webdriver.Chrome()
            webDriver = context.browser
        else:
            context.browser = webDriver


def after_tag(context, tag):
    if tag.startswith("UI"):
        pass


def __get_files():
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files
