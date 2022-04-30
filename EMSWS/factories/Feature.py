import json
import requests
import  EMSWS.Constant as Constant
import logging
import os
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class FeatureFactory(object):
    def addFeature(self, FeatureNameGenerator, featureJsonPath, LM_name, nameSpace_name):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        featureFile = open(featureJsonPath, 'r')
        featureFileData = featureFile.read()
        feature_json_object = json.loads(featureFileData)
        featureFile.close()
        feature_json_object["feature"]["namespace"]["name"] = nameSpace_name
        feature_json_object["feature"]["nameVersion"]["name"] = FeatureNameGenerator + self.RandomString(9)
        feature_json_object["feature"]["nameVersion"]["version"] = "1.0"
        feature_json_object["feature"]["featureLicenseModels"]["featureLicenseModel"][0]["licenseModel"][
            "name"] = LM_name
        featureFile = open(featureJsonPath, "w")
        json.dump(feature_json_object, featureFile)
        featureFile.close()
        featureFile = open(featureJsonPath, 'r')
        featureUpdated_json = featureFile.read()
        responseFeature = requests.post(url + '/ems/api/v5/features', featureUpdated_json, auth=(username, password))
        responseTextFeature = json.loads(responseFeature.text)
        LOGGER.info(responseTextFeature)
        feature_name = responseTextFeature["feature"]["nameVersion"]["name"]
        feature_version = responseTextFeature["feature"]["nameVersion"]["version"]
        self.FeatureProperties = [feature_name, feature_version]
        return self

    def getFeatureProperties(self):
        return self.FeatureProperties