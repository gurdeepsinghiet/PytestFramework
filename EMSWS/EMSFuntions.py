import pytest
import json
import numpy as np
import requests
from jsonpath_ng.ext import parse
import Constant
import logging
import random
import string
from EMSAssertion import EMSAssertionFactory
from NameSpace import NameSpacefactory
from Feature import FeatureFactory
from Product import  ProductFactory
from Contact import ContactFactory
from Entitlement import Entitlementfacory
from LicenceModel import LicenseModelfactory
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class EMSFactory(EMSAssertionFactory,NameSpacefactory,FeatureFactory,ProductFactory,ContactFactory,Entitlementfacory,LicenseModelfactory):

    # define the function and pass the length as argument
    def Upper_Lower_string(self,length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result

    def createNameSpace(self,nameSpaceJsonPath, nameSpaceNamegenerator):
        nameSpaceFile = open(nameSpaceJsonPath, 'r')
        nameSpaceFileData = nameSpaceFile.read()
        json_object = json.loads(nameSpaceFileData)
        nameSpaceFile.close()
        json_object["namespace"]["name"] = nameSpaceNamegenerator + self.Upper_Lower_string(9)
        # nameSpaceFile = open(nameSpaceJsonPath, "w")
        # json.dump(json_object, nameSpaceFile)
        # nameSpaceFile.close()
        # nameSpaceFile = open(nameSpaceJsonPath, 'r')
        # nameSpace_json1 = nameSpaceFile.read()
        json_object1 = json.dumps(json_object)
        responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', json_object1, auth=(username, password))
        response_nameSpace = json.loads(responseNameSpace.text)
        LOGGER.info(response_nameSpace)
        nameSpace_name = response_nameSpace["namespace"]["name"]
        nameSpace_id = response_nameSpace["namespace"]["id"]
        self.nameSpaceProps=[nameSpace_name , nameSpace_id ]
        return self

    def getEnforcement(self):
        responseEnforcement = requests.get(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',
                                           auth=(username, password))
        response_Enforcement = json.loads(responseEnforcement.text)
        LOGGER.info(response_Enforcement)
        enforcementId = response_Enforcement["enforcement"]["id"]
        self.enforcementProps = [enforcementId]
        return self

    def searchFlexibleLicenseModel(self):
        responseEnforcement = requests.get(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',
                                           auth=(username, password))
        response_Enforcement = json.loads(responseEnforcement.text)
        LOGGER.info(response_Enforcement)
        enforcementId = response_Enforcement["enforcement"]["id"]
        self.enforcementProps = [enforcementId]
        responseFlexibleLicenseModel = requests.get(
            url + '/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model',
            auth=(username, password))
        response_LM_json = json.loads(responseFlexibleLicenseModel.text)
        LOGGER.info(response_LM_json)
        self.FlexibleLicenseModelJson = response_LM_json
        return self

    def updateLicencezModelAttribute(self,LM_ATTR_Name, value, response_LM_json):
        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value
        return self

    def getEnforcementId(self) ->list:
        return self.enforcementProps





