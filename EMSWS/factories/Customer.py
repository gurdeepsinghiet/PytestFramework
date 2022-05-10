import logging
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword
class CustomerFactory:

    def addCustomer(self, customerJsonPath, customerNameGenerator, contact_id):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        customername=customerNameGenerator + self.RandomString(9)
        customerUpdate_json = self.UpdateJsonPath(customerJsonPath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],
                                                  [customername,customername,contact_id])
        LOGGER.info(customerUpdate_json)
        response = self.PostRequest(url + '/ems/api/v5/customers', customerUpdate_json, currentApiFuncName(), 201)
        if response[1] == 201:
            customerJson = utility.convertJsontoDictinary(response[0])
            customer_name = customerJson["customer"]["name"]
            customer_id = customerJson["customer"]["id"]
        self.customerProperties = [customer_name, customer_id]
        return self


    def getCustomerProperties(self):
        return self.customerProperties