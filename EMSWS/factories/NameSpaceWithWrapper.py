import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
from EMSWS.Utilities import UtilityClass
from EMSWS.EmsApiWrapper import  EmsApiWrapper
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class NameSpaceFactoryWrapper(object):

    def add_namespace_wrap(self,expected_return_code,out_parameter_list, out_json_path_list):
        eaw=EmsApiWrapper()
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        self.UpdateJsonFile(JsonPath.nameSpaceJsonPath, ['$.namespace.name'], ["emsNameSpace" + self.RandomString(9)])
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces',self.UpdateJsonFileResponse,expected_return_code,
                                     current_api_name(),out_parameter_list,out_json_path_list)
        return self

    def get_namespace_wrap(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url,"", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def search_namespace_wrap(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None,
                         refId1=None,
                         refId2=None, description=None,
                         state=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
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

    def partial_update_namespace_wrap(self, name_space_json, expected_return_code, out_parameter_list=None, out_json_path_list=None,
                                 id=None,
                                 name=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        if name is not None:
            request_url=url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url, name_space_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)

        return self

    def delete_namespace_wrap(self, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                         name=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url = url + '/ems/api/v5/namespaces/emailId=' + name
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_namespace_wrap(self, name_space_json, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                          name=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=""
        if id is not None:
            request_url=url + '/ems/api/v5/namespaces/' + id
        elif name is not None:
            request_url=url + '/ems/api/v5/namespaces/name=' + name
        self.ems_api_request_wrapper(request_url, name_space_json, expected_return_code,
                                    current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_namespace_json_file_path_wrap(self, namespace_json_file_path, namespace_name, expected_return_code,
                                     out_parameter_list=None, out_json_path_list=None):

        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        self.UpdateJsonFile(namespace_json_file_path, ['$.namespace.name'], [namespace_name])
        LOGGER.info(self.UpdateJsonFileResponse)
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces',self.UpdateJsonFileResponse,expected_return_code,
                                     current_api_name(),out_parameter_list,out_json_path_list)
        return self

    def add_namespace_json_wrap(self, namespace_json, expected_return_code, out_parameter_list=None,
                           out_json_path_list=None):
        utility = UtilityClass()
        eaw = EmsApiWrapper()
        current_api_name = utility.currentApiName()
        self.ems_api_request_wrapper(url + '/ems/api/v5/namespaces',namespace_json,expected_return_code,
                                     current_api_name(),out_parameter_list,out_json_path_list)
        return self
