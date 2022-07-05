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
        # Dictionary object for creating NameSpace Report
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, ["nsName", "nsID", "nameSpaceRes"],
                             ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, out_parameter_list, out_json_path_list)
        return self

    def get_namespace(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.getRequest(url + '/ems/api/v5/namespaces/' + id, "", current_api_name(), expected_return_code,
                            out_parameter_list, out_json_path_list)
        elif name is not None:
            self.getRequest(url + '/ems/api/v5/namespaces/name=' + name, "", current_api_name(), expected_return_code,
                            out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
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
        LOGGER.info(url + "/ems/api/v5/namespaces?" + request_url[0:-1])
        self.getRequest(url + "/ems/api/v5/namespaces?" + request_url[0:-1], "", current_api_name(),
                        expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def partial_update_namespace(self, name_space_json, expected_return_code, out_parameter_list, out_json_path_list,
                                 id=None,
                                 name=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.patchRequest(url + '/ems/api/v5/namespaces/' + id, name_space_json, current_api_name(),
                              expected_return_code, out_parameter_list, out_json_path_list)
        if name is not None:
            self.patchRequest(url + '/ems/api/v5/namespaces/name=' + name, name_space_json, current_api_name(),
                              expected_return_code, out_parameter_list, out_json_path_list)
        if self.patchApiResponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def delete_namespace(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                         name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/' + id, "", current_api_name(), expected_return_code,
                               out_parameter_list, out_json_path_list)
        elif name is not None:
            self.deleteRequest(url + '/ems/api/v5/namespaces/emailId=' + name, "", current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        if self.deleteApiresponse[0] == expected_return_code:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("NameSpace deleted successfully")
            else:
                for i, resvar in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def replace_namespace(self, name_space_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                          name=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.putRequest(url + '/ems/api/v5/namespaces/' + id, name_space_json, current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif name is not None:
            self.putRequest(url + '/ems/api/v5/namespaces/name=' + name, name_space_json, current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        if self.putApiResponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def add_namespace_json_file_path(self, namespace_json_file_path, namespace_name, expected_return_code,
                                     out_parameter_list=None, out_json_path_list=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(namespace_json_file_path, ['$.namespace.name'], [namespace_name])
        LOGGER.info(self.UpdateJsonFileResponse)
        # Dictionary object for crearing NameSpace Report
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, ["nsName", "nsID", "nameSpaceRes"],
                             ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/namespaces', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, out_parameter_list, out_json_path_list)
        return self

    def add_namespace_json(self, namespace_json, expected_return_code, out_parameter_list=None,
                           out_json_path_list=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namespace_json, current_api_name(), expected_return_code,
                             ["nsName", "nsID", "nameSpaceRes"], ['$.namespace.name', '$.namespace.id', '$'])
            LOGGER.info(self.out_param_List["nsName"])
            LOGGER.info(self.out_param_List["nsID"])
            LOGGER.info(self.out_param_List["nameSpaceRes"])
        if expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/namespaces', namespace_json, current_api_name(), expected_return_code,
                             out_parameter_list, out_json_path_list)
        return self
