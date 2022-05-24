import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass
import logging

LOGGER = logging.getLogger(__name__)
#Standalone Licence Model  Entilement partial activation
@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"OnPremPytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_nameSpace(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    ems = EMSFactory()
    ems.addNameSpace(Constant.nameSpaceJsonPath,nameSpaceName,201,["GsNS","GSNSRes","GSNSId","nsState"],["$..name","$","$..id","$..state"])\
    .searchFlexibleLicenseModel()\
    .addOnPremiseLMNetwork(LM_name, ems.FlexibleLicenseModelJson, 201,["LMIDGS1"],["$.licenseModel.id"])\
    .addOnPremiseLMNetwork("pppp"+ems.RandomString(9), ems.FlexibleLicenseModelJson, 201,["LMIDGS2"],["$.licenseModel.id"])\


