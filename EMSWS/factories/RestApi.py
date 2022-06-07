import requests
import logging
import EMSWS.Constant as Constant
from EMSWS.ReportParameters import ReportParam
import pytest
import json
from EMSWS.Utilities import UtilityClass
from jsonpath_ng.ext import parse
import xml.etree.ElementTree as ET
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RestApiUtilityFactory(object):

    def PostRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None,xmlSupport=None):
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
        #return [postapiResponse.text,postapiResponse.status_code,reportParam.getReportParameters()]
        return self

    def getRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None,xmlSupport=None):

        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            getapiRes = requests.get(requestUrl, requestBody, auth=(username, password))
            LOGGER.info(getapiRes.status_code)
            # Collectin data for Report
            if getapiRes.status_code == expectedresCode:
                try:
                    response_dictionary = json.loads(getapiRes.text)
                    LOGGER.info(response_dictionary)
                    # Collecting data for Report Status if Test step Pass
                    reportParam.setActualCode(getapiRes.status_code)
                    reportParam.setResponseTime(getapiRes.elapsed.total_seconds())
                    reportParam.setActualRespone(getapiRes.text)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    if (variableList != None and xPathList != None):
                        for i, jsonxpath in enumerate(xPathList):
                            LOGGER.info(xPathList[i])
                            LOGGER.info(variableList[i])
                            self.getJsonXpathValue(getapiRes.text, variableList[i], xPathList[i])

                except json.decoder.JSONDecodeError as e:
                    reportParam.setActualCode(getapiRes.status_code)
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone("response json decode error")
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")
            else:
                LOGGER.error(getapiRes.text)
                reportParam.setActualCode(getapiRes.status_code)
                reportParam.setResponseTime(getapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(getapiRes.text)
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
        self.getApiresponse=[getapiRes.text, getapiRes.status_code, reportParam.getReportParameters()]
        #return [getapiResponse.text, getapiResponse.status_code, reportParam.getReportParameters()]
        return self
    def deleteRequest(self):
        pass

    def patchRequest(self, requestUrl, requestBody, ApiName,expectedresCode,variableList=None,xPathList=None,xmlSupport=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(ApiName)
            reportParam.setInputs(requestBody)
            reportParam.setExpectedCode(expectedresCode)
            patchapiRes = requests.patch(requestUrl, requestBody, auth=(username, password))
            LOGGER.info(patchapiRes)
            # Collectin data for Report
            if patchapiRes.status_code == expectedresCode:
                response_dictionary = json.loads(patchapiRes.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(patchapiRes.status_code)
                reportParam.setResponseTime(patchapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiRes.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (variableList != None and xPathList != None):
                    for i, jsonxpath in enumerate(xPathList):
                        LOGGER.info(xPathList[i])
                        LOGGER.info(variableList[i])
                        self.getJsonXpathValue(patchapiRes.text, variableList[i], xPathList[i])
            else:
                reportParam.setActualCode(patchapiRes.status_code)
                reportParam.setResponseTime(patchapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiRes.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.data.append(reportParam.getReportParameters())
                LOGGER.error(patchapiRes.text)
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
        self.patchApiresponse = [patchapiRes.text, patchapiRes.status_code, reportParam.getReportParameters()]
        return self

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


    def updateXMLFile(self,xmlFilePath,xpathList,xpathValueList,resVarList=None,resXpathList=None):
        xmlTree=ET.parse(xmlFilePath)
        myRoot=xmlTree.getroot()
        for i, xpath in enumerate(xpathList):
            new_tag=myRoot.find(xpath)
            new_tag.text = xpathValueList[i]
        self.xmlstroutput = ET.tostring(myRoot, encoding='unicode', method='xml')
        LOGGER.info(self.xmlstroutput)
        if (resVarList != None and resXpathList != None):
            for i,xpath in enumerate(resXpathList):
                selected_Tag = myRoot.find(xpath)
                self.emsVariableList[resVarList[i]] = selected_Tag.text
        return self


    def updateXML(self,xmlData,xpathList,xpathValueList,resVarList=None,resJpathList=None):
        pass