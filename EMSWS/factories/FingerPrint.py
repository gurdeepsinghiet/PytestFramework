import EMSWS.EMSConfig as Constant
import EMSWS.JsonPath as JsonPath
import EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class FingerPrintFactory(object):

    def add_finger_print(self, expected_return_code, customer_id, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        fp_xml = self.retrive_finger_print("testfp")
        LOGGER.info(fp_xml)
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.fingerPrintJsonPath,
                            ['$..friendlyName', '$..refId1', '$..refId2', '$..fingerprintXml'],
                            ["fp" + self.RandomString(9), "fprefId1" + self.RandomString(9),
                             "fprefId2" + self.RandomString(9), fp_xml])

        request_url=url + '/ems/api/v5/customers/' + customer_id + '/fingerprints'
        self.ems_api_request_wrapper(request_url, self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self
