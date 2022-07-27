import os
import json
import string
import logging
import random
from jsonpath_ng.ext import parse
import EMSWS.EMSConfig as Constant
import xml.etree.ElementTree as ET
from EMSWS.EmsApiAuthWrapper import EmsAuthApiWrapper
from EMSWS.EmsApiWrapper import EmsApiWrapper
from EMSWS.Utilities import UtilityClass
from EMSWS.factories.CustomerAttribute import CustomerAttributeFactory
from EMSWS.factories.EMSProperties import EmsPropertiesFactory
from EMSWS.factories.Feature import FeatureFactory
from EMSWS.factories.FingerPrint import FingerPrintFactory
from EMSWS.factories.Product import ProductFactory
from EMSWS.factories.Contact import ContactFactory
from EMSWS.factories.Customer import CustomerFactory
from EMSWS.factories.NameSpace import NameSpaceFactory
from EMSWS.factories.ReportEngine import ReportGenerator
from EMSWS.factories.Activation import ActivationFactory
from EMSWS.factories.Entitlement import EntitlementFacory
from EMSWS.factories.RestApi import RestApiUtilityFactory
from EMSWS.factories.EMSAssertion import EMSAssertionFactory
from EMSWS.factories.LicenceModel import LicenseModelFactory
from EMSWS.factories.SCC import SCCFactory
from EMSWS.factories.UserManagement import UserManagementFactory
from EMSWS.factories.RoleManagement import RoleManagementFactory
from EMSWS.factories.Authentication.AuthRestApi import RestApiAuthFactory
from EMSWS.factories.AuthProxyStub.authproxystub import AuthProxyStubFactory
from EMSWS.factories.Authentication.Authentication import AuthenticationFactory
from EMSWS.factories.AuthProxyStub.authproxystubapi import RestAuthProxyStubFactory

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class EMSFactory(EMSAssertionFactory,NameSpaceFactory,FeatureFactory,ProductFactory,
                 ContactFactory,CustomerFactory,EntitlementFacory,LicenseModelFactory,ReportGenerator,
                 RestApiUtilityFactory,ActivationFactory,RestApiAuthFactory,AuthenticationFactory,
                 UserManagementFactory,RoleManagementFactory,
                 AuthProxyStubFactory,RestAuthProxyStubFactory,FingerPrintFactory,CustomerAttributeFactory,
                 EmsApiWrapper,EmsAuthApiWrapper,EmsPropertiesFactory,SCCFactory):

    def __init__(self):
        self.report_data=[]
        self.out_param_List={}
    @staticmethod
    def RandomString(length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result

    def retriveFingerPrint(self,fpXmlFileName):
        u=UtilityClass()
        filename=fpXmlFileName+self.RandomString(9)+".xml"
        command=self.getModulePath()+"//FingerPrintCreation//fingerPrint.exe -f "+ self.getModulePath()+Constant.emsReportPath+filename
        os.system('cmd /c '+command)
        content=u.readFile(self.getModulePath()+"\\output\\"+filename)
        u.deleteFile(self.getModulePath()+"\\output\\"+filename)
        return content

    def retrive_finger_print(self, fp_xml_file_name):
        utility = UtilityClass()
        file_name = fp_xml_file_name + self.RandomString(9) + ".xml"
        command = self.getModulePath() + "//FingerPrintCreation//fingerPrint.exe -f " + self.getModulePath() + Constant.emsReportPath + file_name
        os.system('cmd /c ' + command)
        content = utility.readFile(self.getModulePath() + "\\output\\" + file_name)
        utility.deleteFile(self.getModulePath() + "\\output\\" + file_name)
        return content

    def getJsonXpathValue(self, jsonString, jsonVarible, jsonXpath):
        json_data = json.loads(jsonString)
        jsonpath_expression = parse(jsonXpath)
        match = jsonpath_expression.find(json_data)
        self.out_param_List[jsonVarible] = match[0].value
        LOGGER.info(self.out_param_List)

    def getJsonXpathsValues(self, jsonString, jsonVaribleList, jsonXpathList):
        if (jsonVaribleList != None and jsonXpathList != None):
            for i, jsonxpath in enumerate(jsonXpathList):
                self.getJsonXpathValue(jsonString, jsonVaribleList[i], jsonXpathList[i])
        return self

    def isJson(self, jsonString):
        if jsonString == "":
            return False
        try:
            json.loads(jsonString)
        except ValueError as e:
            return False
        return True

    def isXml(self, xmlString):
        if xmlString == "":
            return False
        try:
            ET.fromstring(xmlString)
        except ET.ParseError:
            return False
        return True

    def getModulePath(self):
        path = os.path.dirname(Constant.__file__)
        return path

    def isJsonFile(self, jsonFilePath):
        with open(jsonFilePath, 'r') as f:
            data = f.read()
            try:
                json.loads(data)
            except ValueError as e:
                return False
            return True

    def isXmlFile(self, xmlFilePath):
        with open(xmlFilePath, 'r') as f:
            data = f.read()
            try:
                ET.fromstring(data)
            except ET.ParseError:
                return False
            return True

    def is_dictionary(self, str):
        if type(str) is dict:
            return True
        else:
            return False
