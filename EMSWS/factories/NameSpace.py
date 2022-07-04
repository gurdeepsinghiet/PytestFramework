import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class NameSpacefactory(object):

    def addNameSpace(self,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        #getting the name of Current Running Test cases
        utility=UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(JsonPath.nameSpaceJsonPath, ['$.namespace.name'],["emsNameSpace"+self.RandomString(9)])
        LOGGER.info(self.UpdateJsonFileResponse)
        # Dictionary object for creating NameSpace Report
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,["nsName","nsID","nameSpaceRes"],['$.namespace.name','$.namespace.id','$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        elif(expectedReturnCode != None and outParameterList !=None and outJsonPathList !=None):
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        return self

    def getNameSpace(self, expectedReturnCode, outParameterList, outJsonPathList, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.getRequest(url + '/ems/api/v5/namespaces/' + id, "", currentApiFuncName(), expectedReturnCode,
                            outParameterList, outJsonPathList)
        elif name != None:
            self.getRequest(url + '/ems/api/v5/namespaces/name=' + name, "", currentApiFuncName(), expectedReturnCode,
                            outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def searchNameSpace(self, expectedReturnCode, outParameterList, outJsonPathList, id=None, name=None, refId1=None,
                        refId2=None, description=None,
                        state=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responeurl = ""
        if (id != None):
            responeurl += "id=" + id + "&"
        if (name != None):
            responeurl += "name=" + name + "&"
        if (refId1 != None):
            responeurl += "licenseModelName=" + refId1 + "&"
        if (refId2 != None):
            responeurl += "licenseModelId=" + refId2 + "&"
        if (description != None):
            responeurl += "description=" + description + "&"
        if (state != None):
            responeurl += "version=" + state + "&"
        LOGGER.info(url + "/ems/api/v5/namespaces?" + responeurl[0:-1])
        self.getRequest(url + "/ems/api/v5/namespaces?" + responeurl[0:-1], "", currentApiFuncName(),
                        expectedReturnCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def partialUpdateNameSpace(self, nameSpace_json, expectedReturnCode, outParameterList, outJsonPathList, id=None,
                               name=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/namespaces/' + id, nameSpace_json, currentApiFuncName(),
                              expectedReturnCode, outParameterList, outJsonPathList)
        if name != None:
            self.patchRequest(url + '/ems/api/v5/namespaces/name=' + name, nameSpace_json, currentApiFuncName(),
                              expectedReturnCode, outParameterList, outJsonPathList)
        if self.patchApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteNameSpace(self, expectedReturnCode,outParameterList=None, outJsonPathList=None, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/' + id, "", currentApiFuncName(),expectedReturnCode,outParameterList,outJsonPathList)
        elif name != None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/emailId=' + name, "", currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        if self.deleteApiresponse[0] == expectedReturnCode:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("NameSpace deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceNameSpace(self, nameSpace_json, expectedReturnCode, outParameterList, outJsonPathList, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/namespaces/' + id, nameSpace_json, currentApiFuncName(),expectedReturnCode, outParameterList,outJsonPathList)
        elif name != None:
            self.putRequest(url + '/ems/api/v5/namespaces/name=' + name, nameSpace_json, currentApiFuncName(), expectedReturnCode, outParameterList,outJsonPathList)
        if self.putApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def addNameSpaceJsonFilePath(self,nameSpaceJsonFilePath,nameSpaceName,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        #getting the name of Current Running Test cases
        utility=UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(nameSpaceJsonFilePath, ['$.namespace.name'],[nameSpaceName])
        LOGGER.info(self.UpdateJsonFileResponse)
        # Dictionary object for crearing NameSpace Report
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,["nsName","nsID","nameSpaceRes"],['$.namespace.name','$.namespace.id','$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        elif(expectedReturnCode != None and outParameterList !=None and outJsonPathList !=None):
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        return self

    def addNameSpaceJson(self,nameSpace_json,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', nameSpace_json, currentApiFuncName(), expectedReturnCode,
                             ["nsName", "nsID", "nameSpaceRes"], ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        if expectedReturnCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', nameSpace_json, currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        return self
