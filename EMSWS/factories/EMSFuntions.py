import EMSWS.Constant as Constant
import logging
import random
import json
from jsonpath_ng.ext import parse
import string
from EMSWS.factories.NameSpace import NameSpacefactory
from EMSWS.factories.EMSAssertion import EMSAssertionFactory
from EMSWS.factories.Feature import FeatureFactory
from EMSWS.factories.Product import ProductFactory
from EMSWS.factories.Contact import ContactFactory
from EMSWS.factories.Entitlement import Entitlementfacory
from EMSWS.factories.LicenceModel import LicenseModelfactory
from EMSWS.factories.ReportEngine import ReportGenerator
from EMSWS.factories.RestApi import RestApiUtilityFactory
from EMSWS.factories.Customer import CustomerFactory
from EMSWS.factories.Activation import ActivationFactory
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class EMSFactory(EMSAssertionFactory,NameSpacefactory,FeatureFactory,ProductFactory,
                 ContactFactory,CustomerFactory,Entitlementfacory,LicenseModelfactory,ReportGenerator,
                 RestApiUtilityFactory,ActivationFactory):

    def __init__(self):
        self.data=[]
        self.emsVariableList={}
    @staticmethod
    def RandomString(length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result

    def getJsonXpathValue(self,jsonString,jsonVarible,jsonXpath):
        json_data = json.loads(jsonString)
        jsonpath_expression = parse(jsonXpath)
        match = jsonpath_expression.find(json_data)
        self.emsVariableList[jsonVarible] = match[0].value
        LOGGER.info(self.emsVariableList)


    def getJsonXpathsValues(self,jsonString,jsonVaribleList,jsonXpathList):
        if (jsonVaribleList != None and jsonXpathList != None):
            for i, jsonxpath in enumerate(jsonXpathList):
                self.getJsonXpathValue(jsonString, jsonVaribleList[i], jsonXpathList[i])
        return self





