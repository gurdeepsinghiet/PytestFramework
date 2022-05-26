import EMSWS.Constant as Constant
import pytest
from EMSWS.factories.EMSFuntions import EMSFactory
from EMSWS.Utilities import UtilityClass
import logging

LOGGER = logging.getLogger(__name__)
#Standalone Licence Model  Entilement partial activation
@pytest.mark.parametrize("nameSpaceName, LM_name",
[("pytest" + EMSFactory.RandomString(9),"OnPremPytest" + EMSFactory.RandomString(9))])
def test_nameSpace(emsObjectFixture,nameSpaceName,LM_name):
    ems = EMSFactory()
    ems = emsObjectFixture['ems']
    u=UtilityClass()
    ems \
        .addNameSpace(Constant.nameSpaceJsonPath, nameSpaceName, 201) \
        .searchFlexibleLicenseModel() \
        .addFlexibleLicenceModelStandalone(LM_name, ems.FlexibleLicenseModelJson, 201) \
        .updateLicencezModelAttributeWithTag("RENEW_FREQUENCY", "overwriteAllowed", "false",
                                             ems.emsVariableList["LMRES"]) \
        .partialUpdateLM(u.convertDictinarytoJson(ems.Updated_LM_Json), 200, ["partialUpdateResponse"], ["$"],
                         enforcementId=ems.getEnforcementId()[0], enforcementnameVersion=None,
                         licenseModelId=ems.emsVariableList["lmId"], lmid=None, LMname=None) \
        .updateLicencezModelAttributeWithTag("DURATION", "value", "2380", ems.emsVariableList["partialUpdateResponse"]) \
        .partialUpdateLM(u.convertDictinarytoJson(ems.emsVariableList["partialUpdateResponse"]), 200,
                         ["partialUpdateResponse_updated"], ["$"],
                         enforcementId=ems.getEnforcementId()[0], enforcementnameVersion=None,
                         licenseModelId=ems.emsVariableList["lmId"], lmid=None, LMname=None) \
        .getLicenceModelAttributesTagsValues(["RENEW_FREQUENCY"],["overwriteAllowed"],["tagsValueList"],ems.emsVariableList["partialUpdateResponse"])\
        .verifyAssertions(ems.emsVariableList["tagsValueList"],
                              False)

