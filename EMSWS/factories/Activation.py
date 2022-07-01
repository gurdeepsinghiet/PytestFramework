import EMSWS.EMSConfig as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ActivationFactory(object):
    def addActivation(self,activationJsonPathFile,expectedResponseCode,pkId,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(activationJsonPathFile, ['$..activationProductKeys.activationProductKey[0].pkId'], [pkId], ["activationRes"],
                        ['$'])
        LOGGER.info(self.UpdateJsonFileResponse)
        if expectedResponseCode == expectedResponseCode and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/activations/bulkActivate', self.UpdateJsonFileResponse, currentApiFuncName(), expectedResponseCode,
                         ["aId","activationRes"],
                         ['$.activations.activation[0].aId','$'])
            LOGGER.info(self.emsVariableList["aId"])
            LOGGER.info(self.emsVariableList["activationRes"])
        elif (expectedResponseCode != None and outVariableList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/activations/bulkActivate', self.UpdateJsonFileResponse, currentApiFuncName(), expectedResponseCode,
                             outVariableList, outJsonPathList)
        return self


    def createActivation(self,activationUpdated_json,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 200 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/activations/bulkActivate', activationUpdated_json, currentApiFuncName(), expectedCode,
                         ["aId","activationRes"],
                         ['$.activations.activation[0].aId','$'])
            LOGGER.info(self.emsVariableList["aId"])
            LOGGER.info(self.emsVariableList["activationRes"])
        elif (expectedCode != None and expectedCode != None and xPathList != None):
            self.PostRequest(url + '/ems/api/v5/activations/bulkActivate', activationUpdated_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self