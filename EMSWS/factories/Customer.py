import logging
from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword
class CustomerFactory(object):

    def addCustomerJsonFilePath(self, customerJsonPath,CustomerName,contact_id,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(customerJsonPath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],[CustomerName,CustomerName,contact_id],["custRes"],['$'])
        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, currentApiFuncName(), 201,["customerName","custGUID","customerRes"],['$.customer.name','$.customer.id','$'])
            LOGGER.info(self.emsVariableList["customerName"])
            LOGGER.info(self.emsVariableList["custGUID"])
            LOGGER.info(self.emsVariableList["customerRes"])
        elif expectedCode != None and outVariableList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        return self

    def createCustomerJson(self, customer_json, expectedCode, outVariableList=None, outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', customer_json, currentApiFuncName(), 201,
                             ["customerName", "custGUID", "customerRes"], ['$.customer.name', '$.customer.id', '$'])
            LOGGER.info(self.emsVariableList["customerName"])
            LOGGER.info(self.emsVariableList["custGUID"])
            LOGGER.info(self.emsVariableList["customerRes"])
        elif expectedCode != None and outVariableList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/customers', customer_json, currentApiFuncName(), expectedCode,
                             outVariableList, outJsonPathList)
        return self

    def partialUpdateCustomer(self, customer_json, expectedCode, outVariableList, outJsonPathList, id=None, emailId=None,
                              identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                         expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.patchRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                         currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif identifier != None:
            self.patchRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                         currentApiFuncName(), expectedCode, outVariableList,outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                         currentApiFuncName(), expectedCode, outVariableList,outJsonPathList)
        if self.patchApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def deleteCustomer(self, expectedCode,outVariableList=None, outJsonPathList=None, id=None, emailId=None, identifier=None,
                       externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/customers/' + id,"", currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.deleteRequest(url + '/ems/api/v5/customers/emailId=' + emailId,"", currentApiFuncName(),
                                          expectedCode,outVariableList, outJsonPathList)
        elif identifier != None:
            self.deleteRequest(url + '/ems/api/v5/customers/identifier=' + identifier, "",currentApiFuncName(),
                                          expectedCode,outVariableList, outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/customers/externalId=' + externalId, "",currentApiFuncName(),
                                          expectedCode,outVariableList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if(self.deleteApiresponse[0] == Constant.HTTP204):
                LOGGER.info("Customer deleted successfully")
            else:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def replaceCustomer(self, customer_json, expectedCode, outVariableList, outJsonPathList, id=None, emailId=None,
                        identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                       expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.putRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                       currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif identifier != None:
            self.putRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                       currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                       currentApiFuncName(), expectedCode,outVariableList,outJsonPathList)
        if self.putApiResponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def searchCustomer(self, expectedCode, outVariableList, outJsonPathList, id=None, name=None, identifier=None,
                       externalId=None, refId=None, crmId=None, description=None, marketGroupId=None,
                       marketGroupName=None, state=None, contactEmailId=None, contactId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responseurl = ""
        if (id != None):
            responseurl += "id=" + id + "&"
        if (name != None):
            responseurl += "name=" + name + "&"
        if identifier != None:
            responseurl += "identifier=" + identifier + "&"
        if (externalId != None):
            responseurl += "externalId=" + externalId + "&"
        if refId != None:
            responseurl += "refId=" + refId + "&"
        if (crmId != None):
            responseurl += "crmId=" + crmId + "&"
        if description != None:
            responseurl += "description=" + description + "&"
        if (marketGroupId != None):
            responseurl += "marketGroupId=" + marketGroupId + "&"
        if (marketGroupName) != None:
            responseurl += "marketGroupName=" + marketGroupName + "&"
        if (state != None):
            responseurl += "state=" + state + "&"
        if (contactEmailId) != None:
            responseurl += "contactEmailId=" + contactEmailId + "&"
        if (contactId != None):
            responseurl += "contactId=" + contactId + "&"
        LOGGER.info(url + "/ems/api/v5/customers?" + responseurl[0:-1])
        self.getRequest(url + "/ems/api/v5/customers?" + responseurl[0:-1], "", currentApiFuncName(),
                                   expectedCode, outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self


