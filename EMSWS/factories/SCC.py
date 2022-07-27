from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import logging
import EMSWS.JsonPath as JsonPath
import EMSWS.XmlPath as XmlPath
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
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"
        request_url = ""
        if id is not None:
            request_url = url + '/scc/v5/applicationProperties/' + id
        self.ems_api_auth_request_wrapper("GET", request_url, "", headers, current_api_name(), "admin", "142E!LmT",
                                         expected_return_code, out_parameter_list, out_json_path_list,
                                         output_res_xml_parameter,bearerAuth=None)
        return self


    def post_scc_app_reset_flag(self, customer_name ,fingerprint_name,epoch_time,expected_return_code, out_parameter_list=None,
                               out_json_path_list=None, id=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        headers = CaseInsensitiveDict()
        headers["x-sfnt-vendor"] = "6291536"
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"
        if self.isXmlFile(self.getModulePath() + XmlPath.resetUpdateXmlPath):
            self.updateXMLFile(XmlPath.resetUpdateXmlPath,
                               ["./lastUpdateTimestamp"],
                               [epoch_time])
            LOGGER.info(self.xmlstroutput)
            request_url = url + '/scc/v5/customers/' + customer_name + '/fingerprints/' + fingerprint_name + '/resetUpdateFlag'
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, current_api_name(),
                                              "admin", "142E!LmT",
                                              expected_return_code, out_parameter_list, out_json_path_list,
                                              output_res_xml_parameter, bearerAuth=None)

        def post_scc_sync(self, customer_name, fingerprint_name, epoch_time, expected_return_code,
                                    out_parameter_list=None,
                                    out_json_path_list=None, id=None, output_res_xml_parameter=None):
            utility = UtilityClass()
            current_api_name = utility.currentApiName()
            LOGGER.info(current_api_name())
            request_url = ""
            headers = CaseInsensitiveDict()
            headers["x-sfnt-vendor"] = "6291536"
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            if self.isXmlFile(self.getModulePath() + XmlPath.resetUpdateXmlPath):
                self.updateXMLFile(XmlPath.resetUpdateXmlPath,
                                   ["./lastUpdateTimestamp"],
                                   [epoch_time])
                LOGGER.info(self.xmlstroutput)
                request_url = url + '/scc/v5/customers/' + customer_name + '/fingerprints/' + fingerprint_name + '/resetUpdateFlag'
                self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, current_api_name(),
                                                  "admin", "142E!LmT",
                                                  expected_return_code, out_parameter_list, out_json_path_list,
                                                  output_res_xml_parameter, bearerAuth=None)

        return self

    def post_ems_app_reset_flag(self, customer_name ,fingerprint_name,epoch_time,expected_return_code, out_parameter_list=None,
                               out_json_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"
        if self.isXmlFile(self.getModulePath() + XmlPath.resetUpdateXmlPath):
            self.updateXMLFile(XmlPath.resetUpdateXmlPath,
                               ["./lastUpdateTimestamp"],
                               [epoch_time])
            LOGGER.info(self.xmlstroutput)
            request_url = url + '/ems/api/v5/customers/name=' + customer_name + '/fingerprints/friendlyName=' + fingerprint_name + '/resetUpdateFlag'
            self.ems_api_auth_request_wrapper("POST", request_url, self.xmlstroutput, headers, current_api_name(),
                                              "admin", "142E!LmT",
                                              expected_return_code, out_parameter_list, out_json_path_list,
                                              output_res_xml_parameter, bearerAuth=None)

        return self