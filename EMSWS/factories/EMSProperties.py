from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import logging
import EMSWS.JsonPath as JsonPath
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class EmsPropertiesFactory(object):

    def search_ems_properties(self, expected_return_code,out_parameter_list=None, out_json_path_list=None,id=None, key=None,
                              sub_group_name=None, enforcement_id=None, enforcement_name=None,
                              enforcement_version=None, page_start_index=None, page_size=None, search_pattern=None,
                              sort_by_asc=None, sort_by_desc=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if key is not None:
            request_url += "key=" + key + "&"
        if sub_group_name is not None:
            request_url += "subGroupName=" + sub_group_name + "&"
        if enforcement_id is not None:
            request_url += "enforcementId=" + enforcement_id + "&"
        if enforcement_name is not None:
            request_url += "enforcementName=" + enforcement_name + "&"
        if enforcement_version is not None:
            request_url += "enforcementVersion=" + enforcement_version + "&"
        if page_start_index is not None:
            request_url += "pageStartIndex=" + page_start_index + "&"
        if page_size is not None:
            request_url += "pageSize=" + page_size + "&"
        if search_pattern is not None:
            request_url += "searchPattern=" + search_pattern + "&"
        if sort_by_asc is not None:
            request_url += "sortByAsc=" + sort_by_asc + "&"
        if sort_by_desc is not None:
            request_url += "sortByDesc=" + sort_by_desc + "&"
        request_url = url + "/ems/api/v5/applicationProperties?" + request_url[0:-1]
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def get_ems_properties(self, expected_return_code, out_parameter_list=None,
                           out_json_path_list=None, id=None, key=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/applicationProperties/' + id
        elif key is not None:
            request_url = url + '/ems/api/v5/applicationProperties/key=' + key
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self


    def bulk_update_aplication_properties(self,application_property_id,application_property_value,expected_return_code, out_parameter_list=None, out_json_path_list=None,output_res_xml_parameter=None):

        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.applicationPropsJsonPath, ['$..id','$..value'], [application_property_id,application_property_value])
        LOGGER.info(self.UpdateJsonFileResponse)
        self.ems_api_auth_request_wrapper("PATCH", url + '/ems/api/v5/applicationProperties/bulk', self.UpdateJsonFileResponse, "", current_api_name(), username, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter,bearerAuth=None)
        return self
