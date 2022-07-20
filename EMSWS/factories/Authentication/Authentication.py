import json
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
from requests.structures import CaseInsensitiveDict

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class AuthenticationFactory(object):

    def get_idp_configuration(self, expected_return_code, out_parameter_list, out_json_path_list):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        self.ems_api_request_wrapper("GET", url + '/token/api/v5/idpConfigurations', "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self



    def get_key_clock_token(self, user, password, expected_return_code, out_parameter_list=None,
                            out_json_path_list=None,output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        current_api_name=api_name()
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.get_idp_configuration(ErrorCode.HTTP200, ["realm", "tokenEndpoint", "clientId"],
                                   ["$..realm", "$..tokenEndpoint", "$..clientId"])
        data = {"grant_type": Constant.grant_type, "username": user, "password": password,
                "client_id": self.out_param_List["clientId"]}
        request_url = self.out_param_List["tokenEndpoint"].split("/auth/")[0] + "/auth/realms/" \
                      + self.out_param_List["realm"] + "/protocol/openid-connect/token"
        self.ems_api_auth_request_wrapper("POST", request_url, data, headers, current_api_name, user, password,
                                          expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter)
        return self

    def add_registration_token_without_customer(self, reg_token_xml_json_path, keyClockToken, identifier, refId1, refId2,
                                                count,
                                                expected_return_code, out_parameter_list=None,
                                                out_json_xml_path_list=None,
                                                output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        request_url = Constant.EMSURL + "/token/api/v5/registrationTokens"
        if self.isXmlFile(self.getModulePath() + reg_token_xml_json_path):
            self.updateXMLFile(reg_token_xml_json_path,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, refId1, refId2, count])

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "admin", "142E!LmT",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + reg_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(reg_token_xml_json_path,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, refId1, refId2, count])
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,output_res_xml_parameter)

        return self

    def add_reg_token_without_customer(self, reg_token_xml_json_path, key_clock_token, count, expected_return_code,
                                       out_parameter_list=None,
                                       out_json_xml_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        identifier = "regToken" + self.RandomString(8)
        ref_id1 = "regTokenrefId1" + self.RandomString(8)
        ref_id2 = "regTokenrefId2" + self.RandomString(8)
        request_url = Constant.EMSURL + "/token/api/v5/registrationTokens"
        if self.isXmlFile(self.getModulePath() + reg_token_xml_json_path):
            self.updateXMLFile(reg_token_xml_json_path,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, ref_id1, ref_id2, count])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = f'Bearer {key_clock_token}'
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            LOGGER.info(self.xmlstroutput)
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + reg_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            self.UpdateJsonFile(reg_token_xml_json_path,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, ref_id1, ref_id2, count])
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,output_res_xml_parameter)

        return self

    def add_registration_token_with_customer(self, reg_token_xml_json_path, key_clock_token, customer_name, identifier,
                                             ref_id1,
                                             ref_id2, count, expected_return_code, out_parameter_list=None,
                                             out_json_xml_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        request_url = Constant.EMSURL + "/token/api/v5/registrationTokens"
        if self.isXmlFile(self.getModulePath() + reg_token_xml_json_path):
            self.updateXMLFile(reg_token_xml_json_path,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customer_name, identifier, identifier, ref_id1, ref_id2, count])
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + key_clock_token
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + reg_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            self.UpdateJsonFile(reg_token_xml_json_path,
                                ['$..name', '$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customer_name, identifier, ref_id1, ref_id2, count])
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)

        return self

    def add_reg_token_with_customer(self, reg_token_xml_json_path, key_clock_token, customer_name, count,
                                    expected_return_code,
                                    out_parameter_list=None, out_json_xml_path_list=None,
                                    output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        identifier = "regCustToken" + self.RandomString(8)
        ref_id1 = "regCustTokenrefId1" + self.RandomString(8)
        ref_id2 = "regCustTokenrefId2" + self.RandomString(8)
        request_url = Constant.EMSURL + "/token/api/v5/registrationTokens"
        if self.isXmlFile(self.getModulePath() + reg_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + key_clock_token

            self.updateXMLFile(reg_token_xml_json_path,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customer_name, identifier, identifier, ref_id1, ref_id2, count])

            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + reg_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            self.UpdateJsonFile(reg_token_xml_json_path,
                                ['$..name', '$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customer_name, identifier, ref_id1, ref_id2, count])
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)

        return self

    def add_registration_token_json(self, reg_token_xml_json, key_clock_token, expected_return_code,
                                    out_parameter_list=None, out_json_xml_path_list=None,
                                    output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        headers = CaseInsensitiveDict()
        request_url = Constant.EMSURL + "/token/api/v5/registrationTokens"

        if self.isXml(reg_token_xml_json):
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + key_clock_token
            self.ems_api_auth_request_wrapper("POST", request_url, reg_token_xml_json, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJson(reg_token_xml_json):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            self.ems_api_auth_request_wrapper("POST", request_url, reg_token_xml_json, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)

        return self

    def add_access_token_json_xml_path(self, access_token_xml_json_path, registration_token, identifier, fqdn, refId1, refId2,
                         expected_return_code,
                         out_parameter_list=None, out_json_xml_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        request_url = Constant.EMSURL + "/token/api/v5/authTokens"
        if self.isXmlFile(self.getModulePath() + access_token_xml_json_path):
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registration_token

            self.updateXMLFile(access_token_xml_json_path,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, refId1, refId2, fqdn], ["acessTokenupdatedXml"], [self.xmlstroutput])
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + access_token_xml_json_path):
            self.UpdateJsonFile(access_token_xml_json_path,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, refId1, refId2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registration_token
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)

        return self

    def add_acc_token_json_xml_path(self, access_token_xml_json_path, registration_token, expected_return_code,
                      out_parameter_list=None, out_json_xml_path_list=None,
                      output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        request_url = Constant.EMSURL + "/token/api/v5/authTokens"
        identifier = "regCustToken" + self.RandomString(8)
        ref_id1 = "regCustTokenrefId1" + self.RandomString(8)
        ref_id2 = "regCustTokenrefId2" + self.RandomString(8)
        fqdn = "fqdn" + self.RandomString(9)
        if self.isXmlFile(self.getModulePath() + access_token_xml_json_path):

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registration_token

            self.updateXMLFile(access_token_xml_json_path,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, ref_id1, ref_id2, fqdn])
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)
        elif self.isJsonFile(self.getModulePath() + access_token_xml_json_path):
            self.UpdateJsonFile(access_token_xml_json_path,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, ref_id1, ref_id2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registration_token
            self.ems_api_auth_request_wrapper("POST", request_url, self.UpdateJsonFileResponse, headers, api_name(), "",
                                              "",
                                              expected_return_code, out_parameter_list, out_json_xml_path_list,
                                              output_res_xml_parameter)

        return self

    def get_registration_token(self, key_clock_token, expected_return_code, out_parameter_list, out_json_xml_path_list, id=None, identifier=None,
                             ref_id1=None, ref_id2=None, token=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + key_clock_token
        request_url = ""
        if id is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens/" + id
        elif identifier is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?identifier" + identifier
        elif ref_id1 is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?refId1" + ref_id1
        elif ref_id2 is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?refId2" + ref_id2
        elif token is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?token=" + token
        self.ems_api_auth_request_wrapper("GET",request_url,"", headers, api_name(), "",
                                          "",
                                          expected_return_code, out_parameter_list, out_json_xml_path_list,
                                          output_res_xml_parameter)

        return self

    def delete_registration_token(self, key_clock_token, expected_return_code,
                                out_parameter_list=None, out_json_xml_path_list=None, id=None, identifier=None, ref_id1=None,
                                ref_id2=None, token=None, customer=None, customerId=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + key_clock_token
        request_url = ""
        if id is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens/" + id
        elif identifier is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?identifier" + identifier
        elif ref_id1 is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?refId1" + ref_id1
        elif ref_id2 is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?refId2" + ref_id2
        elif token is not None:
            request_url = Constant.EMSURL + "/token/api/v5/registrationTokens?token=" + token
        self.ems_api_auth_request_wrapper("DELETE",request_url,"", headers, api_name(), "",
                                          "",
                                          expected_return_code, out_parameter_list, out_json_xml_path_list,
                                          output_res_xml_parameter)
        return self

    def update_access_token(self, reg_token_xml_json, registration_token, expected_return_code,
                            out_parameter_list=None, out_json_xml_path_list=None, id=None,
                            output_res_xml_parameter=None):
        utility = UtilityClass()
        api_name = utility.currentApiName()
        LOGGER.info(api_name())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic " + registration_token
        request_url = ""
        if id is not None:
            request_url = url + "/token/api/v5/authTokens/" + id
        self.ems_api_auth_request_wrapper("PATCH",request_url,reg_token_xml_json, headers, api_name(), "",
                                          "",
                                          expected_return_code, out_parameter_list, out_json_xml_path_list,
                                          output_res_xml_parameter)
        return self