import json
import requests
import Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ContactFactory:
    def addStandardContact(self, contactJsonPath, contactNameGenerator, emailString):
        contactFile = open(contactJsonPath, 'r')
        contactFileData = contactFile.read()
        contact_json_object = json.loads(contactFileData)
        contactFile.close()
        contact_json_object["contact"]["name"] = contactNameGenerator + self.RandomString(9)
        contact_json_object["contact"]["password"] = "Thales@123"
        contact_json_object["contact"]["contactType"] = "Standard"
        contact_json_object["contact"]["emailId"] = emailString + str(
            np.random.randint(1000000, 7000000)) + "@Thales.com"
        contactFile = open(contactJsonPath, "w")
        json.dump(contact_json_object, contactFile)
        contactFile.close()
        contactFile = open(contactJsonPath, 'r')
        contactupdated_json = contactFile.read()
        responseContact = requests.post(url + '/ems/api/v5/contacts', contactupdated_json, auth=(username, password))
        responseTextContact = json.loads(responseContact.text)
        contact_name = responseTextContact["contact"]["name"]
        conatct_id = responseTextContact["contact"]["id"]
        contact_emailId = responseTextContact["contact"]["emailId"]
        self.contactStandardProperties = [contact_name, conatct_id, contact_emailId]
        return self

    def getContactProperties(self):
        return self.contactStandardProperties



