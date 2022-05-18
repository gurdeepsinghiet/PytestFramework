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
        self.UpdateJsonFile(Constant.customerJsonPath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],[CustomerName,CustomerName,contact_id],["custRes"],['$'])
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


