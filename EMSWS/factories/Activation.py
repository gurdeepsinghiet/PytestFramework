import EMSWS.EMSConfig as Constant
import logging
from EMSWS.Utilities import UtilityClass

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class ActivationFactory(object):

    def add_activation(self, activation_json_path_file, expected_return_code, pkId, out_parameter_list=None,
                       out_json_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(activation_json_path_file, ['$..activationProductKeys.activationProductKey[0].pkId'],
                            [pkId])
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/activations/bulkActivate',
                                          self.UpdateJsonFileResponse, "",current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter, bearerAuth=None)
        return self

    def add_activation_json(self, activation_json, expected_return_code, out_parameter_list=None,
                            out_json_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/activations/bulkActivate',activation_json, "",
                                          current_api_name(), username, password, expected_return_code,out_parameter_list,
                                          out_json_path_list, output_res_xml_parameter,bearerAuth=None)
        return self
