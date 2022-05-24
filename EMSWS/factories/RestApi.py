import requests
import logging
import EMSWS.Constant as Constant
from EMSWS.ReportParameters import ReportParam
import pytest
import json
from EMSWS.Utilities import UtilityClass
from jsonpath_ng.ext import parse
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RestApiUtilityFactory(object):

    def PostRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            postapiResponse = requests.post(requestUrl, requestBody,auth=(username, password))
            #LOGGER.info(postapiResponse)
            # Collectin data for Report
            if postapiResponse.status_code == expectedresCode:
                response_dictionary = json.loads(postapiResponse.text)
                #LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if(variableList != None and xPathList !=None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(postapiResponse.text,variableList[i],xPathList[i])
            else:
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(postapiResponse.text)
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
        return [postapiResponse.text,postapiResponse.status_code,reportParam.getReportParameters()]

    def getRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None):

        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            getapiResponse = requests.get(requestUrl, requestBody, auth=(username, password))
            LOGGER.info(getapiResponse.status_code)
            # Collectin data for Report
            if getapiResponse.status_code == expectedresCode:
                try:
                    response_dictionary = json.loads(getapiResponse.text)
                    LOGGER.info(response_dictionary)
                    # Collecting data for Report Status if Test step Pass
                    reportParam.setActualCode(getapiResponse.status_code)
                    reportParam.setResponseTime(getapiResponse.elapsed.total_seconds())
                    reportParam.setActualRespone(getapiResponse.text)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    if (variableList != None and xPathList != None):
                        for i, jsonxpath in enumerate(xPathList):
                            self.getJsonXpathValue(getapiResponse.text, variableList[i], xPathList[i])
                except json.decoder.JSONDecodeError as e:
                    reportParam.setActualCode(getapiResponse.status_code)
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone("response json decode error")
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")
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

    def patchRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            patchapiResponse = requests.patch(requestUrl, requestBody, auth=(username, password))
            LOGGER.info(patchapiResponse)
            # Collectin data for Report
            if patchapiResponse.status_code == expectedresCode:
                response_dictionary = json.loads(patchapiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(patchapiResponse.status_code)
                reportParam.setResponseTime(patchapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (variableList != None and xPathList != None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(patchapiResponse.text, variableList[i], xPathList[i])
            else:
                reportParam.setActualCode(patchapiResponse.status_code)
                reportParam.setResponseTime(patchapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(patchapiResponse.text)
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
        return [patchapiResponse.text, patchapiResponse.status_code, reportParam.getReportParameters()]

    def putRequest(self):
        pass

    def UpdateJsonFile(self,jsonpath,jsontagsList,jsonValueList,variableList=None,xPathList=None):
        utilityClass=UtilityClass()
        reportParam = ReportParam()
        reportParam.setApiName("UpdateJsonPath")
        reportParam.setInputs(jsonpath)
        reportParam.setExpectedCode("200")
        with open(jsonpath) as f:
            try:
                jsonData = json.load(f)
                LOGGER.info(jsonData)
                for i, jsonxpath in enumerate(jsontagsList):
                    LOGGER.info(jsonxpath)
                    jsonpath_expression = parse(jsonxpath)
                    LOGGER.info(jsonpath_expression)
                    jsonpath_expression.find(jsonData)
                    jsonpath_expression.update(jsonData, jsonValueList[i])
                try:
                    response = json.dumps(jsonData, indent=2)
                    LOGGER.info(response)
                    reportParam.setActualCode("200")
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone(response)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    self.UpdateJsonFileResponse=response
                    if (variableList != None and xPathList != None):
                        for i,jsonxpath in enumerate(xPathList):
                            self.getJsonXpathValue(response, variableList[i], xPathList[i])
                    self.data.append(reportParam.getReportParameters())
                except TypeError as e:
                    reportParam.setActualCode("404")
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone(e)
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")

            except json.decoder.JSONDecodeError as e:
                reportParam.setActualCode("404")
                reportParam.setResponseTime("")
                reportParam.setActualRespone(e)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(e)
                pytest.fail("problem with json decoding")
        return self

    def UpdateJson(self,jsonDictionary,jsontagsList,jsonValueList,resVarList=None,resJpathList=None):
        utilityClass=UtilityClass()
        reportParam = ReportParam()
        reportParam.setApiName("UpdateJsonPath")
        reportParam.setInputs(utilityClass.convertDictinarytoJson(jsonDictionary))
        reportParam.setExpectedCode("200")
        for i,jsonxpath in enumerate(jsontagsList):
            LOGGER.info(jsonxpath)
            jsonpath_expression = parse(jsonxpath)
            LOGGER.info(jsonpath_expression)
            jsonpath_expression.find(jsonDictionary)
            jsonpath_expression.update(jsonDictionary, jsonValueList[i])
            LOGGER.info(jsonDictionary)
            try:
                response = json.dumps(jsonDictionary, indent=2)
                LOGGER.info(response)
                reportParam.setActualCode("200")
                reportParam.setResponseTime("")
                reportParam.setActualRespone(response)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (resVarList != None and resJpathList != None):
                    for i, jsonxpath in enumerate(resJpathList):
                        self.getJsonXpathValue(response, resVarList[i], resJpathList[i])
                    self.data.append(reportParam.getReportParameters())
            except TypeError as e:
                    reportParam.setActualCode("404")
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone(e)
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")

        return self


    def PostRequestSelf(self, requestUrl, requestBody, ApiName,expectedresCode,resVarList=None,resJpathList=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            postapiResponse = requests.post(requestUrl, requestBody,auth=(username, password))
            LOGGER.info(postapiResponse)
            # Collectin data for Report
            if postapiResponse.status_code == expectedresCode:
                response_dictionary = json.loads(postapiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if(resVarList != None and resJpathList !=None):
                    for i, jsonxpath in enumerate(resVarList):
                        self.getJsonXpathValue(postapiResponse.text,resVarList[i],resJpathList[i])
            else:
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(postapiResponse.text)
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


    def getRequestself(self, requestUrl, requestBody, ApiName,expectedresCode,resVarList=None,resJpathList=None):

        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            getapiResponse = requests.get(requestUrl, requestBody, auth=(username, password))
            LOGGER.info(getapiResponse.status_code)
            # Collectin data for Report
            if getapiResponse.status_code == expectedresCode:
                try:
                    response_dictionary = json.loads(getapiResponse.text)
                    LOGGER.info(response_dictionary)
                    # Collecting data for Report Status if Test step Pass
                    reportParam.setActualCode(getapiResponse.status_code)
                    reportParam.setResponseTime(getapiResponse.elapsed.total_seconds())
                    reportParam.setActualRespone(getapiResponse.text)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    if (resVarList != None and resJpathList != None):
                        for i, jsonxpath in enumerate(resJpathList):
                            self.getJsonXpathValue(getapiResponse.text, resVarList[i], resJpathList[i])
                except json.decoder.JSONDecodeError as e:
                    reportParam.setActualCode(getapiResponse.status_code)
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone("response json decode error")
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")
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
        return self