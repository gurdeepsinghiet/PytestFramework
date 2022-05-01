import json
import requests
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
import os
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class FeatureFactory(object):
    def addFeature(self, FeatureNameGenerator, featureJsonPath, LM_name, nameSpace_name):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        FeatureFileData = utility.readFile(featureJsonPath)
        LOGGER.info(FeatureFileData)
        feature_json_object = utility.convertJsontoDictinary(FeatureFileData)
        feature_json_object["feature"]["namespace"]["name"] = nameSpace_name
        feature_json_object["feature"]["nameVersion"]["name"] = FeatureNameGenerator + self.RandomString(9)
        feature_json_object["feature"]["nameVersion"]["version"] = "1.0"
        feature_json_object["feature"]["featureLicenseModels"]["featureLicenseModel"][0]["licenseModel"][
            "name"] = LM_name
        feature_json = utility.convertDictinarytoJson(feature_json_object)
        LOGGER.info(feature_json)
        response = self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), "201")
        if response[1] == 201 or response[1] == 204 or response[1] == 200:
            featureDictinary = utility.convertJsontoDictinary(response[0])
            feature_name = featureDictinary["feature"]["nameVersion"]["name"]
            feature_version = featureDictinary["feature"]["nameVersion"]["version"]
            self.FeatureProperties = [feature_name, feature_version,]
        return self

    def getFeatureProperties(self):
        return self.FeatureProperties