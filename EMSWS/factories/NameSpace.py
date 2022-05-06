import EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class NameSpacefactory():

    def addNameSpace(self, nameSpaceJsonPath, nameSpaceNamegenerator):
        #getting the name of Current Running Test cases
        utility=UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        namceSpace_json = self.UpdateJsonPath(nameSpaceJsonPath, ['$.namespace.name'], [nameSpaceNamegenerator + self.RandomString(9)])
        LOGGER.info(namceSpace_json)
        # Dictionary object for crearing NameSpace Report
        response = self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), "201")
        if response[1] == 201 or response[1] == 204 or response[1] == 200:
            nameSpaceJson=utility.convertJsontoDictinary(response[0])
            nameSpace_name = nameSpaceJson["namespace"]["name"]
            nameSpace_id = nameSpaceJson["namespace"]["id"]
            self.nameSpaceProperties = [nameSpace_name, nameSpace_id, response[0]]
            # List Object for Namespace Response
        return self

    def createNameSpace(self):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        namceSpace_json=self.UpdateJsonPath(Constant.nameSpaceJsonPath, ['$.namespace.name'], [running_testcases[0:8] + self.RandomString(9)])
        LOGGER.info(namceSpace_json)
        response = self.PostRequest(url + '/ems/api/v5/namespaces', namceSpace_json, currentApiFuncName(), "201")
        if response[1] == 201 or response[1] == 204 or response[1] == 200:
            nameSpaceJson = utility.convertJsontoDictinary(response[0])
            nameSpace_name = nameSpaceJson["namespace"]["name"]
            nameSpace_id = nameSpaceJson["namespace"]["id"]
            self.nameSpaceProperties = [nameSpace_name, nameSpace_id, response[0]]
        # List Object for Namespace Response
        return self


    def getNamespaceProps(self) -> list:
        return self.nameSpaceProperties