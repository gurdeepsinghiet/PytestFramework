import EMSWS.Constant as Constant
import pytest
from EMSWS.Utilities import UtilityClass
from EMSWS.factories.EMSFuntions import EMSFactory

def test_createCustomerandConatct(emsObjectFixture):
    u = UtilityClass()
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    CustomerName = "Standardcust" + ems.RandomString(9)
    ContactName = "pytestContact" + ems.RandomString(9)
    ContactEmailId = ems.RandomString(9) + "@Thales.com"

    conatctXpath = ['$.contact.name', '$.contact.password', '$.contact.contactType', '$.contact.emailId']
    conatctXpathValues = [ContactName, "Thales@123", "Standard", ContactEmailId]
    customerXpath = ['$.customer.name', '$.customer.identifier', '$..contacts.contact[0].id']

    ems \
    .UpdateJsonFile(Constant.contactJsonPath, conatctXpath, conatctXpathValues, ["contactRes"], ['$']) \
    .createStandardContact(u.convertDictinarytoJson(ems.emsVariableList["contactRes"]), 201) \
    .UpdateJsonFile(Constant.customerJsonPath, customerXpath,[CustomerName, CustomerName, ems.emsVariableList["contact_id"]], ["custRes"], ['$']) \
    .createCustomer(u.convertDictinarytoJson(ems.emsVariableList["custRes"]), 201) \

def test_createNameSpaceHighend(emsObjectFixture):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    ems\
    .searchFlexibleLicenseModel()



@pytest.mark.parametrize("num, output",[("Ftrpytestwpwzezego","1.0"),("Ftrpytestwpwzezego","1.0")])
def test_getFeatureApi(emsObjectFixture,num,output):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    ems\
    .getFeature(nameVersion=num+":"+output)