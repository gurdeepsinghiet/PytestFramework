import json
import os
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class LicenseModelfactory(object):

    def updateLicencezModelAttribute(LM_ATTR_Name , value, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value

    def getEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response = self.getRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',"",currentApiFuncName(),200)
        if response[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(response[0])
            enforcementId = response_Enforcement["enforcement"]["id"]
            self.enforcementProps = [enforcementId]
        return self

    def searchEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response = self.getRequest(url + '/ems/api/v5/enforcements?name=Sentinel RMS',"",currentApiFuncName(),200)
        if response[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(response[0])
            enforcementId = response_Enforcement["enforcements"]["enforcement"][0]["id"]
            self.enforcementProps = [enforcementId]
        return self

    def getEnforcementId(self) ->list:
        return self.enforcementProps

    def searchFlexibleLicenseModel(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.searchEnforcement();
        enforcementId=self.getEnforcementId()[0];
        responseFlexibleLicenseModel = self.getRequest(url +'/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model', "", currentApiFuncName(),200)
        if responseFlexibleLicenseModel[1] == 200:
            flexibleLicenseModelJson = utility.convertJsontoDictinary(responseFlexibleLicenseModel[0])
            LOGGER.info(flexibleLicenseModelJson)
            self.FlexibleLicenseModelJson = flexibleLicenseModelJson
        return self

    def addFlexibleLicenceModelStandalone(self, LMNameGenerator, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + self.RandomString(9)
        response_LM_json1 = json.dumps(response_LM_json)
        response = self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                    response_LM_json1, currentApiFuncName(), 201)
        if response[1] == 201:
            lmNetworkJson = utility.convertJsontoDictinary(response[0])
            LM_name = lmNetworkJson["licenseModel"]["name"]
            lmId = lmNetworkJson["licenseModel"]["id"]
            self.LMStandaloneProperties = [LM_name, lmId]
        return self

    def updateLicencezModelAttribute(self, LM_ATTR_Name, value, response_LM_json):

        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value
        return self

    def addFlexibleLicenceModelNetwork(self, LMNameGenerator, response_LM_json):
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + self.RandomString(9)
        response_LM_json1 = json.dumps(response_LM_json)
        response = self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), 201)
        if response[1] == 201:
            lmNetworkJson = utility.convertJsontoDictinary(response[0])
            LM_name = lmNetworkJson["licenseModel"]["name"]
            lmId = lmNetworkJson["licenseModel"]["id"]
            self.LMNeworksProperties = [LM_name, lmId]
        return self

    def getLMStandProperties(self):
        return self.LMStandaloneProperties

    def getLMNetworkProperties(self):
        return self.LMNeworksProperties
