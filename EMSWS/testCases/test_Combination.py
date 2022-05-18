import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory




def test_createNamespace():
    ems = EMSFactory()
    ems.UpdateJsonFile(Constant.nameSpaceJsonPath,['$.namespace.name'],["nameSpaceNamegenerator" + ems.RandomString(9)],["nameSpaceRes"],['$'])\
    .addNameSpace(ems.emsVariableList["nameSpaceRes"],201)


