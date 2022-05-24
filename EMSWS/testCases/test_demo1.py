import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass



#Standalone Licence Model  Entilement partial activation
@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_updateEntStand(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    ems = EMSFactory()
    ems = emsObjectFixture['ems']
    u=UtilityClass()
    ems\
    .addNameSpace(Constant.nameSpaceJsonPath,nameSpaceName,201)\
    .searchFlexibleLicenseModel() \
    .addFlexibleLicenceModelStandalone(LM_name, ems.FlexibleLicenseModelJson, 201) \
    .updateLicencezModelAttributes(["RENEW_FREQUENCY", "GRACE_LIMIT"], ["34", "5"], ems.emsVariableList["LMRES"]) \
    .partialUpdateLM(u.convertDictinarytoJson(ems.Updated_LM_Json), 200, ["parupdteRes"], ["$"],lmid=ems.emsVariableList["lmId"], enforcementId=ems.getEnforcementId()[0]) \
    .addFeature(Constant.featureJsonPath,featureName, featureVersion, ems.emsVariableList["nsName"], LM_name, 201) \
    .addProductNonLVH(Constant.productJsonPath, ProductName, ProductVersion, nameSpaceName, featureName,featureVersion, 201) \
    .addStandardContact(Constant.contactJsonPath, ContactName, ContactEmailId, 201) \
    .addCustomer(Constant.customerJsonPath, CustomerName, ems.emsVariableList["contact_id"], 201) \
    .addEntitlementNONLVHEAWOFF(Constant.entitlementJsonPath,ProductName,ProductVersion,CustomerName,201) \
    .UpdateJson(ems.emsVariableList["entRes"],["$..entitlementAsWhole","$..productKeys.productKey[0].startDate"],[True,"2022-05-20"])\
    .partialUpdateEntitlement(u.convertDictinarytoJson(ems.emsVariableList["entRes"]),200,["parUpdateEntRes"],["$"],eId=ems.emsVariableList["eid"])