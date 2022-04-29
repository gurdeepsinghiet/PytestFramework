import logging
import os
import sys
import pytest

LOGGER = logging.getLogger(__name__)

class EMSAssertionFactory:

    def __init__(self):
        pass
    def getAssertions(self,expected,actual):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        AssertionsReport={}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = ""
        AssertionsReport["Expected_Code"] = ""
        AssertionsReport["actual_Code"] = ""
        try:
            LOGGER.info("Comparing "+expected+" Value with "+actual)
            assert expected == actual
            AssertionsReport["Expected_Response"] = expected
            AssertionsReport["actual"] = actual
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = actual
            AssertionsReport["Response_time"] = ""
        except AssertionError:
            AssertionsReport["Expected_Response"] = expected
            AssertionsReport["actual"] = actual
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = actual
            AssertionsReport["Response_time"] = ""
            AssertionsReport["Status"] = "Failed"
            self.data.append(AssertionsReport)
            pytest.fail("Test case is not Failed as expected value is not matched with actual value")
            LOGGER.error("expected value " + expected + " is not matched with "+actual)

        self.data.append(AssertionsReport)
        return self