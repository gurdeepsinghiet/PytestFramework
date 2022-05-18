import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass

@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_createNamespace(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    #ems = EMSFactory()
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
    .addEntitlementNONLVHEAWON(Constant.entitlementJsonPath,ProductName,ProductVersion,CustomerName,201)


@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_Entitlement(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
    #ems = EMSFactory()
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
    .addEntitlementNONLVHEAWON(Constant.entitlementJsonPath,ProductName,ProductVersion,CustomerName,201)

@pytest.mark.parametrize("nameSpaceName, LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId",
[("pytest" + EMSFactory.RandomString(9),"pytest" + EMSFactory.RandomString(9),"pytestftr" + EMSFactory.RandomString(9),"1.0",
"pytestptr" + EMSFactory.RandomString(9),"1.0","Standardcust"+EMSFactory.RandomString(9),"pytestContact"+EMSFactory.RandomString(9),EMSFactory.RandomString(9) + "@Thales.com")])
def test_createCloudLM(emsObjectFixture,nameSpaceName,LM_name,featureName,featureVersion,ProductName,ProductVersion,CustomerName,ContactName,ContactEmailId):
        #ems = EMSFactory()
        ems = emsObjectFixture['ems']

        featureXpath = ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                        '$..featureLicenseModel[0].licenseModel.name']
        featureXpathValue = [featureName, featureVersion, nameSpaceName, LM_name]
        productXpath = ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                        '$..productFeature[0].feature.nameVersion.name',
                        '$..productFeature[0].feature.nameVersion.version']
        productXpathvalues = [ProductName, ProductVersion, nameSpaceName, featureName, featureVersion]
        conatctXpath = ['$.contact.name', '$.contact.password', '$.contact.contactType', '$.contact.emailId']
        conatctXpathValues = [ContactName, "Thales@123", "Standard", ContactEmailId]
        customerXpath = ['$.customer.name', '$.customer.identifier', '$..contacts.contact[0].id']
        entiitelementXpath = ['$..customer.name',
                              '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                              '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version',
                              '$.entitlement.entitlementAsWhole']

        entiitelementXpathValues = [CustomerName, ProductName, ProductVersion, True]
        activtionXpath = ['$..activationProductKeys.activationProductKey[0].pkId']

        u = UtilityClass()

        ems.addNameSpace(Constant.nameSpaceJsonPath,nameSpaceName,201)\
            .searchCloudConnectedLicenceModel() \
            .updateLicencezModelAttributes(["USAGE_LIMIT", "GRACE_LIMIT"], ["120", "5"],ems.CloudConnectedLicenseModelJson) \
            .addcloudConnectedLicenceModel(LM_name, ems.Updated_LM_Json,201) \
            .UpdateJsonFile(Constant.featureJsonPath, featureXpath, featureXpathValue, ["featureRes"], ['$']) \
            .createFeature(u.convertDictinarytoJson(ems.emsVariableList["featureRes"]), 201) \
            .UpdateJsonFile(Constant.productJsonPath, productXpath, productXpathvalues, ["productRes"], ['$']) \
            .createProductNonLVH(u.convertDictinarytoJson(ems.emsVariableList["productRes"]), 201) \
            .UpdateJsonFile(Constant.contactJsonPath, conatctXpath, conatctXpathValues, ["contactRes"], ['$']) \
            .createStandardContact(u.convertDictinarytoJson(ems.emsVariableList["contactRes"]), 201) \
            .UpdateJsonFile(Constant.customerJsonPath, customerXpath,[CustomerName, CustomerName, ems.emsVariableList["contact_id"]], ["custRes"], ['$']) \
            .createCustomer(u.convertDictinarytoJson(ems.emsVariableList["custRes"]), 201) \
            .UpdateJsonFile(Constant.entitlementJsonPath, entiitelementXpath, entiitelementXpathValues,["entitlementRes"], ['$']) \
            .createEntitlementNONLVHEAWON(u.convertDictinarytoJson(ems.emsVariableList["entitlementRes"]), 201)\
            .UpdateJsonFile(Constant.activationJsonPath, activtionXpath,[ems.emsVariableList["pkId"]],["activationRes"], ['$'])\
            .addActivation(u.convertDictinarytoJson(ems.emsVariableList["entitlementRes"]),201)



def test_ChangingCustomerAttrEndDateStartDate(emsObjectFixture):

    ems = EMSFactory()
    ems = emsObjectFixture['ems']

    LM_name = "pytestLMDate" + ems.RandomString(9)
    ems.searchCloudConnectedLicenceModel() \
    .updateLicencezModelAttributes(["START_DATE", "END_DATE"], ["2022-05-05 00:00", "2023-05-05 00:00"], ems.CloudConnectedLicenseModelJson) \
    .addcloudConnectedLicenceModel(LM_name, ems.Updated_LM_Json, 201) \


def test_ChangingLMATTR(emsObjectFixture):

    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    LM_name = "pytestLMGrace" + ems.RandomString(9)
    ems.searchCloudConnectedLicenceModel() \
    .updateLicencezModelAttributes(["USAGE_LIMIT", "GRACE_LIMIT"], ["120", "5"], ems.CloudConnectedLicenseModelJson) \
    .addcloudConnectedLicenceModel(LM_name, ems.Updated_LM_Json, 201)