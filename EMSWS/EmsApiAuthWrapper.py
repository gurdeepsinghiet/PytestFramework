import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class EmsAuthApiWrapper(object):

    def ems_api_auth_request_wrapper(self, request_type,request_url, request_body, headers, api_name, username, password,
                                     expected_return_code,
                                     out_parameter_list, out_json_path_list, output_res_xml_parameter,bearerAuth):

        if request_type == 'POST':
            if self.is_dictionary(request_body) or self.isJson(request_body):
                self.post_auth_request(request_url,
                                       request_body,headers, api_name, username, password, expected_return_code,
                                       out_parameter_list,
                                       out_json_path_list, bearerAuth=bearerAuth)

            elif self.isXml(request_body):
                self.post_auth_request(request_url,
                                       request_body, headers, api_name, username, password, expected_return_code,
                                       out_parameter_list,
                                       out_json_path_list, bearerAuth=bearerAuth,outputXmlResVar = output_res_xml_parameter)

        elif request_type == 'GET':
            self.get_auth_request(request_url,request_body, headers, api_name, username, password,
                                  expected_return_code,out_parameter_list,out_json_path_list, bearerAuth=bearerAuth,outputXmlResVar = output_res_xml_parameter)
            if self.getAuthApiresponse[1] == expected_return_code and out_parameter_list is not None and out_json_path_list is not None:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])

        elif request_type == 'DELETE':
            self.delete_auth_request(request_url,
                                     request_body, headers, api_name, username, password, expected_return_code,
                                     out_parameter_list,
                                     out_json_path_list, bearerAuth=bearerAuth)
            if self.deleteapiAuthResponse[0] == expected_return_code:
                if self.deleteapiAuthResponse[0] == ErrorCode.HTTP204:
                    LOGGER.info("NameSpace deleted successfully")
                elif self.deleteapiAuthResponse[0] == expected_return_code and \
                        out_parameter_list is not None and out_json_path_list is not None:
                    for i, out_param in enumerate(out_parameter_list):
                        LOGGER.info(out_parameter_list[i])
                        LOGGER.info(self.out_param_List[out_parameter_list[i]])

        elif request_type == 'PATCH':
            self.patch_auth_request(request_url,
                                    request_body, headers, api_name, username, password, expected_return_code,
                                    out_parameter_list,
                                    out_json_path_list, bearerAuth=bearerAuth)
            if self.patchAuthApiResponse[1] is expected_return_code and out_parameter_list is not None \
                    and out_json_path_list is not None and output_res_xml_parameter is None:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])
