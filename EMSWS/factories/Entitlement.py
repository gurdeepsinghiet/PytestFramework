import json
from EMSWS.Utilities import UtilityClass
import requests
import  EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class Entitlementfacory(object):

    def add_entitlement_non_lvh_eaw_on_json_path(self,entitlement_json_path,product_name,product_version,
                                                 customer_name,expected_return_code,out_parameter_list=None,out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        self.UpdateJsonFile(entitlement_json_path, ['$..customer.name', '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                            '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version','$.entitlement.entitlementAsWhole'],
                            [customer_name, product_name, product_version,True], ["entitlementRes"],
                        ['$'])
        request_url = url + "/ems/api/v5/entitlements"
        self.ems_api_request_wrapper(request_url, self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_entitlement_json(self, entitlement_json, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = url + "/ems/api/v5/entitlements"
        self.ems_api_request_wrapper(request_url,entitlement_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_entitlement_non_lvh_eaw_off_json_path(self,entitlementjsonPath,product_name,product_version,customerName,expected_return_code,out_parameter_list=None,out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        self.UpdateJsonFile(self.getModulePath()+entitlementjsonPath, ['$..customer.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version',
                                                           '$.entitlement.entitlementAsWhole'],
                            [customerName, product_name, product_version, False], ["entitlementRes"],
                            ['$'])
        self.ems_api_request_wrapper(url + "/ems/api/v5/entitlements", self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def partial_update_entitlement(self,entitlement_json,expected_return_code,out_parameter_list, out_json_path_list,id=None,e_id=None,external_id=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=""
        if id != None:
            request_url=url + '/ems/api/v5/entitlements/' + id
        elif e_id != None:
            request_url=url + '/ems/api/v5/entitlements/eId=' + e_id
        elif external_id != None:
            request_url=url + '/ems/api/v5/entitlements/externalId =' + external_id
        self.ems_api_request_wrapper(request_url, entitlement_json,
                                     expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def get_entitlement(self,expected_return_code,out_parameter_list,out_json_path_list,entitlement_id=None,
                        id=None, e_id=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=""
        if entitlement_id != None:
            request_url=url + '/ems/api/v5/entitlements/' + entitlement_id
        elif id != None:
            request_url=url + '/ems/api/v5/entitlements/' + id
        elif e_id != None:
            request_url=url + '/ems/api/v5/entitlements/eId=' + e_id
        elif external_id != None:
            request_url=url + '/ems/api/v5/entitlements/externalId=' + external_id

        self.ems_api_request_wrapper(request_url, "",
                                     expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def delete_entitlement(self, expected_return_code,out_parameter_list=None, out_json_path_list=None,
                           id=None, e_id=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url=""
        if id != None:
            request_url=url + '/ems/api/v5/entitlements/' + id
        elif e_id != None:
            request_url=url + '/ems/api/v5/entitlements/eId=' + e_id
        elif external_id != None:
            request_url=url + '/ems/api/v5/entitlements/externalId =' + external_id
        self.ems_api_request_wrapper(request_url, "",
                                     expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_entitlement(self, entitlement_json, expected_return_code, out_parameter_list, out_json_path_list, id=None, eId=None,
                           externalId=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id != None:
            request_url = url + '/ems/api/v5/entitlements/' + id
        elif eId != None:
            request_url = url + '/ems/api/v5/entitlements/eId=' + eId
        elif externalId != None:
            request_url = url + '/ems/api/v5/entitlements/externalId =' + externalId
        self.ems_api_request_wrapper(request_url, entitlement_json,
                                     expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_product_key_entitlement(self,product_name, product_version, e_id, product_key_json_path,
                                    expected_return_code,out_parameter_list=None,out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        productKeyFile = open(self.getModulePath()+product_key_json_path, 'r')
        productKeyFileData = productKeyFile.read()
        productKey_json_object = json.loads(productKeyFileData)
        productKey_json_object["productKey"]["item"]["itemProduct"]["product"]["nameVersion"]["name"] = product_name
        productKey_json_object["productKey"]["item"]["itemProduct"]["product"]["nameVersion"][
            "version"] = product_version
        productKeyFile.close()
        json_object1 = json.dumps(productKey_json_object)
        request_url=url + '/ems/api/v5/entitlements/eId=' + e_id + '/productKeys'

        self.ems_api_request_wrapper(request_url, json_object1,
                                     expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)

        return self