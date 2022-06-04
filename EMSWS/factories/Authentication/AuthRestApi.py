import requests
import logging
import EMSWS.Constant as Constant
from EMSWS.ReportParameters import ReportParam
import pytest
import json
from EMSWS.Utilities import UtilityClass
import xml.etree.ElementTree as ET

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL


class RestApiAuthFactory(object):
    def PostAuthRequest(self, requestUrl, requestBody,headers, ApiName, expectedresCode, username,password,variableList=None,xPathList=None):
        u=UtilityClass()
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(u.convertDictinarytoJson(requestBody))
            reportParam.setExpectedCode(expectedresCode)
            postapiAuthResponse = requests.post(requestUrl, requestBody, headers=headers,auth=(username, password))
            # LOGGER.info(postapiResponse)
            # Collectin data for Report
            if postapiAuthResponse.status_code == expectedresCode:
                response_dictionary = json.loads(postapiAuthResponse.text)
                # LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(postapiAuthResponse.status_code)
                reportParam.setResponseTime(postapiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiAuthResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (variableList != None and xPathList != None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(postapiAuthResponse.text, variableList[i], xPathList[i])
            else:
                reportParam.setActualCode(postapiAuthResponse.status_code)
                reportParam.setResponseTime(postapiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiAuthResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(postapiAuthResponse.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.data.append(reportParam.getReportParameters())
        LOGGER.info(self.data)

        return self


