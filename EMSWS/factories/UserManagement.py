from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import logging

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class UserManagementFactory(object):

    def add_user_json_file_path(self, user_json_file_path, login_id, user_name, user_email_id, user_password,
                                user_type, user_state, expected_return_code, out_parameter_list=None,
                                out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(user_json_file_path,
                            ["$.user.loginId", "$.user.name", "$..emailId", "$..password", "$..userType",
                             "$..userState"],
                            [login_id, user_name, user_email_id, user_password, user_type, user_state])
        self.ems_api_request_wrapper(url + '/ems/api/v5/users', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_user_json(self, user_json, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_request_wrapper(url + '/ems/api/v5/users', user_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def get_user(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, email_id=None,
                 login_id=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/users/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/users/emailid=' + email_id
        elif login_id is not None:
            request_url = url + '/ems/api/v5/users/loginId=' + login_id
        elif external_id is not None:
            request_url = url + '/ems/api/v5/users/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def search_user(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, state=None,
                    role_name=None,
                    login_id=None, name=None,
                    market_group_name=None, email_id=None, ref_id1=None, ref_id2=None, external_id=None,
                    creation_date_from=None,
                    creation_date_to=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if state is not None:
            request_url += "state=" + state + "&"
        if role_name is not None:
            request_url += "roleName=" + role_name + "&"
        if login_id is not None:
            request_url += "loginId=" + login_id + "&"
        if market_group_name is not None:
            request_url += "marketGroupName=" + market_group_name + "&"
        if email_id is not None:
            request_url += "emailId=" + email_id + "&"
        if ref_id1 is not None:
            request_url += "refId1=" + ref_id1 + "&"
        if ref_id2 is not None:
            request_url += "refId2=" + ref_id2 + "&"
        if external_id is not None:
            request_url += "externalId=" + external_id + "&"
        if creation_date_from is not None:
            request_url += "creationDateFrom=" + creation_date_from + "&"
        if creation_date_to is not None:
            request_url += "creationDateTo=" + creation_date_to + "&"
        request_url = url + "/ems/api/v5/users?" + request_url[0:-1]
        LOGGER.info(request_url)
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def update_user(self, user_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                    email_id=None,
                    login_id=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/users/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/users/emailId=' + email_id
        elif login_id is not None:
            request_url = url + '/ems/api/v5/users/loginId=' + login_id
        elif external_id is not None:
            request_url = url + '/ems/api/v5/users/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, user_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_user(self, user_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                     email_id=None,
                     login_id=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/users/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/users/emailId=' + email_id
        elif login_id is not None:
            request_url = url + '/ems/api/v5/users/loginId=' + login_id
        elif external_id is not None:
            request_url = url + '/ems/api/v5/users/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, user_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def delete_user(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                    email_id=None, login_id=None,
                    external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/users/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/users/emailId=' + email_id
        elif login_id is not None:
            request_url = url + '/ems/api/v5/users/loginId=' + login_id
        elif external_id is not None:
            request_url = url + '/ems/api/v5/users/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self
