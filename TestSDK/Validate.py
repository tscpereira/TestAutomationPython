from nose.tools import *
from TestSDK import Log as log


def __treat_failure(fail, ex):
    if fail:
        raise ex
    else:
        start_index = ex.args[0].find("FAILED")
        print(ex.args[0][start_index:None])


def IsEqual(actual, expected, name, fail = True):
    try:
        assert_equal(actual, expected, "[FAILED] '%s' Expected [%s] Actual [%s]" % (name, expected, actual))
        log.message("[PASSED] '" + name + "' Expected [" + expected + "] Actual [" + actual + "]")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsNotEqual(first, second, name, fail = False):
    try:
        assert_not_equal(first, second, "[FAILED] '%s' First [%s] is equal to Second [%s]" % (name, first, second))
        log.message("[PASSED] '" + name + "' Value [" + first + "] is not equal to [ " + second + "]")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsIn(container, value, name, fail = False):
    try:
        assert_in(value, container, "[FAILED] '%s' Value [%s] is not in [%s]" % (name, value, container))
        log.message("[PASSED] '" + name + "' Value [" + value + "] is in [" + container + "]")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsNotIn(container, value, name, fail = False):
    try:
        assert_not_in(value, "[FAILED] '%s' Value [%s] is in [%s]" % (name, value, container))
        log.message("[PASSED] '" + name + "' Value [" + value + "] is not in [" + container + "]")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsTrue(object, name, fail = False):
    try:
        assert_true(object, "[FAILED] '" + name + "' Expected [True] Actual [False]")
        log.message("[PASSED] '" + name + "' Value is True")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsFalse(object, name, fail = False):
    try:
        assert_false(object, "[FAILED] '" + name + "' Expected [False] Actual [True]")
        log.message("[PASSED] '" + name + "' Value is False")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsNotNone(object, name, fail = False):
    try:
        assert_is_not_none(object, "[FAILED] '" + name + "' Expected [NotNone] Actual [None]")
        log.message("[PASSED] '" + name + "' Expected [NotNone] Actual [" + object + "]")
    except AssertionError as ex:
        __treat_failure(fail, ex)


def IsNone(object, name, fail = False):
    try:
        assert_is_none(object, "[FAILED] '" + name + "' Expected [None] Actual [" + object + "]")
        log.message("[PASSED] '" + name + "' Expected [None] Actual [None]")
    except AssertionError as ex:
        __treat_failure(fail, ex)