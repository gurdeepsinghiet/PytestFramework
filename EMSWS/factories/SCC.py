from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import logging
from requests.structures import CaseInsensitiveDict
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class SCCFactory():

    def get_scc_app_properties(self, expected_return_code, out_parameter_list=None,
                               out_json_path_list=None, id=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        headers = CaseInsensitiveDict()
        headers["x-sfnt-vendor"] = "6291536"
        request_url = ""
        if id is not None:
            request_url = url + '/scc/v5/applicationProperties/' + id
        self.ems_api_auth_request_wrapper("GET", request_url, "", headers, current_api_name(), "admin", "142E!LmT",
                                         expected_return_code, out_parameter_list, out_json_path_list,
                                         output_res_xml_parameter)
        return self


    def post_scc_app_reset_flag(self, customer_id ,fingerprint_id,expected_return_code, out_parameter_list=None,
                               out_json_path_list=None, id=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        headers = CaseInsensitiveDict()
        headers["x-sfnt-vendor"] = "6291536"
        if id is not None:
            request_url = url + '/scc/v5/customers/'+customer_id+ '/fingerprints/' + fingerprint_id + '/resetUpdateFlag'
        self.ems_api_auth_request_wrapper("POST", request_url, "", headers, current_api_name(), "admin", "142E!LmT",
                                         expected_return_code, out_parameter_list, out_json_path_list,
                                         output_res_xml_parameter)
        return self