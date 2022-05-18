import EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ActivationFactory(object):
    def addActivation(self,activationUpdated_json,expectedCode,variableList=None,xPathList=None):
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