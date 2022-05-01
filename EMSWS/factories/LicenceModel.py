import requests
import json
import os
import sys
import pytest
from jsonpath_ng.ext import parse
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class LicenseModelfactory(object):

    def updateLicencezModelAttribute(LM_ATTR_Name, value, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value

    def getEnforcement(self):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        responseEnforcement = requests.get(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',
                                           auth=(username, password))
        response_Enforcement = json.loads(responseEnforcement.text)
        LOGGER.info(response_Enforcement)
        enforcementId = response_Enforcement["enforcement"]["id"]
        self.enforcementProps = [enforcementId]
        return self

    def searchFlexibleLicenseModel(self):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        LOGGER.info(currentFuncName())
        FlexibleLicenseModelReportPorps = {}
        FlexibleLicenseModelReportPorps["Api_Name"] = currentFuncName()
        FlexibleLicenseModelReportPorps["inputs"] = ""
        FlexibleLicenseModelReportPorps["Expected_Code"] = "201"
        responseEnforcement = requests.get(url + '/ems/api/v5/enforcements?name=Sentinel RMS',
                                           auth=(username, password))
        if responseEnforcement.status_code == 201 or responseEnforcement.status_code == 204 or responseEnforcement.status_code == 200:
            FlexibleLicenseModelReportPorps["actual_Code"] = responseEnforcement.status_code
            FlexibleLicenseModelReportPorps["Response_time"] = responseEnforcement.elapsed.total_seconds()
            FlexibleLicenseModelReportPorps["Status"] = "Pass"
            response_Enforcement = json.loads(responseEnforcement.text)
            FlexibleLicenseModelReportPorps["Act_Response"] = "response_Enforcement"
            FlexibleLicenseModelReportPorps["Expected_Response"] = ""
            LOGGER.info(response_Enforcement)
            enforcementId = response_Enforcement["enforcements"]["enforcement"][0]["id"]
            self.enforcementProps = [enforcementId]
            responseFlexibleLicenseModel = requests.get(url + '/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model',auth=(username, password))
            if responseFlexibleLicenseModel.status_code == 201 or responseFlexibleLicenseModel.status_code == 204 or responseFlexibleLicenseModel.status_code == 200:
                response_LM_json = json.loads(responseFlexibleLicenseModel.text)
                LOGGER.info(response_LM_json)
                self.FlexibleLicenseModelJson = response_LM_json
                self.data.append(FlexibleLicenseModelReportPorps)

            else:
                LOGGER.error(responseFlexibleLicenseModel.text)
                pytest.fail("getting FlexibleLicenseModel is giving error failed")
        else:
            LOGGER.error(responseEnforcement.text)
            pytest.fail("getting Enforcement is giving error failed")
        return self


    def getEnforcementId(self) ->list:
        return self.enforcementProps


    def addFlexibleLicenceModelStandalone(self,LMNameGenerator, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + self.RandomString(9)
        response_LM_json1 = json.dumps(response_LM_json)
        responseLM1 = requests.post(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                    response_LM_json1, auth=(username, password))
        responseTextLM = json.loads(responseLM1.text)
        LOGGER.info(responseTextLM)
        LM_name = responseTextLM["licenseModel"]["name"]
        lmId = response_LM_json["licenseModel"]["id"]
        self.LMStandaloneProperties=[LM_name, lmId]
        return self

    def updateLicencezModelAttribute(self,LM_ATTR_Name, value, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value
        return self

    def addFlexibleLicenceModelNetwork(self,LMNameGenerator, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + self.RandomString(9)
        response_LM_json1 = json.dumps(response_LM_json)
        responseLM1 = requests.post(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                    response_LM_json1, auth=(username, password))
        responseTextLM = json.loads(responseLM1.text)
        LOGGER.info(responseTextLM)
        LM_name = responseTextLM["licenseModel"]["name"]
        lmId = response_LM_json["licenseModel"]["id"]
        self.LMNeworksProperties = [LM_name, lmId]
        return self

    def getLMStandProperties(self):
        return self.LMStandaloneProperties


    def getLMNetworkProperties(self):
        return self.LMNeworksProperties
