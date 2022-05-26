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
        self.UpdateJsonFile(conatctJsonFilepath, ['$.contact.name', '$.contact.password','$.contact.contactType','$.contact.emailId'],[ContactName,"Thales@123", "Standard",ContactEmailId])
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

    def getContact(self, expectedCode, resvariableList, resxPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.getRequest(url + '/ems/api/v5/contacts/' + id, "", currentApiFuncName(), expectedCode,
                                       resvariableList, resxPathList)
        elif emailId != None:
            response = self.getRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, "", currentApiFuncName(),
                                       expectedCode, resvariableList, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self


    def partialUpdateContact(self, contact_json, expectedCode, resvariableList, resxPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.patchRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                         expectedCode, resxPathList)
        elif emailId != None:
            response = self.patchRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                         currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def deleteContact(self, feature_json, expectedCode, resvariableList, resxPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.deleteRequest(url + '/ems/api/v5/contacts/' + id, feature_json, currentApiFuncName(),
                                          expectedCode, resxPathList)
        elif emailId != None:
            response = self.deleteRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, feature_json,
                                          currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def replaceContact(self, contact_json, expectedCode, resvariableList, resxPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.putRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                       expectedCode, resxPathList)
        elif emailId != None:
            response = self.putRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def searchContact(self, expectedCode, resvariableList, resxPathList, id=None, name=None, refId1=None, refId2=None,
                      emailId=None, phoneNumber=None, state=None, customerName=None, customerId=None,
                      marketGroupId=None, marketGroupName=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responseurl = ""
        if (id != None):
            responseurl += "id=" + id + "&"
        if (name != None):
            responseurl += "name=" + name + "&"
        if (refId1 != None):
            responseurl += "refId1=" + refId1 + "&"
        if (refId2 != None):
            responseurl += "refId2=" + refId2 + "&"
        if (emailId != None):
            responseurl += "emailId=" + emailId + "&"
        if (phoneNumber != None):
            responseurl += "phoneNumber" + phoneNumber + "&"
        if (state != None):
            responseurl += "state" + state + "&"
        if (customerId != None):
            responseurl += "customerId" + customerId + "&"
        if (customerName != None):
            responseurl += "customerName" + customerName + "&"
        if (marketGroupId != None):
            responseurl += "marketGroupId" + marketGroupId + "&"
        if (marketGroupName != None):
            responseurl += "marketGroupName" + marketGroupName + "&"
        LOGGER.info(url + "/ems/api/v5/contacts?" + responseurl[0:-1])
        response = self.getRequest(url + "/ems/api/v5/contacts?" + responseurl[0:-1], "", currentApiFuncName(),
                                   expectedCode, resvariableList, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

