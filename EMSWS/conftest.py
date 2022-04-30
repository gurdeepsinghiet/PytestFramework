import  pytest
import os
import logging
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.factories.customHtmlFileGenerator import CustomeReportGenerator
LOGGER = logging.getLogger(__name__)
@pytest.fixture(autouse=True)
def emsObjectFixture():
    ems = EMSFactory()
    return locals()

@pytest.fixture(autouse=True)
def getReportPytestHook(emsObjectFixture):
    v=emsObjectFixture['ems']
    yield v
    v.reportGenerator()





