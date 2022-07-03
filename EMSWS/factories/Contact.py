import EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ContactFactory:
    def addStandardContactJsonPath(self,contactJsonFilepath,ContactName,ContactEmailId,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(contactJsonFilepath, ['$.contact.name', '$.contact.password','$.contact.contactType','$.contact.emailId'],[ContactName,"Thales@123", "Standard",ContactEmailId])
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.out_param_List["contact_name"])
            LOGGER.info(self.out_param_List["contact_id"])
            LOGGER.info(self.out_param_List["contact_emailId"])
            LOGGER.info(self.out_param_List["contactRes"])
        elif expectedCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        return self

    def addStandardContactJson(self,contactUpdated_json,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), 201,["contact_name","contact_id" ,"contact_emailId","contactRes"],['$.contact.name','$.contact.id','contact.emailId','$'])
            LOGGER.info(self.out_param_List["contact_name"])
            LOGGER.info(self.out_param_List["contact_id"])
            LOGGER.info(self.out_param_List["contact_emailId"])
            LOGGER.info(self.out_param_List["contactRes"])
        elif expectedCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        return self

    def getContact(self, expectedCode, outParameterList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.getRequest(url + '/ems/api/v5/contacts/' + id, "", currentApiFuncName(), expectedCode,
                                       outParameterList, outJsonPathList)
        elif emailId != None:
            self.getRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, "", currentApiFuncName(),
                                       expectedCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self


    def partialUpdateContact(self, contact_json, expectedCode, outParameterList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                         expectedCode, outParameterList,outJsonPathList)
        elif emailId != None:
            self.patchRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                         currentApiFuncName(), expectedCode, outParameterList,outJsonPathList)
        if self.patchApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteContact(self, expectedCode,outParameterList=None, outJsonPathList=None, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/contacts/' + id, "", currentApiFuncName(),
                                          expectedCode,outParameterList, outJsonPathList)
        elif emailId != None:
            self.deleteRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, "",
                                          currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if(self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Contact deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])

        return self

    def replaceContact(self, contact_json, expectedCode, outParameterList, outJsonPathList, id=None, emailId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/contacts/' + id, contact_json, currentApiFuncName(),
                                       expectedCode,outParameterList, outJsonPathList)
        elif emailId != None:
            self.putRequest(url + '/ems/api/v5/contacts/emailId=' + emailId, contact_json,
                                       currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        if self.putApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def searchContact(self, expectedCode, outParameterList, outJsonPathList, id=None, name=None, refId1=None, refId2=None,
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
                                   expectedCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

