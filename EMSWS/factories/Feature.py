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
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        feature_json = self.UpdateJsonPath(featureJsonPath, ['$.feature.nameVersion.name','$.feature.nameVersion.version','$..namespace.name','$..featureLicenseModel[0].licenseModel.name'],
                                           [FeatureNameGenerator + self.RandomString(9),"1.0",nameSpace_name,LM_name])
        LOGGER.info(feature_json)
        response = self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), 201)
        if response[1] == 201:
            featureDictinary = utility.convertJsontoDictinary(response[0])
            feature_name = featureDictinary["feature"]["nameVersion"]["name"]
            feature_version = featureDictinary["feature"]["nameVersion"]["version"]
            self.FeatureProperties = [feature_name, feature_version]
        return self

    def getFeature(self,featureId=None,nameVersion =None,identifierNamespace=None,identifier =None,externalId =None,id=None):
        utility = UtilityClass()
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

    def searchFeature(self, id=None, identifier=None, licenseModelName=None, licenseModelId=None, namespaceId=None,
                      namespaceName=None, name=None, description=None, version=None, externalId=None, refId1=None,
                      refId2=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responeurl=""
        if (id != None):
            responeurl +="id="+id+"&"
        if (identifier != None):
            responeurl +="identifier="+identifier+"&"
        if (licenseModelName != None):
            responeurl += "licenseModelName=" + licenseModelName + "&"
        if (licenseModelId != None):
            responeurl += "licenseModelId=" + licenseModelId + "&"
        if (namespaceId != None):
            responeurl += "namespaceId=" + namespaceId + "&"
        if (namespaceName != None):
            responeurl += "namespaceName=" + namespaceName + "&"
        if (name != None):
            responeurl += "name=" + name + "&"
        if (description != None):
            responeurl += "description=" + description + "&"
        if (version != None):
            responeurl += "version=" + version + "&"
        if (externalId != None):
            responeurl += "externalId=" + externalId + "&"
        if (refId1 != None):
            responeurl += "refId1=" + refId1 + "&"
        if (refId2 != None):
            responeurl += "refId2=" + refId2 + "&"
        LOGGER.info(url +"/ems/api/v5/features?"+ responeurl[0:-1])
        response = self.getRequest(url +"/ems/api/v5/features?"+ responeurl[0:-1], "", currentApiFuncName(), 200)
        if response[1] == 200:
                featureJson = utility.convertJsontoDictinary(response[0])
                feature_name = featureJson["feature"]["nameVersion"]["name"]
                feature_version = featureJson["feature"]["nameVersion"]["version"]
                self.getWsFeatureProperties = [feature_name, feature_version, response[0]]
                LOGGER.info(featureJson)
        return self



