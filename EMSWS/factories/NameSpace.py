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
        if expectedCode == 201 and variableList == None and xPathList == None:
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
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), expectedCode,
                             ["nsName", "nsID", "nameSpaceRes"], ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.emsVariableList["nsName"])
            LOGGER.info(self.emsVariableList["nsID"])
            LOGGER.info(self.emsVariableList["nameSpaceRes"])
        if expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), expectedCode,variableList, xPathList)

        return self

    def partialUpdateNameSpace(self, namceSpace_json, expectedCode,id=None,name=None,variableList=None, xPathList=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            response = self.patchRequest(url + '/ems/api/v5/namespaces/'+id, namceSpace_json, currentApiFuncName(), 200,["nameSpaceUpdatedJson"],["$"])
        if name !=None:
            response = self.patchRequest(url + '/ems/api/v5/namespaces/name='+name, namceSpace_json, currentApiFuncName(), 200,["nameSpaceUpdatedJson"],["$"])
        if response[1] == expectedCode:
            LOGGER.info(self.emsVariableList["nameSpaceUpdatedJson"])
        return self


    def getNamespaceProps(self) -> list:
        return self.nameSpaceProperties