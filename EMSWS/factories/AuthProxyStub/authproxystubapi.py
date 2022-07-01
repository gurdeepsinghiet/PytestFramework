import requests
import logging
import EMSWS.EMSConfig as Constant
from EMSWS.ReportParameters import ReportParam
import pytest
import json
from EMSWS.Utilities import UtilityClass
import xml.etree.ElementTree as ET

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL


class RestAuthProxyStubFactory(object):
    def post_stub_request(self, request_url, request_body, headers, api_name, expected_res_code, username, password,
                          session_id, variable_list=None, xpath_list=None, bearer_auth=None,
                          output_xml_res_var=None,is_session_based_request=None
                          ):
        u = UtilityClass()
        report_param = ReportParam()
        try:
            report_param.setApiName(api_name)
            report_param.setExpectedCode(expected_res_code)
            if bearer_auth is None and is_session_based_request is None:
                stub_response = requests.post(request_url, data=request_body, headers=headers,
                                              auth=(username, password))
                LOGGER.info(stub_response.text)
            elif bearer_auth == "Yes":
                stub_response = requests.post(request_url, data=request_body, headers=headers)
                LOGGER.info(stub_response.text)
            elif bearer_auth is None and is_session_based_request == "Yes":
                stub_response = requests.post(request_url, data=request_body, headers=headers,
                                              cookies="JSESSIONID=" + session_id)
                LOGGER.info(stub_response.text)
            # Collecting data for Report
            if stub_response.status_code == expected_res_code and self.isJson(stub_response.text):
                report_param.setInputs(u.convertDictinarytoJson(request_body))
                report_param.setActualCode(stub_response.status_code)
                report_param.setResponseTime(stub_response.elapsed.total_seconds())
                report_param.setActualRespone(stub_response.text)
                report_param.setStatus("Pass")
                report_param.setExpectedResponse("")
                if variable_list is not None and xpath_list is not None:
                    for i, json_xpath in enumerate(xpath_list):
                        LOGGER.info(xpath_list[i])
                        LOGGER.info(variable_list[i])
                        self.getJsonXpathValue(stub_response.text, variable_list[i], xpath_list[i])
            elif stub_response.status_code == expected_res_code and self.isXml(stub_response.text):
                report_param.setInputs(u.convertDictinarytoJson(request_body))
                request_body = request_body.replace("<", "&lt").replace(">", "&gt")
                report_param.setInputs(request_body)
                self.emsVariableList[output_xml_res_var] = stub_response.text
                my_root = ET.fromstring(stub_response.text)
                for i, xpath in enumerate(xpath_list):
                    selected_tag = my_root.find(xpath)
                    self.emsVariableList[variable_list[i]] = selected_tag.text
                report_param.setActualCode(stub_response.status_code)
                report_param.setResponseTime(stub_response.elapsed.total_seconds())
                post_resp = stub_response.text.replace("<", "&lt").replace(">", "&gt")
                report_param.setActualRespone(post_resp)
                report_param.setStatus("Pass")
                report_param.setExpectedResponse("")
            else:
                report_param.setInputs(u.convertDictinarytoJson(request_body))
                report_param.setActualCode(stub_response.status_code)
                report_param.setResponseTime(stub_response.elapsed.total_seconds())
                report_param.setActualRespone(stub_response.text)
                report_param.setStatus("Failed")
                report_param.setExpectedResponse("")
                self.data.append(report_param.getReportParameters())
                LOGGER.error(stub_response.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            report_param.setInputs(u.convertDictinarytoJson(request_body))
            report_param.setActualCode("500")
            report_param.setResponseTime("")
            report_param.setActualRespone(e)
            report_param.setStatus("Failed")
            report_param.setExpectedResponse("")
            self.data.append(report_param.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)

        self.data.append(report_param.getReportParameters())
        LOGGER.info(self.data)

        return self
