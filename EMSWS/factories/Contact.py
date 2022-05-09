import  EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ContactFactory:
    def addStandardContact(self, contactJsonPath, contactNameGenerator, emailString):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        contactname=contactNameGenerator + self.RandomString(9)
        emailStr=emailString + self.RandomString(9) + "@Thales.com"
        contactUpdated_json = self.UpdateJsonPath(contactJsonPath, ['$.contact.name', '$.contact.password',
                                                                     '$.contact.contactType','$.contact.emailId'],
                                                  [contactname,"Thales@123", "Standard",emailStr])
        LOGGER.info(contactUpdated_json)
        response = self.PostRequest(url + '/ems/api/v5/contacts', contactUpdated_json, currentApiFuncName(), 201)
        if response[1] == 201:
            customerJson = utility.convertJsontoDictinary(response[0])
            contact_name = customerJson["contact"]["name"]
            conatct_id = customerJson["contact"]["id"]
            contact_emailId = customerJson["contact"]["emailId"]
        self.contactStandardProperties = [contact_name, conatct_id, contact_emailId]
        return self

    def getContactProperties(self):
        return self.contactStandardProperties



