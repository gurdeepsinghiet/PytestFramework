import logging
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import pytest
from EMSWS.ReportParameters import ReportParam

LOGGER = logging.getLogger(__name__)

class EMSAssertionFactory:

    def __init__(self):
        pass
    def verifyAssertions(self,expected,actual,verificationComments=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        reportParam = ReportParam()
        reportParam.setApiName(currentApiFuncName())
        reportParam.setInputs("")
        reportParam.setExpectedCode("")
        reportParam.setActualCode("")
        try:
            LOGGER.info("Comparing "+str(expected)+" Value with "+str(actual))
            assert expected == actual
            reportParam.setResponseTime("")
            reportParam.setActualRespone(str(actual))
            reportParam.setStatus("Pass")
            reportParam.setExpectedResponse(str(expected))
        except AssertionError:
            reportParam.setResponseTime("")
            reportParam.setActualRespone(str(actual))
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse(str(expected))
            self.data.append(reportParam.getReportParameters())
            LOGGER.error("expected value " + str(expected) + " is not matched with " + str(actual))
            pytest.fail("Test case is  Failed as expected value is not matched with actual value")
        self.data.append(reportParam.getReportParameters())
        return self


    def verifyJsonXpathValues(self,jsonDictionary,jsontagList,expectedValueList):
        for i, jsonxpath in enumerate(jsontagList):
            jsonpath_expression = parse(jsonxpath)
            match = jsonpath_expression.find(jsonDictionary)
            self.verifyAssertions(match[0].value,expectedValueList[i])
        self


    def verifyJsonxpathValue(self,jsonDictionary,jsontag,expectedValue):
        jsonpath_expression = parse(jsontag)
        match = jsonpath_expression.find(jsonDictionary)
        LOGGER.info(match[0].value)
        self.verifyAssertions(expectedValue,match[0].value)
        self



