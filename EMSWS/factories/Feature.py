from EMSWS.Utilities import UtilityClass
import  EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class FeatureFactory(object):

    def addFeature(self,nameSpaceName,LM_name,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(JsonPath.featureJsonPath, ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                        '$..featureLicenseModel[0].licenseModel.name'], ["Ftr"+self.RandomString(9), "1.0", nameSpaceName, LM_name], ["featureRes"], ['$'])
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,["feature_name", "feature_version", "featureRes"],['$.feature.nameVersion.name','$.feature.nameVersion.version','$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif(expectedReturnCode != None and outParameterList !=None and outJsonPathList !=None):
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(),expectedReturnCode, outParameterList,outJsonPathList)
        return self
    def addFeatureJsonFilePath(self,featureFilePath,featureNameGen,featureVersion,nameSpaceName,LM_name,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(featureFilePath, ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                        '$..featureLicenseModel[0].licenseModel.name'], [featureNameGen, featureVersion, nameSpaceName, LM_name], ["featureRes"], ['$'])
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,["feature_name", "feature_version", "featureRes"],['$.feature.nameVersion.name','$.feature.nameVersion.version','$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif(expectedReturnCode != None and outParameterList !=None and outJsonPathList !=None):
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(),expectedReturnCode, outParameterList,outJsonPathList)
        return self

    def addFeatureJson(self, feature_json, expectedReturnCode, outParameterList=None, outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), expectedReturnCode,
                             ["feature_name", "feature_version", "featureRes"],
                             ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif (expectedReturnCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/features', feature_json, currentApiFuncName(), expectedReturnCode,
                             outParameterList, outJsonPathList)

        return self

    def getFeature(self,outParameterList,outJsonPathList,expectedReturnCode,featureId=None,nameVersion =None,identifierNamespace=None,identifier =None,externalId =None,id=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if featureId !=None:
            self.getRequest(url + '/ems/api/v5/features/'+featureId, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif id !=None:
            self.getRequest(url + '/ems/api/v5/features/' + id, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif nameVersion !=None:
            self.getRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif identifierNamespace != None:
            self.getRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif identifier != None:
            self.getRequest(url + '/ems/api/v5/features/identifier=' + identifier, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif externalId != None:
            self.getRequest(url + '/ems/api/v5/features/externalId=' + externalId, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def partialUpdateFeature(self, feature_json, expectedReturnCode,outParameterList, outJsonPathList,id=None,nameVersion=None,identifierNamespace =None,identifier =None,externalId =None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            self.patchRequest(url + '/ems/api/v5/features/'+id, feature_json, currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        elif nameVersion !=None:
            self.patchRequest(url + '/ems/api/v5/features/nameVersion='+nameVersion, feature_json, currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        elif identifier != None:
            self.patchRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                                             currentApiFuncName(), expectedReturnCode, outParameterList,outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/features/externalId=' + externalId, feature_json,
                                             currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        elif identifierNamespace != None:
            self.patchRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, feature_json,
                                             currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        if self.patchApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def searchFeature(self,outParameterList,outJsonPathList,expectedReturnCode,id=None, identifier=None, licenseModelName=None, licenseModelId=None, namespaceId=None,
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
        self.getRequest(url +"/ems/api/v5/features?"+ responeurl[0:-1], "", currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteFeature(self, expectedReturnCode,outParameterList=None, outJsonPathList=None, id=None, nameVersion=None,
                      identifierNamespace=None, identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/features/' + id,"", currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif nameVersion != None:
            self.deleteRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, "",currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        elif identifierNamespace != None:
            self.deleteRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace,"",
                                          currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.deleteRequest(url + '/ems/api/v5/features/identifier=' + identifier, "",currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/features/externalId=' + externalId, "",currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedReturnCode:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Feature deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceFeature(self, feature_json, expectedReturnCode, outParameterList, outJsonPathList, id=None, nameVersion=None,
                       identifierNamespace=None, identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/features/' + id, feature_json, currentApiFuncName(),
                                       expectedReturnCode,outParameterList, outJsonPathList)
        elif nameVersion != None:
            self.putRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, feature_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.putRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/features/externalId=' + externalId, feature_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif identifierNamespace != None:
            self.putRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace,
                                       feature_json, currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        if self.putApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self







