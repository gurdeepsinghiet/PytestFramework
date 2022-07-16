import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
from EMSWS.Utilities import UtilityClass
from EMSWS.factories.RestApi import RestApiUtilityFactory

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class EmsApiWrapper():

    def ems_api_request_wrapper(self,request_url,request_body,expected_return_code,api_name,
                                out_parameter_list,out_json_path_list):
        utility=UtilityClass()
        ws_yml_data=utility.read_yaml_file(utility.getModulePath()+"\\"+'EMSWS.yaml', api_name)
        if ws_yml_data['protocol'] == 'POST':

            self.post_request(request_url,request_body, api_name,
                              expected_return_code, out_parameter_list, out_json_path_list)

        elif ws_yml_data['protocol'] == 'GET':
            self.get_request(request_url,request_body, api_name, expected_return_code,
                             out_parameter_list, out_json_path_list)
            if self.getApiresponse[1] == expected_return_code and out_parameter_list !=None and out_json_path_list !=None:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])

        elif ws_yml_data['protocol'] == 'PUT':
            self.put_request(request_url, request_body, api_name,expected_return_code,
                             out_parameter_list, out_json_path_list)
            if self.patchApiResponse[1] == expected_return_code and out_parameter_list !=None and out_json_path_list !=None:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])

        elif ws_yml_data['protocol'] == 'PATCH':
            self.patch_request(request_url, request_body, api_name,
                               expected_return_code, out_parameter_list, out_json_path_list)
            if self.patchApiResponse[1] == expected_return_code and out_parameter_list !=None and out_json_path_list !=None:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])

        elif ws_yml_data['protocol'] == 'DELETE':
            self.delete_request(request_url, "", api_name,
                                expected_return_code, out_parameter_list, out_json_path_list)
            if self.deleteApiresponse[0] == expected_return_code:
                if self.deleteApiresponse[0] == ErrorCode.HTTP204:
                    LOGGER.info("NameSpace deleted successfully")
                elif self.deleteApiresponse[0] == expected_return_code and out_parameter_list !=None and out_json_path_list !=None :
                    for i, out_param in enumerate(out_parameter_list):
                        LOGGER.info(out_parameter_list[i])
                        LOGGER.info(self.out_param_List[out_parameter_list[i]])