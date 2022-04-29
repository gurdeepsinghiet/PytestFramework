import requests
import json
import os
import Constant
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
