import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory

def test_createLeaseProduct_new(emsObjectFixture,request):
    testname = request.node.name
    ems=emsObjectFixture['ems']
    #ems=EMSFactory()
    ems\
    .searchFeature(name="SM-71440_WAubM4152WAubM",id="5330")

