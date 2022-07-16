import os
import json
import string
import logging
import random
from jsonpath_ng.ext import parse
import EMSWS.EMSConfig as Constant
import xml.etree.ElementTree as ET

from EMSWS.EmsApiWrapper import EmsApiWrapper
from EMSWS.Utilities import UtilityClass
from EMSWS.factories.Feature import FeatureFactory
from EMSWS.factories.FingerPrint import FingerPrintFactory
from EMSWS.factories.NameSpaceWithWrapper import NameSpaceFactoryWrapper
from EMSWS.factories.Product import ProductFactory
from EMSWS.factories.Contact import ContactFactory
from EMSWS.factories.Customer import CustomerFactory
from EMSWS.factories.NameSpace import NameSpaceFactory
from EMSWS.factories.ReportEngine import ReportGenerator
from EMSWS.factories.Activation import ActivationFactory
from EMSWS.factories.Entitlement import Entitlementfacory
from EMSWS.factories.RestApi import RestApiUtilityFactory
from EMSWS.factories.EMSAssertion import EMSAssertionFactory
from EMSWS.factories.LicenceModel import LicenseModelFactory
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
                 ContactFactory,CustomerFactory,Entitlementfacory,LicenseModelFactory,ReportGenerator,
                 RestApiUtilityFactory,ActivationFactory,RestApiAuthFactory,AuthenticationFactory,
                 UserManagementFactory,RoleManagementFactory,
                 AuthProxyStubFactory,RestAuthProxyStubFactory,FingerPrintFactory,NameSpaceFactoryWrapper,EmsApiWrapper):

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
