import EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ContactFactory:
    def addStandardContact(self,conatctJsonFilepath,ContactName,ContactEmailId,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(Constant.contactJsonPath, ['$.contact.name', '$.contact.password','$.contact.contactType','$.contact.emailId'],[ContactName,"Thales@123", "Standard",ContactEmailId])
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.emsVariableList["contact_name"])
            LOGGER.info(self.emsVariableList["contact_id"])
            LOGGER.info(self.emsVariableList["contact_emailId"])
            LOGGER.info(self.emsVariableList["contactRes"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,variableList, xPathList)
        return self

    def createStandardContact(self,contactUpdated_json,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.emsVariableList["contact_name"])
            LOGGER.info(self.emsVariableList["contact_id"])
            LOGGER.info(self.emsVariableList["contact_emailId"])
            LOGGER.info(self.emsVariableList["contactRes"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', contactUpdated_json, currentApiFuncName(), expectedCode,variableList, xPathList)
        return self



