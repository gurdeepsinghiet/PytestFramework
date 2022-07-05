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
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.fingerPrintJsonPath,
                            ['$..friendlyName', '$..refId1', '$..refId2', '$..fingerprintXml'],
                            ["fp" + self.RandomString(9), "fprefId1" + self.RandomString(9),
                             "fprefId2" + self.RandomString(9), fp_xml])
        LOGGER.info(self.UpdateJsonFileResponse)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/customers/' + customer_id + '/fingerprints',
                             self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, ["friendlyName"],
                             ['$..friendlyName'])
            LOGGER.info(self.out_param_List["friendlyName"])

        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/customers/' + customer_id + 'fingerprints', self.UpdateJsonFileResponse,
                             current_api_name(),
                             expected_return_code, out_parameter_list, out_json_path_list)
        return self
