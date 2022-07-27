import logging
from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
import EMSWS.JsonPath as JsonPath
username = Constant.EMSUserName
password = Constant.EMSPassword


class CustomerAttributeFactory(object):
    def add_custom_attribute(self, expected_return_code, custom_att_name,entity_type,out_parameter_list=None, out_json_path_list=None,
                      output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.customAttributeJsonPath, ['$.customAttribute.name','$.customAttribute.entityType'], [custom_att_name,entity_type])
        LOGGER.info(self.UpdateJsonFileResponse)
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/customAttributes', self.UpdateJsonFileResponse, "",
                                          current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def get_namespace(self, out_parameter_list, out_json_path_list, expected_return_code, id=None,
                      output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/customAttributes/' + id
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self


    def partial_update_namespace(self, custom_attr_json, expected_return_code, out_parameter_list, out_json_path_list,
                                 id=None,
                                 return_resource=None,output_res_xml_parameter=None):

        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/namespaces/' + id
        if return_resource is not None:
            request_url = url + '/ems/api/v5/namespaces/returnResource=' + return_resource
        self.ems_api_auth_request_wrapper("PATCH", request_url,custom_attr_json, "",
                                          current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def delete_custom_attribute(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None
                                , output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/customAttributes/' + id
        self.ems_api_auth_request_wrapper("DELETE", request_url, "", "",
                                          current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

