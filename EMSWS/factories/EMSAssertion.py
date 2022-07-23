import logging
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import pytest
from EMSWS.ReportParameters import ReportParam

LOGGER = logging.getLogger(__name__)

class EMSAssertionFactory:

    def __init__(self):
        pass
    def verify_assertions(self,expected,actual,verification_comments=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        report_param = ReportParam()
        report_param.setApiName(current_api_name())
        report_param.setInputs("")
        report_param.setExpectedCode("")
        report_param.setActualCode("")
        try:
            LOGGER.info("Comparing "+str(expected)+" Value with "+str(actual))
            assert expected == actual
            report_param.setResponseTime("")
            report_param.setActualRespone(str(actual))
            report_param.setStatus("Pass")
            report_param.setExpectedResponse(str(expected))
        except AssertionError:
            report_param.setResponseTime("")
            report_param.setActualRespone(str(actual))
            report_param.setStatus("Failed")
            report_param.setExpectedResponse(str(expected))
            self.report_data.append(report_param.getReportParameters())
            LOGGER.error("expected value " + str(expected) + " is not matched with " + str(actual))
            pytest.fail("Test case is  Failed as expected value is not matched with actual value")
        self.report_data.append(report_param.getReportParameters())
        return self

    def verify_json_path_values(self, json_dictionary, json_tag_list, expected_value_list):
        for i, json_path in enumerate(json_tag_list):
            jsonpath_expression = parse(json_path)
            match = jsonpath_expression.find(json_dictionary)
            self.verify_assertions(expected_value_list[i],match[0].value)
        return self


    def verify_json_path_value(self,json_dictionary,json_tag,expected_value):
        jsonpath_expression = parse(json_tag)
        match = jsonpath_expression.find(json_dictionary)
        LOGGER.info(match[0].value)
        self.verify_assertions(expected_value,match[0].value)
        return self



