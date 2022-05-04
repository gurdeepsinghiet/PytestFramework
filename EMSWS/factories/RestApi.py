import requests
import logging
import EMSWS.Constant as Constant
from EMSWS.ReportParameters import ReportParam
import pytest
import json
from jsonpath_ng.ext import parse
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RestApiUtilityFactory(object):

    def PostRequest(self, requestUrl, requestBody, ApiName,expectedresCode):
        reportParam = ReportParam()

        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            postapiResponse = requests.post(requestUrl, requestBody,auth=(username, password))
            LOGGER.info(postapiResponse)
            # Collectin data for Report
            if postapiResponse.status_code == 201 or postapiResponse.status_code == 204 or postapiResponse.status_code == 200:
                response_dictionary = json.loads(postapiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
            else:
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(postapiResponse.text)
                pytest.fail("Problem with creating Entity")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
            LOGGER.error(e)
        self.data.append(reportParam.getReportParameters())
        LOGGER.info(self.data)
        return [postapiResponse.text,postapiResponse.status_code,reportParam.getReportParameters()]

    def getRequest(self, requestUrl, requestBody, ApiName,expectedresCode):

        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            getapiResponse = requests.get(requestUrl, requestBody, auth=(username, password))
            # Collectin data for Report
            if getapiResponse.status_code == 201 or getapiResponse.status_code == 204 or getapiResponse.status_code == 200:
                response_dictionary = json.loads(getapiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(getapiResponse.status_code)
                reportParam.setResponseTime(getapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(getapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
            else:
                LOGGER.error(getapiResponse.text)
                reportParam.setActualCode(getapiResponse.status_code)
                reportParam.setResponseTime(getapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(getapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                pytest.fail("Problem with getting Entity")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
        self.data.append(reportParam.getReportParameters())
        LOGGER.info(self.data)
        return [getapiResponse.text, getapiResponse.status_code, reportParam.getReportParameters()]

    def deleteRequest(self):
        pass

    def patchRequest(self):
        pass

    def putRequest(self):
        pass

    def UpdateJsonPath(self,jsonpath,jsontagsList,jsonValueList):
        reportParam = ReportParam()
        reportParam.setApiName("UpdateJsonPath")
        reportParam.setInputs(jsonpath)
        reportParam.setExpectedCode("200")
        with open(jsonpath) as f:
            jsonData = json.load(f)
        LOGGER.info(jsonData)
        for i, jsonxpath in enumerate(jsontagsList):
            LOGGER.info(jsonxpath)
            jsonpath_expression = parse(jsonxpath)
            LOGGER.info(jsonpath_expression)
            jsonpath_expression.find(jsonData)
            jsonpath_expression.update(jsonData, jsonValueList[i])
        response = json.dumps(jsonData, indent=2)
        LOGGER.info(response)
        reportParam.setActualCode("200")
        reportParam.setResponseTime("")
        reportParam.setActualRespone(response)
        reportParam.setStatus("Pass")
        reportParam.setExpectedResponse("")
        self.data.append(reportParam.getReportParameters())
        return response