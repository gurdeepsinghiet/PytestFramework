from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import logging

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class RoleManagementFactory(object):

    def add_role_json_file_path(self, role_json_file_path, role_name,
                                expected_return_code, out_parameter_list=None, out_json_path_list=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(role_json_file_path, ['$.role.name'], [role_name])
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/roles', self.UpdateJsonFileResponse, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)

        return self

    def add_role_json(self, role_json, expected_return_code, out_parameter_list=None, out_json_path_list=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/roles', role_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def get_role(self, expected_return_code, out_parameter_list,
                 out_json_path_list, id=None, name=None,output_res_xml_parameter=None):

        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/roles/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/roles/name=' + name
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def search_role(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None, description=None,
                   creation_date_from=None, creation_date_to=None, page_start_index=None, page_size=None, search_pattern=None,
                   sort_by_asc=None, sort_by_desc=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if description is not None:
            request_url += "description=" + description + "&"
        if creation_date_from is not None:
            request_url += "creationDateFrom" + creation_date_from + "&"
        if creation_date_to is not None:
            request_url += "creationDateTo" + creation_date_to + "&"
        if page_start_index is not None:
            request_url += "pageStartIndex" + page_start_index + "&"
        if page_size is not None:
            request_url += "pageSize" + page_size + "&"
        if search_pattern is not None:
            request_url += "searchPattern" + search_pattern + "&"
        if sort_by_asc is not None:
            request_url += "sortByAsc" + sort_by_asc + "&"
        if sort_by_desc is not None:
            request_url += "sortByDesc" + sort_by_desc + "&"
        request_url = url + "/ems/api/v5/roles?" + request_url[0:-1]
        LOGGER.info(request_url)
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def update_role(self, role_json, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None
                    ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/roles/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/roles/name=' + name
        self.ems_api_auth_request_wrapper("PATCH", request_url, role_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def replace_role(self, role_json, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None,
                     output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/roles/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/roles/name=' + name
        self.ems_api_auth_request_wrapper("PUT", request_url, role_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def delete_role(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None, name=None
                    ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/roles/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/roles/name=' + name
        self.ems_api_auth_request_wrapper("DELETE", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self
