import logging
import os
import sys
import pytest

LOGGER = logging.getLogger(__name__)

class EMSAssertionFactory:

    def __init__(self):
        pass
    def verifyAssertions(self,expected,actual,verificationComments=None):
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        AssertionsReport={}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = ""
        AssertionsReport["Expected_Code"] = ""
        AssertionsReport["actual_Code"] = ""
        try:
            LOGGER.info("Comparing "+str(expected)+" Value with "+str(actual))
            assert expected == actual
            AssertionsReport["Expected_Response"] = str(expected)
            AssertionsReport["actual"] = str(actual)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = str(actual)
            AssertionsReport["Response_time"] = ""
        except AssertionError:
            AssertionsReport["Expected_Response"] = str(expected)
            AssertionsReport["actual"] = str(actual)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = str(actual)
            AssertionsReport["Response_time"] = ""
            AssertionsReport["Status"] = "Failed"
            self.data.append(AssertionsReport)
            pytest.fail("Test case is  Failed as expected value is not matched with actual value")
            LOGGER.error("expected value " + str(expected) + " is not matched with "+str(actual))

        self.data.append(AssertionsReport)
        return self


    def verifyJsonXpathxValues(self,json,jsonXpathList,tagjsonvaluesList,expectedValueList):
        pass



    def verifyJsonxpathValue(self,json,jsonXpathtag,tagvalue,expectedValue):
        pass



