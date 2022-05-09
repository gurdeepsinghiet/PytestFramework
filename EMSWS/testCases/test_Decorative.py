import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
def test_createLeaseProduct(emsObjectFixture,request):
    testname = request.node.name
    ems=emsObjectFixture['ems']
    ems\
    .addNameSpace(Constant.nameSpaceJsonPath,"namespace")\
    .searchFlexibleLicenseModel()\
    .addFlexibleLicenceModelStandalone("LMnamepytest",ems.FlexibleLicenseModelJson)\
    .addFeature("Ftrpytest",Constant.featureJsonPath,ems.getLMStandProperties()[0],ems.getNamespaceProps()[0])\
    .addProductNonLVH(Constant.productJsonPath,"pytestprod",ems.getNamespaceProps()[0],ems.getFeatureProperties()[0],ems.getFeatureProperties()[1])\
    .getAssertions(ems.getProductProperties()[2], ems.getFeatureProperties()[0])\
    .getAssertions(ems.getProductProperties()[3], ems.getFeatureProperties()[0])\
    .getAssertions(testname,"test_createLeaseProduct")

def test_createNameSpaceLDK(emsObjectFixture):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    ems\
    .createNameSpace()\
    .addStandardContact(Constant.contactJsonPath,"emscontact","bnnn")\
    .addCustomer(Constant.customerJsonPath,"bnm",ems.getContactProperties()[1])

def test_createNameSpaceHighend(emsObjectFixture):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    ems\
    .searchFlexibleLicenseModel()

def test_createLeaseProduct_new(emsObjectFixture,request):
    testname = request.node.name
    ems=emsObjectFixture['ems']
    #ems=EMSFactory()
    ems\
    .addNameSpace(Constant.nameSpaceJsonPath,"namespace")\
    .searchFlexibleLicenseModel()\
    .addFlexibleLicenceModelStandalone("LMnamepytest",ems.FlexibleLicenseModelJson)\
    .addFeature("Ftrpytest",Constant.featureJsonPath,ems.getLMStandProperties()[0],ems.getNamespaceProps()[0])\
    .addProductNonLVH(Constant.productJsonPath,"pytestprod",ems.getNamespaceProps()[0],ems.getFeatureProperties()[0],ems.getFeatureProperties()[1])\
    .getAssertions(ems.getProductProperties()[2], ems.getFeatureProperties()[0])\
    .getAssertions(ems.getProductProperties()[3], ems.getFeatureProperties()[1])\
    .getAssertions(testname,"test_createLeaseProduct")

@pytest.mark.parametrize("num, output",[("Ftrpytestwpwzezego","1.0"),("Ftrpytestwpwzezego","1.0")])
def test_getFeatureApi(emsObjectFixture,num,output):
    #ems = EMSFactory()
    ems = emsObjectFixture['ems']
    ems\
    .getFeature(nameVersion=num+":"+output)