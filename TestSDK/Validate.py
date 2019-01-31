from nose.tools import *


def IsEqual(actual, expected, name, errorMessage = None):
    print("Validating '" + name + "' Expected [" + expected + "] Actual [" + actual + "]")
    assert_equal(actual, expected, errorMessage)

def IsNotEqual(actual, notEqual, name, errorMessage=None):
    print("Validating '" + name + "' Actual [" + actual + "]")
    assert_not_equal(actual, notEqual, errorMessage)

def IsIn(container, expectedText, errorMessage = None):
    print("Validating if [" + expectedText + "] is in [" + container + "]")
    assert_in(expectedText, container, errorMessage)

def IsNotIn(container, expectedText, errorMessage = None):
    print("Validating if [" + expectedText + "] is not in [" + container + "]")
    assert_not_in(expectedText, container, errorMessage)

def IsTrue(object, errorMessage=None):
    print("Validating if [" + object + "] is true")
    assert_true(object, errorMessage)

def IsFalse(object, errorMessage=None):
    print("Validating if [" + object + "] is false")
    assert_false(object, errorMessage)