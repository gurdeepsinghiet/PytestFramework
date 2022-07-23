import requests
import logging
import EMSWS.EMSConfig as Constant
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


    def post_request(self, request_url, request_body, api_name, expected_return_code, out_parameter_list=None,
                     out_json_path_list=None, xmlSupport=None):

        reportParam = ReportParam()
        try:
            reportParam.setApiName(api_name)
            reportParam.setInputs(request_body)
            reportParam.setExpectedCode(expected_return_code)
            postapiResponse = requests.post(request_url, request_body, auth=(username, password))
            LOGGER.info(postapiResponse)
            # if expected code matches status_code of RestApi response,then reportParam collect Status Pass data for the report
            if postapiResponse.status_code == expected_return_code:
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if out_parameter_list != None and out_json_path_list != None:
                    for i, jsonxpath in enumerate(out_json_path_list):
                        LOGGER.info(out_json_path_list[i])
                        LOGGER.info(out_parameter_list[i])
                        self.getJsonXpathValue(postapiResponse.text, out_parameter_list[i], out_json_path_list[i])
            # if expected code does matches status_code of RestApi response,then reportParam collect Status Fail data for the report
            else:
                reportParam.setActualCode(postapiResponse.status_code)
                reportParam.setResponseTime(postapiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(postapiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                LOGGER.error(postapiResponse.text)
                # Test case will be terminate at this Step
                pytest.fail("Response code not matched")
        # the below Step handle exception in the Rest Api like Server error,Connection error etc.
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.report_data.append(reportParam.getReportParameters())
        LOGGER.info(self.report_data)
        # return [postapiResponse.text,postapiResponse.status_code,reportParam.getReportParameters()]
        return self

    def get_request(self, request_url, request_body, api_name, expected_return_code, out_parameter_list=None,
                    out_json_path_list=None, xmlSupport=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(api_name)
            reportParam.setInputs(request_body)
            reportParam.setExpectedCode(expected_return_code)
            getapiRes = requests.get(request_url, request_body, auth=(username, password))
            LOGGER.info(getapiRes.status_code)
            if getapiRes.status_code == expected_return_code:
                try:
                    reportParam.setActualCode(getapiRes.status_code)
                    reportParam.setResponseTime(getapiRes.elapsed.total_seconds())
                    reportParam.setActualRespone(getapiRes.text)
                    reportParam.setStatus("Pass")
                    reportParam.setExpectedResponse("")
                    if (out_parameter_list != None and out_json_path_list != None):
                        for i, jsonxpath in enumerate(out_json_path_list):
                            LOGGER.info(out_json_path_list[i])
                            LOGGER.info(out_parameter_list[i])
                            self.getJsonXpathValue(getapiRes.text, out_parameter_list[i], out_json_path_list[i])

                except json.decoder.JSONDecodeError as e:
                    reportParam.setActualCode(getapiRes.status_code)
                    reportParam.setResponseTime("")
                    reportParam.setActualRespone("response json decode error")
                    reportParam.setStatus("Failed")
                    reportParam.setExpectedResponse("")
                    self.report_data.append(reportParam.getReportParameters())
                    LOGGER.error(e)
                    pytest.fail("problem with json decoding")
            else:
                LOGGER.error(getapiRes.text)
                reportParam.setActualCode(getapiRes.status_code)
                reportParam.setResponseTime(getapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(getapiRes.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                pytest.fail("Problem with getting Entity")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
        self.report_data.append(reportParam.getReportParameters())
        LOGGER.info(self.report_data)
        self.getApiresponse = [getapiRes.text, getapiRes.status_code, reportParam.getReportParameters()]

        return self

    def delete_request(self, request_url, request_body, api_name, expected_return_code, out_parameter_list=None,
                       out_json_path_list=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(api_name)
            reportParam.setInputs(request_body)
            reportParam.setExpectedCode(expected_return_code)
            deleteApiresponse = requests.delete(request_url, data=request_body, auth=(username, password))
            LOGGER.info(deleteApiresponse)
            if deleteApiresponse.status_code == expected_return_code:
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(deleteApiresponse.status_code)
                reportParam.setResponseTime(deleteApiresponse.elapsed.total_seconds())
                reportParam.setActualRespone("Entity deleted successfully")
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (out_parameter_list != None and out_json_path_list != None and deleteApiresponse.text != None):
                    for i, jsonxpath in enumerate(out_json_path_list):
                        LOGGER.info(out_json_path_list[i])
                        LOGGER.info(out_parameter_list[i])
                        self.getJsonXpathValue(deleteApiresponse.text, out_parameter_list[i], out_json_path_list[i])
            else:
                reportParam.setActualCode(deleteApiresponse.status_code)
                reportParam.setResponseTime(deleteApiresponse.elapsed.total_seconds())
                reportParam.setActualRespone(deleteApiresponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                LOGGER.error(deleteApiresponse.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.report_data.append(reportParam.getReportParameters())
        LOGGER.info(self.report_data)
        self.deleteApiresponse = [deleteApiresponse.status_code, reportParam.getReportParameters()]
        return self

    def patch_request(self, request_url, request_body, api_name, expected_return_code, out_parameter_list=None,
                      out_json_path_list=None, xmlSupport=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(api_name)
            reportParam.setInputs(request_body)
            reportParam.setExpectedCode(expected_return_code)
            patchapiRes = requests.patch(request_url, request_body, auth=(username, password))
            LOGGER.info(patchapiRes)
            # Collectin data for Report
            if patchapiRes.status_code == expected_return_code:
                response_dictionary = json.loads(patchapiRes.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(patchapiRes.status_code)
                reportParam.setResponseTime(patchapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiRes.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (out_parameter_list != None and out_json_path_list != None):
                    for i, jsonxpath in enumerate(out_json_path_list):
                        LOGGER.info(out_json_path_list[i])
                        LOGGER.info(out_parameter_list[i])
                        self.getJsonXpathValue(patchapiRes.text, out_parameter_list[i], out_json_path_list[i])
            else:
                reportParam.setActualCode(patchapiRes.status_code)
                reportParam.setResponseTime(patchapiRes.elapsed.total_seconds())
                reportParam.setActualRespone(patchapiRes.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                LOGGER.error(patchapiRes.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.report_data.append(reportParam.getReportParameters())
        LOGGER.info(self.report_data)
        self.patchApiResponse = [patchapiRes.text, patchapiRes.status_code, reportParam.getReportParameters()]
        return self

    def put_request(self, request_url, request_body, api_name, expected_return_code, out_parameter_list=None,
                    out_json_path_list=None):
        reportParam = ReportParam()
        try:
            reportParam.setApiName(api_name)
            reportParam.setInputs(request_body)
            reportParam.setExpectedCode(expected_return_code)
            putApiResponse = requests.put(request_url, request_body, auth=(username, password))
            LOGGER.info(putApiResponse)
            # Collectin data for Report
            if putApiResponse.status_code == expected_return_code:
                response_dictionary = json.loads(putApiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                reportParam.setActualCode(putApiResponse.status_code)
                reportParam.setResponseTime(putApiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(putApiResponse.text)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                if (out_parameter_list != None and out_json_path_list != None):
                    for i, jsonxpath in enumerate(out_json_path_list):
                        LOGGER.info(out_json_path_list[i])
                        LOGGER.info(out_parameter_list[i])
                        self.getJsonXpathValue(putApiResponse.text, out_parameter_list[i], out_json_path_list[i])
            else:
                reportParam.setActualCode(putApiResponse.status_code)
                reportParam.setResponseTime(putApiResponse.elapsed.total_seconds())
                reportParam.setActualRespone(putApiResponse.text)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                LOGGER.error(putApiResponse.text)
                pytest.fail("Response code not matched")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
            reportParam.setActualCode("500")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            pytest.fail("Connection error with server")
            LOGGER.error(e)
        self.report_data.append(reportParam.getReportParameters())
        LOGGER.info(self.report_data)
        self.putApiResponse = [putApiResponse.text, putApiResponse.status_code, reportParam.getReportParameters()]
        return self

    def UpdateJsonFile(self, json_file_path, json_tags_list, json_value_list, out_parameter_list=None, out_json_path_list=None):
        utilityClass = UtilityClass()
        reportParam = ReportParam()
        reportParam.setApiName("UpdateJsonPath")
        reportParam.setInputs(json_file_path)
        reportParam.setExpectedCode("200")
        try:
            with open(self.getModulePath() + json_file_path) as f:
                json_data = json.load(f)
                LOGGER.info(json_data)
                for i, jsonxpath in enumerate(json_tags_list):
                    LOGGER.info(jsonxpath)
                    jsonpath_expression = parse(jsonxpath)
                    LOGGER.info(jsonpath_expression)
                    jsonpath_expression.find(json_data)
                    jsonpath_expression.update(json_data, json_value_list[i])
                response = json.dumps(json_data, indent=2)
                LOGGER.info(response)
                reportParam.setActualCode("200")
                reportParam.setResponseTime("")
                reportParam.setActualRespone(response)
                reportParam.setStatus("Pass")
                reportParam.setExpectedResponse("")
                self.UpdateJsonFileResponse = response
                if out_parameter_list is not None and out_json_path_list is not None:
                    for i, jsonxpath in enumerate(out_json_path_list):
                        self.getJsonXpathValue(response, out_parameter_list[i], out_json_path_list[i])
                self.report_data.append(reportParam.getReportParameters())

        except FileNotFoundError as e:
            reportParam.setActualCode("404")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            LOGGER.error(e)
            pytest.fail("File Not found at this path")
        except json.decoder.JSONDecodeError as e:
            reportParam.setActualCode("404")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            LOGGER.error(e)
            pytest.fail("problem with json decoding")
        except TypeError as e:
            reportParam.setActualCode("404")
            reportParam.setResponseTime("")
            reportParam.setActualRespone(e)
            reportParam.setStatus("Failed")
            reportParam.setExpectedResponse("")
            self.report_data.append(reportParam.getReportParameters())
            LOGGER.error(e)
            pytest.fail("problem with json decoding")
        return self

    def UpdateJson(self, jsonDictionary, jsontagsList, jsonValueList, resVarList=None, resJpathList=None):
        utilityClass = UtilityClass()
        reportParam = ReportParam()
        reportParam.setApiName("UpdateJson")
        reportParam.setInputs(utilityClass.convertDictinarytoJson(jsonDictionary))
        reportParam.setExpectedCode("200")
        for i, jsonxpath in enumerate(jsontagsList):
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
                self.report_data.append(reportParam.getReportParameters())
            except TypeError as e:
                reportParam.setActualCode("404")
                reportParam.setResponseTime("")
                reportParam.setActualRespone(e)
                reportParam.setStatus("Failed")
                reportParam.setExpectedResponse("")
                self.report_data.append(reportParam.getReportParameters())
                LOGGER.error(e)
                pytest.fail("problem with json decoding")
        return self

    def updateXMLFile(self, xmlFilePath, out_json_path_list, xpathValueList, resVarList=None,
                      resout_json_path_list=None):
        xmlTree = ET.parse(self.getModulePath() +xmlFilePath)
        myRoot = xmlTree.getroot()
        for i, xpath in enumerate(out_json_path_list):
            new_tag = myRoot.find(xpath)
            new_tag.text = xpathValueList[i]
        self.xmlstroutput = ET.tostring(myRoot, encoding='unicode', method='xml')
        LOGGER.info(self.xmlstroutput)
        if (resVarList != None and resout_json_path_list != None):
            for i, xpath in enumerate(resout_json_path_list):
                selected_Tag = myRoot.find(xpath)
                self.out_param_List[resVarList[i]] = selected_Tag.text
        return self

    def updateXML(self, xml_data, out_json_path_list, xpathValueList, resVarList=None, resout_json_path_list=None):
        myRoot = ET.fromstring(xml_data)
        for i, xpath in enumerate(out_json_path_list):
            new_tag = myRoot.find(xpath)
            new_tag.text = xpathValueList[i]
        self.xmlstroutput = ET.tostring(myRoot, encoding='unicode', method='xml')
        LOGGER.info(self.xmlstroutput)
        if (resVarList != None and resout_json_path_list != None):
            for i, xpath in enumerate(resout_json_path_list):
                selected_Tag = myRoot.find(xpath)
                self.emsout_parameter_list[resVarList[i]] = selected_Tag.text
        return self


