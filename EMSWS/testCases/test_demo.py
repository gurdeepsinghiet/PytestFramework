import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass


def test_ChangingCustomerAttrEndDateStartDate(emsObjectFixture):
    ems = EMSFactory()
    ems = emsObjectFixture['ems']
    LM_name = "pytestLMDate" + ems.RandomString(9)
    ems.searchCloudConnectedLicenceModel() \
    .updateLicencezModelAttributes(["START_DATE", "END_DATE"], ["2022-05-05 00:00", "2023-05-05 00:00"],ems.CloudConnectedLicenseModelJson) \
    .addcloudConnectedLicenceModel(LM_name, ems.Updated_LM_Json, 201)

@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_Entitlement(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    ems = EMSFactory()
    ems = emsObjectFixture['ems']
    u=UtilityClass()
    ems\
    .searchFlexibleLicenseModel() \
    .addFlexibleLicenceModelStandalone(LM_name,ems.FlexibleLicenseModelJson,201)\
    .updateLicencezModelAttributes(["RENEW_FREQUENCY", "GRACE_LIMIT"], ["34", "5"],ems.emsVariableList["LMRES"])\
    .partialUpdateLM(u.convertDictinarytoJson(ems.Updated_LM_Json),200,["parupdteRes"],["$"],lmid=ems.emsVariableList["lmId"],enforcementId=ems.getEnforcementId()[0])

#Changing LM AttriButes Cloud conncted
def test_ChangingLMATTR(emsObjectFixture):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    LM_name = "pytestLMGrace" + ems.RandomString(9)
    ems.searchCloudConnectedLicenceModel() \
        .updateLicencezModelAttributes(["USAGE_LIMIT", "GRACE_LIMIT"], ["120", "5"], ems.CloudConnectedLicenseModelJson) \
        .addcloudConnectedLicenceModel(LM_name, ems.Updated_LM_Json, 201)



#Cloud Coonected Licence Model activation Flow
@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_toverifyCloudConnected(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):

    ems = emsObjectFixture['ems']
    ContactName="pytestContact"+ems.RandomString(9)
    ContactEmailId=ems.RandomString(9) + "@Thales.com"
    u=UtilityClass()
    ems.UpdateJsonFile(Constant.nameSpaceJsonPath,['$.namespace.name'],[nameSpaceName],["nameSpaceRes"],['$'])\
    .createNameSpace(u.convertDictinarytoJson(ems.emsVariableList["nameSpaceRes"]),201)\
    .searchCloudConnectedLicenceModel()\
    .addcloudConnectedLicenceModel(LM_name,ems.CloudConnectedLicenseModelJson,201)\
    .addFeature(Constant.featureJsonPath,featureName,featureVersion,nameSpaceName,LM_name,201)\
    .addProductNonLVH(Constant.productJsonPath,ProductName,ProductVersion,nameSpaceName,featureName,featureVersion,201)\
    .addStandardContact(Constant.contactJsonPath,ContactName,ContactEmailId,201)\
    .addCustomer(Constant.customerJsonPath,CustomerName,ems.emsVariableList["contact_id"],201)\
    .addEntitlementNONLVHEAWON(Constant.entitlementJsonPath,ProductName,ProductVersion,CustomerName,201) \
    .addActivation(Constant.activationJsonPath, 200, ems.emsVariableList["pkId"]) \
    .UpdateJsonFile(Constant.partialEntitlementJsonPath,
                        ["$..eId", "$..productKeys.productKey[0].pkId", "$..product.nameVersion.name",
                         "$..product.nameVersion.version", "$..licenseModel.name",
                         "$..attribute[?(@.name=='GRACE_LIMIT')].value"],
                        [ems.emsVariableList["eid"], ems.emsVariableList["pkId"], ems.emsVariableList["product_name"],
                         "1.0", LM_name, "30"], ["updatedpartEntRes"], ["$"])
def test_first(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)


def test_second(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)

def test_second4(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output,emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*num,output)

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_12(num, output,emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*num,output)