import functionsEMSWS
import Constant
from EMSFuntions import EMSFactory


def test_createLeaseProduct(request):
    testname = request.node.name
    ems = EMSFactory()
    ems\
    .addNameSpace(Constant.nameSpaceJsonPath,"namespace")\
    .searchFlexibleLicenseModel()\
    .addFlexibleLicenceModelStandalone("LMnamepytest",ems.FlexibleLicenseModelJson)\
    .addFeature("Ftrpytest",Constant.featureJsonPath,ems.getLMStandProperties()[0],ems.getNamespaceProps()[0])\
    .addProductNonLVH(Constant.productJsonPath,"pytestprod",ems.getNamespaceProps()[0],ems.getFeatureProperties()[0],ems.getFeatureProperties()[1])\
    .getAssertions(ems.getProductProperties()[2], ems.getFeatureProperties()[0])\
    .getAssertions(ems.getProductProperties()[3], "ems.getFeatureProperties()[1]")\
    .getAssertions(testname,"test_createLeaseProduct")\

def test_createNameSpaceLDK():
    ems = EMSFactory()
    ems\
    .createNameSpace()


def test_createNameSpaceHighend():
    ems = EMSFactory()
    ems\
    .createNameSpace()


    

