import EMSWS.EMSConfig as Constant
import EMSWS.JsonPath as JsonPath
import logging
from requests.structures import CaseInsensitiveDict
from EMSWS.Utilities import UtilityClass

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class FingerPrintFactory(object):

    def add_finger_print(self, expected_return_code, customer_id, out_parameter_list=None, out_json_path_list=None
                         ,output_res_xml_parameter=None):
        utility = UtilityClass()
        fp_xml = self.retrive_finger_print("testfp")
        LOGGER.info(fp_xml)
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.fingerPrintJsonPath,
                            ['$..friendlyName', '$..refId1', '$..refId2', '$..fingerprintXml'],
                            ["fp" + self.RandomString(9), "fprefId1" + self.RandomString(9),
                             "fprefId2" + self.RandomString(9), fp_xml])
        request_url=url + '/ems/api/v5/customers/' + customer_id + '/fingerprints'
        self.ems_api_auth_request_wrapper("POST", request_url,self.UpdateJsonFileResponse, "", current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)

        return self


    def associate_fingerprint_with_product_key(self,friendly_name,pk_id,registeredQuantity,expected_return_code,out_parameter_list=None, out_json_path_list=None
                         ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.productKeyFingerPrintJsonPath,
                            ['$..friendlyName','$..registeredQuantity'],
                            [friendly_name,registeredQuantity])
        request_url = url + '/ems/api/v5/productKeys/'+pk_id+'/productKeyFingerprints'
        LOGGER.info(request_url)
        self.ems_api_auth_request_wrapper("PATCH", request_url, self.UpdateJsonFileResponse, "", current_api_name(),
                                          username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self


    def get_fingerprint(self,expected_return_code,out_parameter_list, out_json_path_list,customerId=None,fingerprintId=None,friendly_name =None, customer_name=None,identifier=None,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"
        request_url = ""
        if customerId is not None and fingerprintId is not None:
            request_url = url + '/ems/api/v5/customers/'+customerId + '/fingerprints/'+fingerprintId
        elif customer_name is not None and fingerprintId is not None:
            request_url = url + '/ems/api/v5/customers/name=' + customer_name +'/fingerprints/'+fingerprintId
        elif customer_name is not None and friendly_name is not None:
            request_url = url + '/ems/api/v5/customers/name=' + customer_name +'/fingerprints/friendlyName='+friendly_name
        elif identifier is not None and friendly_name is not None:
            request_url = url + '/ems/api/v5/customers/identifier=' + identifier +'/fingerprints/friendlyName='+friendly_name
        self.ems_api_auth_request_wrapper("GET", request_url,"", headers,
                                          current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self
