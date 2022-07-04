import logging
from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword
class CustomerFactory(object):

    def addCustomerJsonFilePath(self, customerJsonFilePath,CustomerName,contact_id,expectedReturnCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(customerJsonFilePath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],[CustomerName,CustomerName,contact_id],["custRes"],['$'])
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,["customerName","custGUID","customerRes"],['$.customer.name','$.customer.id','$'])
            LOGGER.info(self.out_param_List["customerName"])
            LOGGER.info(self.out_param_List["custGUID"])
            LOGGER.info(self.out_param_List["customerRes"])
        elif expectedReturnCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        return self

    def addCustomerJson(self, customer_json, expectedReturnCode, outParameterList=None, outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', customer_json, currentApiFuncName(), expectedReturnCode,
                             ["customerName", "custGUID", "customerRes"], ['$.customer.name', '$.customer.id', '$'])
            LOGGER.info(self.out_param_List["customerName"])
            LOGGER.info(self.out_param_List["custGUID"])
            LOGGER.info(self.out_param_List["customerRes"])
        elif expectedReturnCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/customers', customer_json, currentApiFuncName(), expectedReturnCode,
                             outParameterList, outJsonPathList)
        return self

    def partialUpdateCustomer(self, customer_json, expectedReturnCode, outParameterList, outJsonPathList, id=None, emailId=None,
                              identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                         expectedReturnCode,outParameterList, outJsonPathList)
        elif emailId != None:
            self.patchRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                         currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.patchRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                         currentApiFuncName(), expectedReturnCode, outParameterList,outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                         currentApiFuncName(), expectedReturnCode, outParameterList,outJsonPathList)
        if self.patchApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteCustomer(self, expectedReturnCode,outParameterList=None, outJsonPathList=None, id=None, emailId=None, identifier=None,
                       externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/customers/' + id,"", currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif emailId != None:
            self.deleteRequest(url + '/ems/api/v5/customers/emailId=' + emailId,"", currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.deleteRequest(url + '/ems/api/v5/customers/identifier=' + identifier, "",currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/customers/externalId=' + externalId, "",currentApiFuncName(),
                                          expectedReturnCode,outParameterList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedReturnCode:
            if(self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Customer deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceCustomer(self, customer_json, expectedReturnCode, outParameterList, outJsonPathList, id=None, emailId=None,
                        identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                       expectedReturnCode,outParameterList, outJsonPathList)
        elif emailId != None:
            self.putRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.putRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                       currentApiFuncName(), expectedReturnCode,outParameterList,outJsonPathList)
        if self.putApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def searchCustomer(self, expectedReturnCode, outParameterList, outJsonPathList, id=None, name=None, identifier=None,
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
                                   expectedReturnCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self


