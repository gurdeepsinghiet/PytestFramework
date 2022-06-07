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
    def PostAuthRequest(self, requestUrl, requestBody,headers,ApiName,expectedresCode,username,password,variableList=None,xPathList=None,bearerAuth=None,outputXmlResVar=None):
        u=UtilityClass()
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setExpectedCode(expectedresCode)
            if(bearerAuth == None):
                postapiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers,auth=(username, password))
            elif (bearerAuth == "Yes"):
                postapiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers)
                LOGGER.info(postapiAuthResponse.text)
            # Collectin data for Report
            if postapiAuthResponse.status_code == expectedresCode and self.isJson(postapiAuthResponse.text):
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
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
            elif postapiAuthResponse.status_code == expectedresCode and  self.isXml(postapiAuthResponse.text):
                requestBody=requestBody.replace("<","&lt").replace(">","&gt")
                reportParam.setInputs(requestBody)
                self.emsVariableList[outputXmlResVar]=postapiAuthResponse.text
                myRoot = ET.fromstring(postapiAuthResponse.text)
                for i, xpath in enumerate(xPathList):
                    selected_Tag = myRoot.find(xpath)
                    self.emsVariableList[variableList[i]] = selected_Tag.text
                reportParam.setActualCode(postapiAuthResponse.status_code)
                reportParam.setResponseTime(postapiAuthResponse.elapsed.total_seconds())
                postRes=postapiAuthResponse.text.replace("<", "&lt").replace(">", "&gt")
                reportParam.setActualRespone(postRes)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
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


    def GetAuthRequest(self, requestUrl, requestBody,headers,ApiName,expectedresCode,username,password,variableList=None,xPathList=None,bearerAuth=None,outputXmlResVar=None):
        u=UtilityClass()
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setExpectedCode(expectedresCode)
            if(bearerAuth == None):
                getapiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers,auth=(username, password))
            else:
                getapiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers)
                LOGGER.info(getapiAuthResponse.text)
            # Collectin data for Report
            self.output = getapiAuthResponse.text
            if getapiAuthResponse.status_code == expectedresCode and self.isJson(getapiAuthResponse.text):
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                response_dictionary = json.loads(getapiAuthResponse.text)
                # LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(getapiAuthResponse.status_code)
                reportParam.setResponseTime(getapiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(getapiAuthResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (variableList != None and xPathList != None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(getapiAuthResponse.text, variableList[i], xPathList[i])
            elif getapiAuthResponse.status_code == expectedresCode and  self.isXml(getapiAuthResponse.text):
                requestBody=requestBody.replace("<","&lt").replace(">","&gt")
                reportParam.setInputs(requestBody)
                self.emsVariableList[outputXmlResVar]=getapiAuthResponse.text
                myRoot = ET.fromstring(getapiAuthResponse.text)
                for i, xpath in enumerate(xPathList):
                    selected_Tag = myRoot.find(xpath)
                    self.emsVariableList[variableList[i]] = selected_Tag.text
                reportParam.setActualCode(getapiAuthResponse.status_code)
                reportParam.setResponseTime(getapiAuthResponse.elapsed.total_seconds())
                getRes=getapiAuthResponse.text.replace("<", "&lt").replace(">", "&gt")
                reportParam.setActualRespone(getRes)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
            else:
                reportParam.setActualCode(getapiAuthResponse.status_code)
                reportParam.setResponseTime(getapiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(getapiAuthResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(getapiAuthResponse.text)
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
        self.getAuthApiresponse = [getapiAuthResponse.text, getapiAuthResponse.status_code, reportParam.getReportParameters()]
        LOGGER.info(self.data)
        return self