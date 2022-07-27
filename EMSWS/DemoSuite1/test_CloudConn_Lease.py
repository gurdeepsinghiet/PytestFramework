import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import pytest
from EMSWS.factories.EMS import EMSFactory
from EMSWS.Utilities import UtilityClass
import EMSWS.JsonPath as JsonPath
import logging

from EMSWS.factories.SCC import SCCFactory

LOGGER = logging.getLogger(__name__)

@pytest.mark.sanity
def test_cloudConnectedProduct(reportFixture):
    ems = reportFixture['ems']
    #ems= EMSFactory()
    utility = UtilityClass()
    ems\
    .add_namespace(ErrorCode.HTTP201,["nsName"],["$..name"])\
    .search_cloud_connected_licence_model(ErrorCode.HTTP200,["outputCloudLmRes"],["$"])\
    .add_cloud_connected_licence_model("demoLM"+ems.RandomString(9),ems.out_param_List["outputCloudLmRes"],ErrorCode.HTTP201,["LM_name"],["$..name"])\
    .add_feature(ems.out_param_List["nsName"],ems.out_param_List["LM_name"],ErrorCode.HTTP201,["ftrName","ftrVersion"],["$..nameVersion.name","$..nameVersion.version"])\
    .add_product_non_lvh(ems.out_param_List["nsName"],ems.out_param_List["ftrName"],"1.0",ErrorCode.HTTP201,["productFtrName","productFtrversion"],["$..feature.nameVersion.name","$..feature.nameVersion.version"])\
    .verify_assertions(ems.out_param_List["ftrName"],ems.out_param_List["productFtrName"])\
    .verify_assertions(ems.out_param_List["ftrVersion"], ems.out_param_List["productFtrversion"])

def test_token(reportFixture):
    ems = reportFixture['ems']
    utility = UtilityClass()
    ems\
    .get_key_clock_token(Constant.EMSUserName,Constant.EMSPassword,200,["accessToken"],["$..access_token"])\
    .add_registration_token_without_customer(JsonPath.regTokenJsonPathwithoutCust,ems.out_param_List["accessToken"],"test"+ems.RandomString(9),
                                             "tyu"+ems.RandomString(8),"tui"+ems.RandomString(7),4,201,["regToken"],["$..token"])\
    .add_acc_token_json_xml_path(JsonPath.accessTokenJsonPath,ems.out_param_List["regToken"],201)

def test_token1(reportFixture):
    ems = reportFixture['ems']
    ems.search_ems_properties(ErrorCode.HTTP200)\
    .get_ems_properties(ErrorCode.HTTP200, key="automaticLicenseUpdateWindow")\
    .get_scc_app_properties(ErrorCode.HTTP200, id="20b7f309-090d-11ed-9f4a-42010a0c0126")


def test_token(reportFixture):
    ems = reportFixture['ems']
    #ems= EMSFactory()
    ems\
    .add_namespace(ErrorCode.HTTP201,["id"],["$..id"])\
    .search_namespace(ErrorCode.HTTP200,["n"],["$"],id=ems.out_param_List["id"])

def test_onPremLmNetworkProduct(reportFixture):
    ems = reportFixture['ems']
    #ems = EMSFactory()
    utility = UtilityClass()
    ems \
        .add_namespace(ErrorCode.HTTP201, ["nsName"], ["$..name"]) \
        .search_flexible_license_model(ErrorCode.HTTP200, ["outputCloudLmRes"], ["$"]) \
        .add_flexible_licence_model_network("21JunetworkLM" + ems.RandomString(9),
                                            ems.out_param_List["outputCloudLmRes"],
                                            ErrorCode.HTTP201, ["LM_name_onPrem_Net", "LMResNetwrk"], ["$..name", "$"]) \
        .get_licence_model_attribute_tag_value("RENEW_FREQUENCY", "value", "getRenewTagRes",
                                               ems.out_param_List["LMResNetwrk"]) \
        .verify_assertions("2147483647", ems.out_param_List["getRenewTagRes"]) \
        .update_licence_model_attributes_by_tags(["RENEW_FREQUENCY"], ["value"], ["1"],
                                                 ems.out_param_List["LMResNetwrk"]) \
        .partial_update_lm(utility.convertDictinarytoJson(ems.Updated_LM_Json), ErrorCode.HTTP200, ["updatedRes"],
                           ["$"])
