import pytest
import json
import os
import requests
from jsonpath_ng.ext import parse
import Constant
import logging
import random
import sys
import string
from EMSAssertion import EMSAssertionFactory
from NameSpace import NameSpacefactory
from Feature import FeatureFactory
from Product import  ProductFactory
from Contact import ContactFactory
from Entitlement import Entitlementfacory
from LicenceModel import LicenseModelfactory
from customHtmlFileGenerator import CustomeReportGenerator
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class EMSFactory(EMSAssertionFactory,NameSpacefactory,FeatureFactory,ProductFactory,ContactFactory,Entitlementfacory,LicenseModelfactory,CustomeReportGenerator):

    def __init__(self):
            self.customReportObj = CustomeReportGenerator()
            self.data=[]

    # define the function and pass the length as argument
    def Upper_Lower_string(self,length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result
    def RString(self,length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result

    def createNameSpace(self):
        run_testcases=os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        LOGGER.info(run_testcases)
        nameSpaceFile = open(Constant.nameSpaceJsonPath, 'r')
        nameSpaceFileData = nameSpaceFile.read()
        json_object = json.loads(nameSpaceFileData)
        nameSpaceFile.close()
        nameDataFrameFile = open('../EMSDataFrame/'+run_testcases+'.json', 'r')
        namespaceData = nameDataFrameFile.read()
        nameDataFrameFile.close()
        print(namespaceData)
        # loads convert json data to dictionary object
        nameSpace_dic = json.loads(namespaceData)
        nameSpaceName = nameSpace_dic["NameSpaceName"] + self.RString(9)
        json_object["namespace"]["name"] = nameSpaceName
        json_object1 = json.dumps(json_object)
        responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', json_object1, auth=(username, password))
        if responseNameSpace.status_code == 201 or responseNameSpace.status_code == 204 or responseNameSpace.status_code==200:
            response_nameSpace = json.loads(responseNameSpace.text)
            LOGGER.info(response_nameSpace)
            nameSpace_name = response_nameSpace["namespace"]["name"]
            nameSpace_id = response_nameSpace["namespace"]["id"]
            self.nameSpaceProps=[nameSpace_name , nameSpace_id ]
            assert nameSpaceName == self.nameSpaceProps[0]
        else:
            LOGGER.Error(responseNameSpace.text)
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
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        LOGGER.info(currentFuncName())
        FlexibleLicenseModelReportPorps = {}
        FlexibleLicenseModelReportPorps["Api_Name"] = currentFuncName()
        responseEnforcement = requests.get(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',
                                           auth=(username, password))
        if responseEnforcement.status_code == 201 or responseEnforcement.status_code == 204 or responseEnforcement.status_code == 200:
            response_Enforcement = json.loads(responseEnforcement.text)
            LOGGER.info(response_Enforcement)
            enforcementId = response_Enforcement["enforcement"]["id"]
            self.enforcementProps = [enforcementId]
            responseFlexibleLicenseModel = requests.get(url + '/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model',auth=(username, password))
            if responseFlexibleLicenseModel.status_code == 201 or responseFlexibleLicenseModel.status_code == 204 or responseFlexibleLicenseModel.status_code == 200:
                response_LM_json = json.loads(responseFlexibleLicenseModel.text)
                LOGGER.info(response_LM_json)
                self.FlexibleLicenseModelJson = response_LM_json
            else:
                LOGGER.error(responseFlexibleLicenseModel.text)
                pytest.fail("getting FlexibleLicenseModel is giving error failed")
        else:
            LOGGER.error(responseEnforcement.text)
            pytest.fail("getting Enforcement is giving error failed")
        return self

    def updateLicencezModelAttribute(self,LM_ATTR_Name, value, response_LM_json):
        jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value
        return self

    def getEnforcementId(self) ->list:
        return self.enforcementProps





