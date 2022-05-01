import  EMSWS.Constant as Constant
import logging
import random
import string
from EMSWS.factories.NameSpace import NameSpacefactory
from EMSWS.factories.EMSAssertion import EMSAssertionFactory
from EMSWS.factories.Feature import FeatureFactory
from EMSWS.factories.Product import  ProductFactory
from EMSWS.factories.Contact import ContactFactory
from EMSWS.factories.Entitlement import Entitlementfacory
from EMSWS.factories.LicenceModel import LicenseModelfactory
from EMSWS.factories.customHtmlFileGenerator import CustomeReportGenerator
from EMSWS.factories.RestApi import RestApiUtilityFactory
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class EMSFactory(EMSAssertionFactory,NameSpacefactory,FeatureFactory,ProductFactory,ContactFactory,Entitlementfacory,LicenseModelfactory,CustomeReportGenerator,RestApiUtilityFactory):

    def __init__(self):
        self.data=[]

    def RandomString(self,length) ->str:
        # Print the string in Lowercase
        result = ''.join(
            (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
        return result









