import logging
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword
class CustomerFactory:

    def addCustomer(self, customerJsonPath,CustomerName,contact_id,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(customerJsonPath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],[CustomerName,CustomerName,contact_id],["custRes"],['$'])
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, currentApiFuncName(), 201,["customerName","custGUID","customerRes"],['$.customer.name','$.customer.id','$'])
            LOGGER.info(self.emsVariableList["customerName"])
            LOGGER.info(self.emsVariableList["custGUID"])
            LOGGER.info(self.emsVariableList["customerRes"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,variableList, xPathList)
        return self

    def createCustomer(self, customerUpdate_json, expectedCode, variableList=None, xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers', customerUpdate_json, currentApiFuncName(), 201,
                             ["customerName", "custGUID", "customerRes"], ['$.customer.name', '$.customer.id', '$'])
            LOGGER.info(self.emsVariableList["customerName"])
            LOGGER.info(self.emsVariableList["custGUID"])
            LOGGER.info(self.emsVariableList["customerRes"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/namespaces', customerUpdate_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self

    def partialUpdateCustomer(self, customer_json, expectedCode, resvariableList, resxPathList, id=None, emailId=None,
                              identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.patchRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                         expectedCode, resxPathList)
        elif emailId != None:
            response = self.patchRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                         currentApiFuncName(), expectedCode, resxPathList)
        elif identifier != None:
            response = self.patchRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                         currentApiFuncName(), expectedCode, resxPathList)
        elif externalId != None:
            response = self.patchRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                         currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def deleteCustomer(self, expectedCode, resvariableList, resxPathList, id=None, emailId=None, identifier=None,
                       externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.deleteRequest(url + '/ems/api/v5/customers/' + id, currentApiFuncName(), expectedCode,
                                          resxPathList)
        elif emailId != None:
            response = self.deleteRequest(url + '/ems/api/v5/customers/emailId=' + emailId, currentApiFuncName(),
                                          expectedCode, resxPathList)
        elif identifier != None:
            response = self.deleteRequest(url + '/ems/api/v5/customers/identifier=' + identifier, currentApiFuncName(),
                                          expectedCode, resxPathList)
        elif externalId != None:
            response = self.deleteRequest(url + '/ems/api/v5/customers/externalId=' + externalId, currentApiFuncName(),
                                          expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def replaceCustomer(self, customer_json, expectedCode, resvariableList, resxPathList, id=None, emailId=None,
                        identifier=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            response = self.putRequest(url + '/ems/api/v5/customers/' + id, customer_json, currentApiFuncName(),
                                       expectedCode, resxPathList)
        elif emailId != None:
            response = self.putRequest(url + '/ems/api/v5/customers/emailId=' + emailId, customer_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif identifier != None:
            response = self.putRequest(url + '/ems/api/v5/customers/identifier=' + identifier, customer_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif externalId != None:
            response = self.putRequest(url + '/ems/api/v5/customers/externalId=' + externalId, customer_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self


