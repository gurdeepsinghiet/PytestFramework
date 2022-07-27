import sys
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import pytest
from EMSWS.factories.EMS import EMSFactory
from EMSWS.Utilities import UtilityClass
import EMSWS.JsonPath as JsonPath
import EMSWS.XmlPath as XmlPath
import logging
LOGGER = logging.getLogger(__name__)


@pytest.mark.Unittest
def test_LmNetwork_LeasePerformance(reportFixture):
    ems = reportFixture['ems']
    #ems= EMSFactory()
    utility = UtilityClass()
    ems \
        .get_ems_properties(ErrorCode.HTTP200, key="automaticallyCheckCustomAttribute",out_parameter_list=["customPropId"],out_json_path_list=["$..id"]) \
        .get_ems_properties(ErrorCode.HTTP200, key="automaticLicenseUpdateWindow",
                            out_parameter_list=["updatewindowId"], out_json_path_list=["$..id"]) \
        .bulk_update_aplication_properties(ems.out_param_List["customPropId"],"true",ErrorCode.HTTP200) \
        .bulk_update_aplication_properties(ems.out_param_List["updatewindowId"], "0", ErrorCode.HTTP200) \
        .add_namespace(ErrorCode.HTTP201, ["nsName"], ["$..name"]) \
        .search_flexible_license_model(ErrorCode.HTTP200, ["outputCloudLmRes"], ["$"]) \
        .add_flexible_licence_model_network("networkLM" + ems.RandomString(9), ems.out_param_List["outputCloudLmRes"],
                                   ErrorCode.HTTP201, ["LM_name_Net"], ["$..name"]) \
        .add_feature(ems.out_param_List["nsName"], ems.out_param_List["LM_name_Net"], ErrorCode.HTTP201,
                     ["ftrName", "ftrVersion"], ["$..nameVersion.name", "$..nameVersion.version"]) \
        .add_product_non_lvh(ems.out_param_List["nsName"], ems.out_param_List["ftrName"], "1.0", ErrorCode.HTTP201,
                             ["productName", "productversion"],
                             ["$.product.nameVersion.name", "$.product.nameVersion.version"]) \
        .add_standard_contact_json_path(JsonPath.contactJsonPath, "contact" + ems.RandomString(9),
                                        "thales" + ems.RandomString(9) + "@ems.com", 201, ["contact_id"], ["$..id"]) \
        .add_customer_json_file_path(JsonPath.customerJsonPath, "ctr" + ems.RandomString(9),
                                     ems.out_param_List["contact_id"], 201, ["custName","cust_id"], ["$..name","$..id"]) \
        .add_entitlement_non_lvh_eaw_off_json_path(JsonPath.entitlementJsonPath, ems.out_param_List["productName"],
                                                  "1.0", ems.out_param_List["custName"], 201,["pkId"],["$..productKey[0].pkId"])\
        .add_finger_print(ErrorCode.HTTP201,ems.out_param_List["cust_id"],["fridenlyName","fp_id"],["$..friendlyName","$..id"])\
        .associate_fingerprint_with_product_key(ems.out_param_List["fridenlyName"],ems.out_param_List["pkId"],5,200) \
        .post_ems_app_reset_flag(ems.out_param_List["custName"], ems.out_param_List["fridenlyName"], "1658473447", 201)\
        .post_scc_app_reset_flag(ems.out_param_List["custName"],
                                       ems.out_param_List["fridenlyName"],"1658473447",200)\
        .get_fingerprint(ErrorCode.HTTP200,out_parameter_list=None,out_json_path_list=None,
                         customer_name=ems.out_param_List["custName"],friendly_name=ems.out_param_List["fridenlyName"],output_res_xml_parameter="fpRes")\
    .add_activation_lease(ems.out_param_List["fpRes"],XmlPath.activationLeaseXmlPath,"5",ems.out_param_List["pkId"],
                          ems.out_param_List["fridenlyName"],ErrorCode.HTTP200)

    LOGGER.info(utility.base64Ecoding(ems.out_param_List["fpRes"]))


@pytest.mark.Unittest
def test_LmStandalone_LeasePerformance(reportFixture):
    ems = reportFixture['ems']
    ems= EMSFactory()
    utility = UtilityClass()
    ems \
        .get_ems_properties(ErrorCode.HTTP200, key="automaticallyCheckCustomAttribute",out_parameter_list=["customPropId"],out_json_path_list=["$..id"]) \
        .get_ems_properties(ErrorCode.HTTP200, key="automaticLicenseUpdateWindow",
                            out_parameter_list=["updatewindowId"], out_json_path_list=["$..id"]) \
        .bulk_update_aplication_properties(ems.out_param_List["customPropId"],"true",ErrorCode.HTTP200) \
        .bulk_update_aplication_properties(ems.out_param_List["updatewindowId"], "720", ErrorCode.HTTP200) \
        .add_namespace(ErrorCode.HTTP201, ["nsName"], ["$..name"]) \
        .search_flexible_license_model(ErrorCode.HTTP200, ["outputCloudLmRes"], ["$"]) \
        .add_flexible_licence_model_standalone("standLM" + ems.RandomString(9), ems.out_param_List["outputCloudLmRes"],
                                   ErrorCode.HTTP201, ["LM_name_Net"], ["$..name"]) \
        .add_feature(ems.out_param_List["nsName"], ems.out_param_List["LM_name_Net"], ErrorCode.HTTP201,
                     ["ftrName", "ftrVersion"], ["$..nameVersion.name", "$..nameVersion.version"]) \
        .add_product_non_lvh(ems.out_param_List["nsName"], ems.out_param_List["ftrName"], "1.0", ErrorCode.HTTP201,
                             ["productName", "productversion"],
                             ["$.product.nameVersion.name", "$.product.nameVersion.version"]) \
        .add_standard_contact_json_path(JsonPath.contactJsonPath, "contact" + ems.RandomString(9),
                                        "thales" + ems.RandomString(9) + "@ems.com", 201, ["contact_id"], ["$..id"]) \
        .add_customer_json_file_path(JsonPath.customerJsonPath, "ctr" + ems.RandomString(9),
                                     ems.out_param_List["contact_id"], 201, ["custName","cust_id"], ["$..name","$..id"]) \
        .add_entitlement_non_lvh_eaw_off_json_path(JsonPath.entitlementJsonPath, ems.out_param_List["productName"],
                                                  "1.0", ems.out_param_List["custName"], 201,["pkId"],["$..productKey[0].pkId"])\
        .add_finger_print(ErrorCode.HTTP201,ems.out_param_List["cust_id"],["fridenlyName","fp_id"],["$..friendlyName","$..id"])\
        .associate_fingerprint_with_product_key(ems.out_param_List["fridenlyName"],ems.out_param_List["pkId"],5,200) \
        .post_ems_app_reset_flag(ems.out_param_List["custName"], ems.out_param_List["fridenlyName"], "1658473447", 201)\
        .post_scc_app_reset_flag(ems.out_param_List["custName"],
                                       ems.out_param_List["fridenlyName"],"1658473447",200)\
        .get_fingerprint(ErrorCode.HTTP200,out_parameter_list=None,out_json_path_list=None,
                         customer_name=ems.out_param_List["custName"],friendly_name=ems.out_param_List["fridenlyName"],output_res_xml_parameter="fpRes")\
    .add_activation_lease(ems.out_param_List["fpRes"],XmlPath.activationLeaseXmlPath,"5",ems.out_param_List["pkId"],
                          ems.out_param_List["fridenlyName"],ErrorCode.HTTP200)\


    LOGGER.info(utility.base64Ecoding(ems.out_param_List["fpRes"]))




  # .post_scc_app_reset_flag(ems.out_param_List["cust_id"],
  #                                ems.out_param_List["fp_id"],"1658473447",201)

@pytest.mark.regression
def test_onPremStandaloneProduct(reportFixture):
    ems = reportFixture['ems']
    #ems= EMSFactory()
    utility=UtilityClass()
    ems\
    .add_namespace_json_file_path(JsonPath.nameSpaceJsonPath,""+ems.RandomString(7),ErrorCode.HTTP201,["nsName"],["$..name"])\
    .search_flexible_license_model(ErrorCode.HTTP200,["outputCloudLmRes"],["$"])\
    .add_on_premise_lm_standalone("onpremstand"+ems.RandomString(9),ems.out_param_List["outputCloudLmRes"],ErrorCode.HTTP201,["LM_name_OnpremStand"],["$..name"])\
    .add_feature(ems.out_param_List["nsName"],ems.out_param_List["LM_name_OnpremStand"],ErrorCode.HTTP201,["ftrName","ftrVersion"],["$..nameVersion.name","$..nameVersion.version"])\
    .add_product_non_lvh(ems.out_param_List["nsName"],ems.out_param_List["ftrName"],"1.0",ErrorCode.HTTP201,["productFtrName","productFtrversion"],["$..feature.nameVersion.name","$..feature.nameVersion.version"])\
    .verify_assertions(ems.out_param_List["ftrName"],ems.out_param_List["productFtrName"]) \
    .verify_assertions(ems.out_param_List["ftrVersion"], ems.out_param_List["productFtrversion"])

import sys
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import pytest
from EMSWS.factories.EMS import EMSFactory
from EMSWS.Utilities import UtilityClass
import EMSWS.JsonPath as JsonPath
import logging
LOGGER = logging.getLogger(__name__)
import EMSWS.XmlPath as XmlPath

@pytest.mark.Unittest
def test_Ems_Custom_Property_update(reportFixture):
    ems = EMSFactory()
    ems = reportFixture['ems']
    utility = UtilityClass()
    ems \
    .get_ems_properties(ErrorCode.HTTP200,["app_prop_id","app_prop_value"],["$..id","$..value"],key="automaticallyCheckCustomAttribute")\
    .bulk_update_aplication_properties(ems.out_param_List["app_prop_id"],"true",ErrorCode.HTTP200,
                                       ["app_prop_update_id","app_prop_updated_value","appPropertyRes"],["$..id","$..value","$"])\
    .verify_json_path_values(ems.out_param_List["appPropertyRes"],["$..key","$..value"],["automaticallyCheckCustomAttribute","true"]) \
    .bulk_update_aplication_properties(ems.out_param_List["app_prop_id"], "false", ErrorCode.HTTP200,
                                           ["app_prop_update_id", "app_prop_updated_value", "appPropertyRes"],
                                           ["$..id", "$..value", "$"]) \
    .verify_json_path_values(ems.out_param_List["appPropertyRes"], ["$..key", "$..value"],
                                 ["automaticallyCheckCustomAttribute", "false"])


@pytest.mark.Unittest
def test_lease_performnace_network_custom_attr(reportFixture):
    ems = reportFixture['ems']
    #ems= EMSFactory()
    utility = UtilityClass()
    ems \
    .get_ems_properties(ErrorCode.HTTP200,["app_prop_id","app_prop_value"],["$..id","$..value"],key="automaticallyCheckCustomAttribute")\
    .bulk_update_aplication_properties(ems.out_param_List["app_prop_id"],"true",ErrorCode.HTTP200,
                                       ["app_prop_update_id","app_prop_updated_value","appPropertyRes"],["$..id","$..value","$"]) \
        .add_custom_attribute(ErrorCode.HTTP201, "productkey" + ems.RandomString(9), "PRODUCTKEY",["cust_property_id","customeAttrName"],["$..id","$..name"])\
    .verify_json_path_values(ems.out_param_List["appPropertyRes"],["$..key","$..value"],["automaticallyCheckCustomAttribute","true"]) \
        .add_namespace(ErrorCode.HTTP201, ["nsName"], ["$..name"]) \
        .search_flexible_license_model(ErrorCode.HTTP200, ["outputCloudLmRes"], ["$"]) \
        .add_flexible_licence_model_network("networkLM" + ems.RandomString(9), ems.out_param_List["outputCloudLmRes"],
                                   ErrorCode.HTTP201, ["LM_name_Net"], ["$..name"]) \
        .add_feature(ems.out_param_List["nsName"], ems.out_param_List["LM_name_Net"], ErrorCode.HTTP201,
                     ["ftrName", "ftrVersion"], ["$..nameVersion.name", "$..nameVersion.version"]) \
        .add_product_non_lvh(ems.out_param_List["nsName"], ems.out_param_List["ftrName"], "1.0", ErrorCode.HTTP201,
                             ["productName", "productversion"],
                             ["$.product.nameVersion.name", "$.product.nameVersion.version"]) \
        .add_standard_contact_json_path(JsonPath.contactJsonPath, "contact" + ems.RandomString(9),
                                        "thales" + ems.RandomString(9) + "@ems.com", 201, ["contact_id"], ["$..id"]) \
        .add_customer_json_file_path(JsonPath.customerJsonPath, "ctr" + ems.RandomString(9),
                                     ems.out_param_List["contact_id"], 201, ["custName","cust_id"], ["$..name","$..id"]) \
        .add_entitlement_non_lvh_eaw_off_json_path(JsonPath.entitlementJsonPath, ems.out_param_List["productName"],
                                                  "1.0", ems.out_param_List["custName"], 201,["pkId","eId"],["$..productKey[0].pkId","$..eId"])\
        .add_finger_print(ErrorCode.HTTP201,ems.out_param_List["cust_id"],["fridenlyName","fp_id"],["$..friendlyName","$..id"])\
        .associate_fingerprint_with_product_key(ems.out_param_List["fridenlyName"],ems.out_param_List["pkId"],1,200) \
        .post_ems_app_reset_flag(ems.out_param_List["custName"], ems.out_param_List["fridenlyName"], "1658473447", 201)\
        .post_scc_app_reset_flag(ems.out_param_List["custName"],
                                       ems.out_param_List["fridenlyName"],"1658473447",200)\
        .get_entitlement(ErrorCode.HTTP200,["entRes"],["$"],e_id=ems.out_param_List["eId"]) \
        .UpdateJson(ems.out_param_List["entRes"],["$..customAttribute[?(@.name=='"+ems.out_param_List['customeAttrName']+"')].value"],
                    ["customeprodKey"+ems.RandomString(9)],["updatesEnt"],["$"])\
        .partial_update_entitlement(utility.convertDictinarytoJson(ems.out_param_List["updatesEnt"]),
                                    ErrorCode.HTTP200,["updatedEnt1","updatedCustAttr"],["$","$..customAttribute[?(@.name=='"+ems.out_param_List['customeAttrName']+"')].value"],e_id=ems.out_param_List["eId"])\
        .get_fingerprint(ErrorCode.HTTP200, out_parameter_list=None, out_json_path_list=None,
                         customer_name=ems.out_param_List["custName"], friendly_name=ems.out_param_List["fridenlyName"],
                         output_res_xml_parameter="fpRes")\
        .add_activation_lease(ems.out_param_List["fpRes"], XmlPath.activationLeaseXmlPath, "5",
                              ems.out_param_List["pkId"],
                              ems.out_param_List["fridenlyName"], ErrorCode.HTTP200)\
        .verify_json_path_values(ems.out_param_List["updatedEnt1"],["$..customAttribute[?(@.name=='"+ems.out_param_List['customeAttrName']+"')].value"],[ems.out_param_List["updatedCustAttr"]])














