# encoding: utf-8

from behave import *
from Pages.SamplePage import SamplePage
from TestSDK import APISDK
from TestSDK.Utils import Utils
from collections import namedtuple
import json


@given('Im in the google page')
def access_googe(context):

    global samplepage
    global utils
    utils = Utils(context)
    samplepage = SamplePage(context)

    print("- Acessing google")
    try:
        context.browser.get("http://www.google.com")
    except Exception:
        print("Unable to complete the tests step:")
        raise


@when('Search by "{item}"')
def search_item(context, item):
    try:
        print("- Searching for: '" + item + "'")
        samplepage.search(item)
    except Exception:
        print("Unable to complete the tests step:")
        raise


@then('Check the results')
def search_item(context):
    try:
        print("- Checking the results")
        utils.take_screenshot("SearchResult.jpg")
    except Exception:
        print("Unable to complete the tests step:")
        raise


@given('I need run a get at google API')
def run_google_request(context):
    try:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        payload = dict(
            location='-33.8670,151.1957',
            radius='500',
            types='food',
            name='cruise',
            key='AIzaSyDf3CAWByILoUJUqgVpRlyJ6yxS9bf5DOA'
        )

        response = APISDK.post(url, payload)
        dtoresponse = json.loads(response.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        # In this print we are accessing the property "lat" from response
        print ("Lat: " + str(dtoresponse.results[0].geometry.location.lat))
        assert dtoresponse.status == "OK", "The request status is NOT OK. \nCurrent status: '" \
                                     + str(response.__getattribute__('status')) + "'"
    except Exception:
        print("Unable to complete the tests step:")
        raise
