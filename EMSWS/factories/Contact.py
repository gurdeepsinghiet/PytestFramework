import EMSWS.EMSConfig as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ContactFactory:
    def addStandardContactJsonFilePath(self,contactJsonFilepath,ContactName,ContactEmailId,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(contactJsonFilepath, ['$.contact.name', '$.contact.password','$.contact.contactType','$.contact.emailId'],[ContactName,"Thales@123", "Standard",ContactEmailId])
        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.emsVariableList["contact_name"])
            LOGGER.info(self.emsVariableList["contact_id"])
            LOGGER.info(self.emsVariableList["contact_emailId"])
            LOGGER.info(self.emsVariableList["contactRes"])
        elif expectedCode != None and outVariableList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        return self

    def addStandardContactJson(self,contactUpdated_json,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.emsVariableList["contact_name"])
            LOGGER.info(self.emsVariableList["contact_id"])
            LOGGER.info(self.emsVariableList["contact_emailId"])
            LOGGER.info(self.emsVariableList["contactRes"])
        elif expectedCode != None and outVariableList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        return self

    def getContact(self, expectedCode, outVariableList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.getRequest(url + '/ems/api/v5/contacts/' + id, "", currentApiFuncName(), expectedCode,
                                       outVariableList, outJsonPathList)
        elif emailId != None:
            self.getRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, "", currentApiFuncName(),
                                       expectedCode, outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self


    def partialUpdateContact(self, contact_json, expectedCode, outVariableList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                         expectedCode, outVariableList,outJsonPathList)
        elif emailId != None:
            self.patchRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                         currentApiFuncName(), expectedCode, outVariableList,outJsonPathList)
        if self.patchApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def deleteContact(self, expectedCode,outVariableList=None, outJsonPathList=None, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/contacts/' + id, "", currentApiFuncName(),
                                          expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.deleteRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, "",
                                          currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if(self.deleteApiresponse[0] == Constant.HTTP204):
                LOGGER.info("Contact deleted successfully")
            else:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])

        return self

    def replaceContact(self, contact_json, expectedCode, outVariableList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                       expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.putRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                       currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        if self.putApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def searchContact(self, expectedCode, outVariableList, outJsonPathList, id=None, name=None, refId1=None, refId2=None,
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
        self.getRequest(url + "/ems/api/v5/contacts?" + responseurl[0:-1], "", currentApiFuncName(),
                                   expectedCode, outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

