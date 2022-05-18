from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class FeatureFactory(object):
    def addFeature(self,featureFilePath,featureNameGen,featureVersion,nameSpaceName,LM_name,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(featureFilePath, ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                        '$..featureLicenseModel[0].licenseModel.name'], [featureNameGen, featureVersion, nameSpaceName, LM_name], ["featureRes"], ['$'])
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,["feature_name", "feature_version", "featureRes"],['$.feature.nameVersion.name','$.feature.nameVersion.version','$'])
            LOGGER.info(self.emsVariableList["feature_name"])
            LOGGER.info(self.emsVariableList["feature_version"])
            LOGGER.info(self.emsVariableList["featureRes"])
        elif(expectedCode != None and variableList !=None and xPathList !=None):
            self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(),expectedCode, variableList,xPathList)
        return self

    def createFeature(self, feature_json, expectedCode, variableList=None, xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), expectedCode,
                             ["feature_name", "feature_version", "featureRes"],
                             ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$'])
            LOGGER.info(self.emsVariableList["feature_name"])
            LOGGER.info(self.emsVariableList["feature_version"])
            LOGGER.info(self.emsVariableList["featureRes"])
        elif (expectedCode != None and expectedCode != None and xPathList != None):
            self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)

        return self

    def getFeature(self,featureId=None,nameVersion =None,identifierNamespace=None,identifier =None,externalId =None,id=None,variableList=None,xPathList=None,expectedCode=None):
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

    def partialUpdateFeature(self, feature_json, expectedCode,id=None,nameVersion=None,identifierNamespace =None,identifier =None,externalId =None,variableList=None, xPathList=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            response = self.patchRequest(url + '/ems/api/v5/features/'+id, feature_json, currentApiFuncName(), 200,["featureUpdatedJson"],["$"])
        elif nameVersion !=None:
            response = self.patchRequest(url + '/ems/api/v5/features/nameVersion='+nameVersion, feature_json, currentApiFuncName(), 200,["featureUpdatedJson"],["$"])
        elif identifier != None:
            response = self.patchRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                                             currentApiFuncName(), 200, ["featureUpdatedJson"], ["$"])
        elif externalId != None:
            response = self.patchRequest(url + '/ems/api/v5/features/externalId=' + externalId, feature_json,
                                             currentApiFuncName(), 200, ["featureUpdatedJson"], ["$"])
        elif identifierNamespace != None:
            response = self.patchRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, feature_json,
                                             currentApiFuncName(), 200, ["featureUpdatedJson"], ["$"])
        if response[1] == expectedCode:
            LOGGER.info(self.emsVariableList["featureUpdatedJson"])
        return self

    def getFeatureProperties(self):
        return self.FeatureProperties

    def getWSFeatureProperties(self):
        return self.getWsFeatureProperties

    def searchFeature(self, id=None, identifier=None, licenseModelName=None, licenseModelId=None, namespaceId=None,
                      namespaceName=None, name=None, description=None, version=None, externalId=None, refId1=None,
                      refId2=None,variableList=None,xPathList=None,expectedCode=None):
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







