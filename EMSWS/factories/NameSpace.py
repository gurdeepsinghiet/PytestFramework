import EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class NameSpacefactory():

    def addNameSpace(self,nameSpaceJsonFilePath,nameSpaceName,expectedCode,variableList=None,xPathList=None):
        #getting the name of Current Running Test cases
        utility=UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(nameSpaceJsonFilePath, ['$.namespace.name'],[nameSpaceName])
        LOGGER.info(self.UpdateJsonFileResponse)
        # Dictionary object for crearing NameSpace Report
        if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,["nsName","nsID","nameSpaceRes"],['$.namespace.name','$.namespace.id','$'])
            LOGGER.info(self.emsVariableList["nsName"])
            LOGGER.info(self.emsVariableList["nsID"])
            LOGGER.info(self.emsVariableList["nameSpaceRes"])
        elif(expectedCode != None and expectedCode !=None and xPathList !=None):
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode, variableList, xPathList)
        return self

    def createNameSpace(self,namceSpace_json,expectedCode,variableList=None,xPathList=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), expectedCode,
                             ["nsName", "nsID", "nameSpaceRes"], ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.emsVariableList["nsName"])
            LOGGER.info(self.emsVariableList["nsID"])
            LOGGER.info(self.emsVariableList["nameSpaceRes"])
        if expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), expectedCode,variableList, xPathList)

        return self

    def partialUpdateNameSpace(self,namceSpace_json,expectedCode,resvariableList, resxPathList,id=None,name=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            self.patchRequest(url + '/ems/api/v5/namespaces/'+id, namceSpace_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if name !=None:
            self.patchRequest(url + '/ems/api/v5/namespaces/name='+name, namceSpace_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.patchApiResponse[1] == expectedCode:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def getNameSpace(self,expectedCode,resvariableList,resxPathList,id=None,name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            self.getRequest(url + '/ems/api/v5/namespaces/' + id, "", currentApiFuncName(), expectedCode, resvariableList, resxPathList)
        elif name !=None:
            self.getRequest(url + '/ems/api/v5/namespaces/name=' + name, "", currentApiFuncName(), expectedCode, resvariableList, resxPathList)
        if self.getApiresponse[1] == expectedCode:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self


    def searchNameSpace(self,expectedCode,resvariableList,resxPathList,id=None, name=None, refId1=None, refId2=None, description=None,
                      state=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responeurl=""
        if (id != None):
            responeurl +="id="+id+"&"
        if (name != None):
            responeurl +="name="+name+"&"
        if (refId1 != None):
            responeurl += "licenseModelName=" + refId1 + "&"
        if (refId2 != None):
            responeurl += "licenseModelId=" + refId2 + "&"

        if (description != None):
            responeurl += "description=" + description + "&"
        if (state != None):
            responeurl += "version=" + state + "&"
        LOGGER.info(url +"/ems/api/v5/namespaces?"+ responeurl[0:-1])
        self.getRequest(url +"/ems/api/v5/namespaces?"+ responeurl[0:-1], "", currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.getApiresponse[1] == expectedCode:
            for i,resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def deleteNameSpace(self, expectedCode,resvariableList=None, resxPathList=None, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/' + id, "", currentApiFuncName(),
                                          expectedCode,resvariableList,resxPathList)
        elif name != None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/emailId=' + name, "",
                                          currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == Constant.HTTP204):
                LOGGER.info("Contact deleted successfully")
            else:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def replaceNameSpace(self, nameSpace_json, expectedCode, resvariableList, resxPathList, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/namespaces/' + id, nameSpace_json, currentApiFuncName(),
                                       expectedCode, resxPathList)
        elif name != None:
            self.putRequest(url + '/ems/api/v5/namespaces/name=' + name, nameSpace_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        if self.putApiResponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self