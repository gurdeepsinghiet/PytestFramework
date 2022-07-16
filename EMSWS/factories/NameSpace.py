import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
from EMSWS.Utilities import UtilityClass

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class NameSpaceFactory(object):

    def add_namespace(self, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.nameSpaceJsonPath, ['$.namespace.name'], ["emsNameSpace" + self.RandomString(9)])
        LOGGER.info(self.UpdateJsonFileResponse)
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def get_namespace(self, out_parameter_list, out_json_path_list,expected_return_code,id=None, name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def search_namespace(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None,
                         refId1=None,
                         refId2=None, description=None,
                         state=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if refId1 is not None:
            request_url += "refId1=" + refId1 + "&"
        if refId2 is not None:
            request_url += "refId2=" + refId2 + "&"
        if description is not None:
            request_url += "description=" + description + "&"
        if state is not None:
            request_url += "version=" + state + "&"
        request_url = url + "/ems/api/v5/namespaces?" + request_url[0:-1]
        LOGGER.info(request_url)
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def partial_update_namespace(self, name_space_json, expected_return_code, out_parameter_list, out_json_path_list,
                                 id=None,
                                 name=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        if name is not None:
            request_url=url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url, name_space_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def delete_namespace(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                         name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/namespaces/emailId=' + name
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_namespace(self, name_space_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                          name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url=url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url, name_space_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_namespace_json_file_path(self, namespace_json_file_path, namespace_name, expected_return_code,
                                     out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(namespace_json_file_path, ['$.namespace.name'], [namespace_name])
        LOGGER.info(self.UpdateJsonFileResponse)
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_namespace_json(self, namespace_json, expected_return_code, out_parameter_list=None,
                           out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces',namespace_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self
