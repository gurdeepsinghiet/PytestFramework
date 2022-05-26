import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass


@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_onpremLM(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    ems = emsObjectFixture['ems']
    u = UtilityClass()
    ems = EMSFactory()
    ems\
    .addNameSpace(Constant.nameSpaceJsonPath,nameSpaceName,201)\
    .searchFlexibleLicenseModel()\


