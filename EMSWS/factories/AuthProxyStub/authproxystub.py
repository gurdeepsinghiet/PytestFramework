import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import logging
import requests
from EMSWS.Utilities import UtilityClass
from requests.structures import CaseInsensitiveDict

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class AuthProxyStubFactory(object):

    def post_validate_tokens_jwt_request(self, reg_token_xml_json_path, app_name, request_type, key_clock_token,
                                         identifier, ref_id1, ref_id2,
                                         count,
                                         is_enabled, expiration_date, expected_code,
                                         variable_list=None, xpath_list=None, output_xml_res_var=None):
        utility = UtilityClass()
        current_api_func_name = utility.currentApiName()
        LOGGER.info(current_api_func_name())
        request_url = "http://localhost:8080/JWTStubApp/validatetokens"
        LOGGER.info(request_url)
        if self.isXmlFile(self.getModulePath() + reg_token_xml_json_path):
            self.updateXMLFile(reg_token_xml_json_path,
                               ["./identifier", "./refId1", "./refId2", "./count", "./isEnabled", "./expirationDate"],
                               [identifier, ref_id1, ref_id2, count, is_enabled, expiration_date])

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            #request_url = Constant.EMSURL + "/" + app_name + "/validatetokens"

            if expected_code == ErrorCode.HTTP201 and variable_list is None and xpath_list is None and \
                    output_xml_res_var is not None:
                self.post_stub_request(request_url, self.xmlstroutput, headers,
                                       current_api_func_name(),
                                       expected_code, "", "", "",
                                       ["registrationtoken"], ["./token"], bearer_auth="Yes",
                                       outputXmlResVar=output_xml_res_var,is_session_based_request="None")

            elif expected_code == ErrorCode.HTTP201 and variable_list is None and xpath_list is None and \
                    output_xml_res_var is None:
                self.post_stub_request(request_url, self.xmlstroutput, headers,
                                       current_api_func_name(),
                                       expected_code, Constant.EMSUserName, Constant.EMSPassword,
                                       ["registrationtoken"], ["./token"], bearer_auth="Yes")

            elif expected_code is not None and variable_list is not None and xpath_list is not None and \
                    output_xml_res_var is not None:
                self.post_stub_request(request_url, self.xmlstroutput, headers,
                                       current_api_func_name(), expected_code, Constant.EMSUserName,
                                       Constant.EMSPassword,
                                       variable_list, xpath_list, bearer_auth="Yes", outputXmlResVar=output_xml_res_var)

            elif expected_code is not None and variable_list is not None and xpath_list is not None and \
                    output_xml_res_var is None:
                self.post_stub_request(request_url, self.xmlstroutput, headers,
                                       current_api_func_name(), expected_code, Constant.EMSUserName,
                                       Constant.EMSPassword,
                                       variable_list, xpath_list, bearer_auth="Yes")
        elif self.isJsonFile(self.getModulePath() + reg_token_xml_json_path):
            LOGGER.info('dhsdihfsdssfff')
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + key_clock_token
            self.UpdateJsonFile(reg_token_xml_json_path,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, ref_id1, ref_id2, count])
            LOGGER.info('dhsdihfsdssfff')
            if expected_code == ErrorCode.HTTP201 and variable_list is None and xpath_list is None:

                self.post_stub_request(request_url, self.UpdateJsonFileResponse, headers,
                                     current_api_func_name(), expected_code, "", "","",
                                     ["registrationRes"],
                                     ['$'], bearer_auth="Yes", is_session_based_request="None")

            elif expected_code is not None and variable_list is not None and xpath_list is not None:
                self.post_stub_request(request_url, self.UpdateJsonFileResponse, headers,
                                     current_api_func_name(), expected_code, "", "","",variable_list, xpath_list,
                                    bearer_auth="Yes", is_session_based_request="None")

        return self


    def SessionIdProxy(self,userName,Password,resvariable=None,responseTags=None):
        utility = UtilityClass()
        current_api_func_name = utility.currentApiName()
        data = {"userName": userName, "password": Password}
        #response=requests.post(url,data=data)
        response = self.PostAuthRequest(Constant.EMSURL+'/ems/api/v5/startSession', data, "",current_api_func_name(), Constant.HTTP200, "", "",resvariable,responseTags,bearerAuth="Yes")
        LOGGER.info(response)
        self

