import json
import requests
from jsonpath_ng.ext import parse
import Constant
import logging

class CustomerFactory:
    def addCustomer(self, customerJsonPath, customerNameGenerator, contact_id):
        customerFile = open(customerJsonPath, 'r')
        customerFileData = customerFile.read()
        customer_json_object = json.loads(customerFileData)
        customerFile.close()
        customerName = customerNameGenerator + self.Upper_Lower_string(9)
        customer_json_object["customer"]["name"] = customerName
        customer_json_object["customer"]["identifier"] = customerName
        customer_json_object["customer"]["contacts"]["contact"][0]["id"] = contact_id
        customerFile = open(customerJsonPath, "w")
        json.dump(customer_json_object, customerFile)
        customerFile.close()
        customerFile = open(customerJsonPath, 'r')
        customerUpdate_json = customerFile.read()
        responseCustomer = requests.post(url + '/ems/api/v5/customers', customerUpdate_json, auth=(username, password))
        responseTextCustomer = json.loads(responseCustomer.text)
        customer_name = responseTextCustomer["customer"]["name"]
        customer_id = responseTextCustomer["customer"]["id"]
        self.customerProperties = [customer_name, customer_id]
        return self


    def getContactProperties(self):
        return self.customerProperties