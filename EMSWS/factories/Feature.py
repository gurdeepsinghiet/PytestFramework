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
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, currentApiFuncName(),expectedCode, variableList,xPathList)
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

    def getFeature(self,resvariableList,resxPathList,expectedCode,featureId=None,nameVersion =None,identifierNamespace=None,identifier =None,externalId =None,id=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if featureId !=None:
            self.getRequest(url + '/ems/api/v5/features/'+featureId, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        elif id !=None:
            self.getRequest(url + '/ems/api/v5/features/' + id, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        elif nameVersion !=None:
            self.getRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        elif identifierNamespace != None:
            self.getRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        elif identifier != None:
            self.getRequest(url + '/ems/api/v5/features/identifier=' + identifier, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        elif externalId != None:
            self.getRequest(url + '/ems/api/v5/features/externalId=' + externalId, "", currentApiFuncName(),expectedCode,resvariableList,resxPathList)
        if self.getApiresponse[1] == expectedCode:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def partialUpdateFeature(self, feature_json, expectedCode,resvariableList, resxPathList,id=None,nameVersion=None,identifierNamespace =None,identifier =None,externalId =None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            self.patchRequest(url + '/ems/api/v5/features/'+id, feature_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif nameVersion !=None:
            self.patchRequest(url + '/ems/api/v5/features/nameVersion='+nameVersion, feature_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif identifier != None:
            self.patchRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                                             currentApiFuncName(), expectedCode, resvariableList,resxPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/features/externalId=' + externalId, feature_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif identifierNamespace != None:
            self.patchRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace, feature_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.patchApiresponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def searchFeature(self,resvariableList,resxPathList,expectedCode,id=None, identifier=None, licenseModelName=None, licenseModelId=None, namespaceId=None,
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
        self.getRequest(url +"/ems/api/v5/features?"+ responeurl[0:-1], "", currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def deleteFeature(self, expectedCode, resvariableList, resxPathList, id=None, nameVersion=None,
                      identifierNamespace=None, identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.deleteRequest(url + '/ems/api/v5/features/' + id, currentApiFuncName(), expectedCode,
                                          resxPathList)
        elif nameVersion != None:
            response = self.deleteRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, currentApiFuncName(),
                                          expectedCode, resxPathList)
        elif identifierNamespace != None:
            response = self.deleteRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace,
                                          currentApiFuncName(), expectedCode, resxPathList)
        elif identifier != None:
            response = self.deleteRequest(url + '/ems/api/v5/features/identifier=' + identifier, currentApiFuncName(),
                                          expectedCode, resxPathList)
        elif externalId != None:
            response = self.deleteRequest(url + '/ems/api/v5/features/externalId=' + externalId, currentApiFuncName(),
                                          expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def replaceFeature(self, feature_json, expectedCode, resvariableList, resxPathList, id=None, nameVersion=None,
                       identifierNamespace=None, identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.putRequest(url + '/ems/api/v5/features/' + id, feature_json, currentApiFuncName(),
                                       expectedCode, resxPathList)
        elif nameVersion != None:
            response = self.putRequest(url + '/ems/api/v5/features/nameVersion=' + nameVersion, feature_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif identifier != None:
            response = self.putRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif externalId != None:
            response = self.putRequest(url + '/ems/api/v5/features/externalId=' + externalId, feature_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif identifierNamespace != None:
            response = self.putRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifierNamespace,
                                       feature_json, currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self







