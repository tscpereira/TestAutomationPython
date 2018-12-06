# encoding: utf-8


from selenium import webdriver
from TestSDK.Logger import Logger
from appium import webdriver as AppiumWebDriver
import os
import time
import datetime
import sys

execution_failed = False
webDriver = None
webDriverMobile = None
path = ""


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
        print (str(count) + "º Scenario: '" + str(scenario.name) + "': " + str(scenario.status))
        count += 1
    print("-------------------------------------------------------------")


def after_all(context):
    if webDriver is not None:
        webDriver.quit()
    if webDriverMobile is not None:
        webDriverMobile.quit()
    if execution_failed:
        result = "FAILED"
    else:
        result = "PASSED"

    print("Saving the test output at folder '" + path + "'")
    sys.stdout = Logger(path).close()
    os.rename(path + "\TestLog.txt", path + "\TestLog_" + result + ".txt")


def before_tag(context, tag):
    global webDriver
    global webDriverMobile
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
        # TODO: Implement integration with APPIUM here (In progress)
        app = "app apk path here"
        context.driver = AppiumWebDriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '4.4',
                'deviceName': None,
                'udid': '01a135891395669f',
                'appActivity': '.HomeActivity',
                'appPackage': 'com.imdb.mobile'
            }
        )
    elif tag.startswith("UI"):
        if webDriver is None:
            context.browser = webdriver.Chrome()
            webDriver = context.browser
        else:
            context.browser = webDriver


def after_tag(context, tag):
    if tag.startswith("UI"):
        pass
