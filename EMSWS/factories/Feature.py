from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
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
        feature_json = self.UpdateJsonPath(featureJsonPath, ['$.feature.nameVersion.name','$.feature.nameVersion.version','$..namespace.name','$..featureLicenseModel[0].licenseModel.name'],
                                           [FeatureNameGenerator + self.RandomString(9),"1.0",nameSpace_name,LM_name])
        LOGGER.info(feature_json)
        response = self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), "201")
        if response[1] == 201 or response[1] == 204 or response[1] == 200:
            featureDictinary = utility.convertJsontoDictinary(response[0])
            feature_name = featureDictinary["feature"]["nameVersion"]["name"]
            feature_version = featureDictinary["feature"]["nameVersion"]["version"]
            self.FeatureProperties = [feature_name, feature_version]
        return self

    def getFeatureProperties(self):
        return self.FeatureProperties