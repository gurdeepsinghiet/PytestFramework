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
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
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
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
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
            reportParam.setInputs(u.convertDictinarytoJson(requestBody))
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
                getapiAuthResponse = requests.get(requestUrl, data=requestBody, headers=headers,auth=(username, password))
            elif(bearerAuth == "Yes"):
                getapiAuthResponse = requests.get(requestUrl, data=requestBody, headers=headers)
            LOGGER.info(getapiAuthResponse.text)
            if getapiAuthResponse.status_code == expectedresCode and self.isJson(getapiAuthResponse.text):
                reportParam.setInputs("")
                LOGGER.info(getapiAuthResponse.text)
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

            elif getapiAuthResponse.status_code == expectedresCode and self.isXml(getapiAuthResponse.text):
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                reportParam.setInputs("")
                self.emsVariableList[outputXmlResVar] = getapiAuthResponse.text
                myRoot = ET.fromstring(getapiAuthResponse.text)
                for i, xpath in enumerate(xPathList):
                    selected_Tag = myRoot.find(xpath)
                    self.emsVariableList[variableList[i]] = selected_Tag.text
                    reportParam.setActualCode(getapiAuthResponse.status_code)
                    reportParam.setResponseTime(getapiAuthResponse.elapsed.total_seconds())
                    getRes = getapiAuthResponse.text.replace("<", "&lt").replace(">", "&gt")
                    reportParam.setActualRespone(getRes)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
            else:
                reportParam.setInputs("")
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
            reportParam.setInputs("")
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
            LOGGER.error(e)
            pytest.fail("Connection error with server")
        self.data.append(reportParam.getReportParameters())
        self.getAuthApiresponse = [getapiAuthResponse.text, getapiAuthResponse.status_code,
                                   reportParam.getReportParameters()]
        LOGGER.info(self.data)
        return self

    def PatchAuthRequest(self, requestUrl, requestBody,headers,ApiName,expectedresCode,username,password,variableList=None,xPathList=None,bearerAuth=None,outputXmlResVar=None):
        u=UtilityClass()
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setExpectedCode(expectedresCode)
            if(bearerAuth == None):
                patchApiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers,auth=(username, password))
            else:
                patchApiAuthResponse = requests.post(requestUrl, data=requestBody, headers=headers)
                LOGGER.info(patchApiAuthResponse.text)
            # Collectin data for Report
            self.output = patchApiAuthResponse.text
            if patchApiAuthResponse.status_code == expectedresCode and self.isJson(patchApiAuthResponse.text):
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                reportParam.setActualCode(patchApiAuthResponse.status_code)
                reportParam.setResponseTime(patchApiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(patchApiAuthResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (variableList != None and xPathList != None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(patchApiAuthResponse.text, variableList[i], xPathList[i])
            elif patchApiAuthResponse.status_code == expectedresCode and  self.isXml(patchApiAuthResponse.text):
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                requestBody=requestBody.replace("<","&lt").replace(">","&gt")
                reportParam.setInputs(requestBody)
                self.emsVariableList[outputXmlResVar]=patchApiAuthResponse.text
                myRoot = ET.fromstring(patchApiAuthResponse.text)
                for i, xpath in enumerate(xPathList):
                    selected_Tag = myRoot.find(xpath)
                    self.emsVariableList[variableList[i]] = selected_Tag.text
                reportParam.setActualCode(patchApiAuthResponse.status_code)
                reportParam.setResponseTime(patchApiAuthResponse.elapsed.total_seconds())
                putRes=patchApiAuthResponse.text.replace("<", "&lt").replace(">", "&gt")
                reportParam.setActualRespone(putRes)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
            else:
                reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                reportParam.setActualCode(patchApiAuthResponse.status_code)
                reportParam.setResponseTime(patchApiAuthResponse.elapsed.total_seconds())
                reportParam.setActualRespone(patchApiAuthResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(patchApiAuthResponse.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setInputs(u.convertDictinarytoJson(requestBody))
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.data.append(reportParam.getReportParameters())
        self.patchAuthApiResponse = [patchApiAuthResponse.text, patchApiAuthResponse.status_code, reportParam.getReportParameters()]
        LOGGER.info(self.data)
        return self

    def deleteAuthRequest(self, requestUrl, requestBody, headers, ApiName, expectedresCode, username, password,
                          resvariableList=None, resxPathList=None, bearerAuth=None, outputXmlResVar=None):
        u = UtilityClass()
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setExpectedCode(expectedresCode)
            if (bearerAuth == None):
                deleteapiAuthResponse = requests.delete(requestUrl, data=requestBody, headers=headers,
                                                        auth=(username, password))
            elif (bearerAuth == "Yes"):
                deleteapiAuthResponse = requests.delete(requestUrl, data=requestBody, headers=headers)
                LOGGER.info(deleteapiAuthResponse.text+"mmmmm")
            if (deleteapiAuthResponse.text != ""):
                if deleteapiAuthResponse.status_code == expectedresCode and self.isJson(deleteapiAuthResponse.text):
                    reportParam.setInputs("")
                    LOGGER.info(deleteapiAuthResponse.text)
                    reportParam.setActualCode(deleteapiAuthResponse.status_code)
                    reportParam.setResponseTime(deleteapiAuthResponse.elapsed.total_seconds())
                    reportParam.setActualRespone("Entity deleted successfully")
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    if (resvariableList != None and resxPathList != None):
                        for i, jsonxpath in enumerate(resxPathList):
                            LOGGER.info(resxPathList[i])
                            LOGGER.info(resvariableList[i])
                            self.getJsonXpathValue(deleteapiAuthResponse.text, resvariableList[i], resxPathList[i])
                elif deleteapiAuthResponse.status_code == expectedresCode and self.isXml(deleteapiAuthResponse.text):
                    reportParam.setInputs(u.convertDictinarytoJson(requestBody))
                    reportParam.setInputs("")
                    self.emsVariableList[outputXmlResVar] = deleteapiAuthResponse.text
                    myRoot = ET.fromstring(deleteapiAuthResponse.text)
                    for i, xpath in enumerate(resxPathList):
                        selected_Tag = myRoot.find(xpath)
                        self.emsVariableList[resvariableList[i]] = selected_Tag.text
                        reportParam.setActualCode(deleteapiAuthResponse.status_code)
                        reportParam.setResponseTime(deleteapiAuthResponse.elapsed.total_seconds())
                        getRes = deleteapiAuthResponse.text.replace("<", "&lt").replace(">", "&gt")
                        reportParam.setActualRespone(getRes)
                        reportParam.setStatus("Pass")
                        reportParam.setExpectedResponse("")
                else:
                    reportParam.setInputs("")
                    reportParam.setActualCode(deleteapiAuthResponse.status_code)
                    reportParam.setResponseTime(deleteapiAuthResponse.elapsed.total_seconds())
                    reportParam.setActualRespone(deleteapiAuthResponse.text)
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(deleteapiAuthResponse.text)
                    pytest.fail("Response code not matched")
            elif(deleteapiAuthResponse.text  == ""):
                if deleteapiAuthResponse.status_code == expectedresCode:
                    reportParam.setInputs("")
                    reportParam.setActualCode(deleteapiAuthResponse.status_code)
                    reportParam.setResponseTime(deleteapiAuthResponse.elapsed.total_seconds())
                    reportParam.setActualRespone("Entity deleted successfully")
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                else:
                    reportParam.setInputs("")
                    reportParam.setActualCode(deleteapiAuthResponse.status_code)
                    reportParam.setResponseTime(deleteapiAuthResponse.elapsed.total_seconds())
                    reportParam.setActualRespone(deleteapiAuthResponse.text)
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(deleteapiAuthResponse.text)
                    pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setInputs(u.convertDictinarytoJson(requestBody))
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.data.append(reportParam.getReportParameters())
            LOGGER.error(e)
            pytest.fail("Connection error with server")
        self.data.append(reportParam.getReportParameters())
        self.deleteapiAuthResponse = [deleteapiAuthResponse.text, deleteapiAuthResponse.status_code,
                                      reportParam.getReportParameters()]
        LOGGER.info(self.data)
        return self