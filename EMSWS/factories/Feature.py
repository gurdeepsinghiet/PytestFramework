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
        response = self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), 200)
        if response[1] == 200:
            featureDictinary = utility.convertJsontoDictinary(response[0])
            feature_name = featureDictinary["feature"]["nameVersion"]["name"]
            feature_version = featureDictinary["feature"]["nameVersion"]["version"]
            self.FeatureProperties = [feature_name, feature_version]
        return self

    def getFeature(self,featureId=None,nameVersion =None,identifierNamespace=None,identifier =None,externalId =None,id=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if featureId !=None:
            response = self.getRequest(url + '/ems/api/v5/features/featureId='+featureId, "", currentApiFuncName(), 200)
        elif id !=None:
            response = self.getRequest(url + '/ems/api/v5/features/' + id, "", currentApiFuncName(), 200)
        elif nameVersion !=None:
            response = self.getRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, "", currentApiFuncName(), 200)
        elif identifierNamespace != None:
            response = self.getRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, "", currentApiFuncName(), 200)
        elif identifier != None:
            response = self.getRequest(url + '/ems/api/v5/features/identifier=' + identifier, "", currentApiFuncName(), 200)
        elif externalId != None:
            response = self.getRequest(url + '/ems/api/v5/features/externalId=' + externalId, "", currentApiFuncName(), 200)
        if response[1] == 200:
            featureJson = utility.convertJsontoDictinary(response[0])
            feature_name = featureJson["feature"]["nameVersion"]["name"]
            feature_version = featureJson["feature"]["nameVersion"]["version"]
            self.getWsFeatureProperties = [feature_name, feature_version,response[0]]
            LOGGER.info(featureJson)
        return self

    def searchFeature(self):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()


    def getFeatureProperties(self):
        return self.FeatureProperties

    def getWSFeatureProperties(self):
        return self.getWsFeatureProperties