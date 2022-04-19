import numpy as np
import requests
import json
import Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword



class LicenseModelfactory(object):

    def addFlexibleLicenceModelStandalone(self,LMNameGenerator, response_LM_json):
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + str(np.random.randint(1000000, 9000000))
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
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        response_LM_json["licenseModel"]["name"] = LMNameGenerator + str(np.random.randint(1000000, 7000000))
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
