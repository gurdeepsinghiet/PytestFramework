import json
import os
import sys
import pytest
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import logging

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class LicenseModelFactory(object):
    def update_licence_model_attribute_by_tag(self, lm_attr_name, json_tag, value, response_lm_dictionary):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        assertions_report = {}
        assertions_report["Api_Name"] = currentFuncName()
        assertions_report["inputs"] = u.convertDictinarytoJson(response_lm_dictionary)
        assertions_report["Expected_Code"] = "200"
        try:
            jsonpath_expression = parse('$..licenseModelAttribute[*]')
            for match in jsonpath_expression.find(response_lm_dictionary):
                if match.value["enforcementAttribute"]["name"] == lm_attr_name:
                    match.value[json_tag] = value
                    self.Updated_LM_Json = response_lm_dictionary
            assertions_report["actual_Code"] = "200"
            assertions_report["Expected_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Status"] = "Pass"
            assertions_report["Act_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Response_time"] = ""
        except TypeError as error:
            assertions_report["actual_Code"] = "404"
            assertions_report["Expected_Response"] = ""
            assertions_report["Status"] = "Failed"
            assertions_report["Act_Response"] = "Type Error occured during updation of LM json"
            assertions_report["Response_time"] = ""
            LOGGER.error("Type Error occured during updation of LM json")
            self.report_data.append(assertions_report)
            pytest.fail("Type Error occured during updation of LM json")
        self.report_data.append(assertions_report)
        return self

    def get_licence_model_attribute_tag_value(self, lm_attr_name, json_tag, out_parameter, response_lm_dictionary):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        assertions_report = {}
        assertions_report["Api_Name"] = currentFuncName()
        assertions_report["inputs"] = u.convertDictinarytoJson(response_lm_dictionary)
        assertions_report["Expected_Code"] = "200"
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        try:
            for match in jsonpath_expression.find(response_lm_dictionary):
                if match.value["enforcementAttribute"]["name"] == lm_attr_name:
                    self.out_param_List[out_parameter] = match.value[json_tag]
            LOGGER.info(self.out_param_List[out_parameter])
            assertions_report["actual_Code"] = "200"
            assertions_report["Expected_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Status"] = "Pass"
            assertions_report["Act_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Response_time"] = ""
        except TypeError as error:
            assertions_report["actual_Code"] = "404"
            assertions_report["Expected_Response"] = ""
            assertions_report["Status"] = "Failed"
            assertions_report["Act_Response"] = "Type Error occured during updation of LM json"
            assertions_report["Response_time"] = ""
            LOGGER.error("Type Error occured during updation of LM json")
            self.report_data.append(assertions_report)
            pytest.fail("Type Error occured during updation of LM json")
        self.report_data.append(assertions_report)
        return self

    # this method update the multiple License Attributes of LM Dictionary object
    # LM_ATTR_NameList : List of Attributed need to be update
    # tagsList: tags names of LM Attributes List
    # valueList : correspondes value of Tags need to be updated
    # response_LM_dictionry : Dictionary object of LM Json
    def update_licence_model_attributes_by_tags(self, lm_attr_name_list, json_tags_list, value_list,
                                                response_lm_dictionary):

        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        assertions_report = {}
        assertions_report["Api_Name"] = currentFuncName()
        assertions_report["inputs"] = u.convertDictinarytoJson(response_lm_dictionary)
        assertions_report["Expected_Code"] = "200"
        try:
            jsonpath_expression = parse('$..licenseModelAttribute[*]')
            for i, attr in enumerate(lm_attr_name_list):
                jsonpath_expression.find(response_lm_dictionary)
                for match in jsonpath_expression.find(response_lm_dictionary):
                    if match.value["enforcementAttribute"]["name"] == lm_attr_name_list[i]:
                        LOGGER.info(attr)
                        LOGGER.info(value_list[i])
                        match.value[json_tags_list[i]] = value_list[i]
                        self.Updated_LM_Json = response_lm_dictionary

            assertions_report["actual_Code"] = "200"
            assertions_report["Expected_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Status"] = "Pass"
            assertions_report["Act_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Response_time"] = ""
        except TypeError as error:
            assertions_report["actual_Code"] = "404"
            assertions_report["Expected_Response"] = ""
            assertions_report["Status"] = "Failed"
            assertions_report["Act_Response"] = "Type Error occured during updation of LM json"
            assertions_report["Response_time"] = ""
            LOGGER.error("Type Error occured during updation of LM json")
            self.report_data.append(assertions_report)
            pytest.fail("Type Error occured during updation of LM json")

        self.report_data.append(assertions_report)
        return self

    def get_licence_model_attributes_tags_values(self, lm_attr_name_list, json_tags_list, out_parameter_list,
                                                 response_lm_dictionary):
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        assertions_report = {}
        assertions_report["Api_Name"] = currentFuncName()
        assertions_report["inputs"] = u.convertDictinarytoJson(response_lm_dictionary)
        assertions_report["Expected_Code"] = "200"
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        try:
            for i, attr in enumerate(lm_attr_name_list):
                for match in jsonpath_expression.find(response_lm_dictionary):
                    if (match.value["enforcementAttribute"]["name"] == lm_attr_name_list[i]):
                        LOGGER.info(attr[i])
                        LOGGER.info(out_parameter_list[i])
                        self.out_param_List[out_parameter_list[i]] = match.value[json_tags_list[i]]
            assertions_report["actual_Code"] = "200"
            assertions_report["Expected_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Status"] = "Pass"
            assertions_report["Act_Response"] = u.convertDictinarytoJson(response_lm_dictionary)
            assertions_report["Response_time"] = ""
        except TypeError as error:
            assertions_report["actual_Code"] = "404"
            assertions_report["Expected_Response"] = ""
            assertions_report["Status"] = "Failed"
            assertions_report["Act_Response"] = "Type Error occurred during updating of LM json"
            assertions_report["Response_time"] = ""
            LOGGER.error("Type Error occured during updation of LM json")
            self.report_data.append(assertions_report)
            pytest.fail("Type Error occured during updation of LM json")
        self.report_data.append(assertions_report)
        return self

    def getLicenceModelAttributesTagsValues1(self, LM_ATTR_NameList, tagsList, getvalueList, response_LM_dictionry):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        for i, attr in enumerate(LM_ATTR_NameList):
            for match in jsonpath_expression.find(response_LM_dictionry):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                    LOGGER.info(attr[i])
                    LOGGER.info(getvalueList[i])
                    self.out_param_List[getvalueList[i]] = match.value[tagsList[i]]
        return self

    def get_enforcement(self):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.getApiresponse = self.get_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0', "",
                                               current_api_name(), 200)
        if self.getApiresponse[1] == ErrorCode.HTTP200:
            response_enforcement = utility.convertJsontoDictinary(self.getApiresponse[0])
            enforcement_id = response_enforcement["enforcement"]["id"]
            self.enforcementProps = [enforcement_id]
        return self

    def search_enforcement(self):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.get_request(url + '/ems/api/v5/enforcements?name=Sentinel RMS', "", current_api_name(), 200)
        if self.getApiresponse[1] == ErrorCode.HTTP200:
            response_enforcement = utility.convertJsontoDictinary(self.getApiresponse[0])
            enforcement_id = response_enforcement["enforcements"]["enforcement"][0]["id"]
            self.enforcementProps = [enforcement_id]
        return self

    def get_enforcement_id(self) -> list:
        return self.enforcementProps

    def search_flexible_license_model(self, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.search_enforcement();
        enforcement_id = self.get_enforcement_id()[0];
        self.get_request(
            url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/name=Flexible License Model', "",
            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
            self.FlexibleLicenseModelJson = utility.convertJsontoDictinary(self.getApiresponse[0])
        return self

    def search_cloud_connected_licence_model(self, expected_return_code, out_parameter_list=None,
                                             out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.search_enforcement();
        enforcement_id = self.get_enforcement_id()[0];
        self.get_request(
            url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/name=Connected License Model', "",
            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
            self.CloudConnectedLicenseModelJson = utility.convertJsontoDictinary(self.getApiresponse[0])
        return self

    def add_flexible_licence_model_standalone(self, lm_name, response_lm_dict, expected_return_code,
                                              out_parameter_list=None, out_json_path_list=None):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "1", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "1", response_lm_dict)
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = json.dumps(response_lm_dict)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list == None and out_json_path_list == None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, current_api_name(), expected_return_code, ["LM_name", "lmId", "LMRES"],
                              ['$.licenseModel.name', '$.licenseModel.id', '$'])
            LOGGER.info(self.out_param_List["LM_name"])
            LOGGER.info(self.out_param_List["lmId"])
            LOGGER.info(self.out_param_List["LMRES"])
        elif out_parameter_list is not None and out_json_path_list is not None:
            LOGGER.info("========================================")
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, current_api_name(), expected_return_code,
                              out_parameter_list, out_json_path_list)
        return self

    def add_flexible_licence_model_network(self, lm_name, response_lm_dict, expected_return_code,
                                           out_parameter_list=None, out_json_path_list=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "0", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "1", response_lm_dict)
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = json.dumps(response_lm_dict)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, current_api_name(), expected_return_code,
                              ["LM_name_onpremNetwork", "lmId_onprem_network"],
                              ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.out_param_List["LM_name_onpremNetwork"])
            LOGGER.info(self.out_param_List["lmId_onprem_network"])
        elif out_parameter_list is not None and out_json_path_list is not None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, current_api_name(), expected_return_code,
                              out_parameter_list, out_json_path_list)
        return self

    def add_on_premise_lm_network(self, lm_name, response_lm_dic, expected_return_code, out_parameter_list=None,
                                  out_json_path_list=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dic)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "0", response_lm_dic)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "0", response_lm_dic)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_lm_dic["licenseModel"]["name"] = lm_name
        response_LM_json1 = json.dumps(response_lm_dic)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, currentApiFuncName(), expected_return_code,
                              ["LM_name_onPrem_Net", "lmId_onPrem_net"],
                              ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.out_param_List["LM_name_onPrem_Net"])
            LOGGER.info(self.out_param_List["lmId_onPrem_net"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, currentApiFuncName(), expected_return_code,
                              out_parameter_list, out_json_path_list)
        return self

    def add_on_premise_lm_standalone(self, lm_name, response_lm_dict, expected_return_code, out_parameter_list=None,
                                     out_json_path_list=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "1", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "0", response_lm_dict)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = json.dumps(response_lm_dict)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, currentApiFuncName(), expected_return_code,
                              ["LM_name_OnpremStand", "lmId_OnpremStand"],
                              ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.out_param_List["LM_name_OnpremStand"])
            LOGGER.info(self.out_param_List["lmId_OnpremStand"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, currentApiFuncName(), expected_return_code,
                              out_parameter_list, out_json_path_list)
        return self

    def add_cloud_connected_licence_model(self, lm_name, response_lm_dict, expected_return_code,
                                          out_parameter_list=None,
                                          out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = json.dumps(response_lm_dict)
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1, current_api_name(), expected_return_code,
                              ["LM_name", "lmId"], ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.out_param_List["LM_name"])
            LOGGER.info(self.out_param_List["lmId"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.post_request(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                              response_LM_json1,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        return self

    def partial_update_lm(self, lm_json, expected_return_code, out_parameter_list, out_json_path_list,
                          enforcement_id=None,
                          enforcement_name_version=None, license_model_id=None, lmid=None, lm_name=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if lmid is not None and enforcement_id is not None:
            self.patch_request(url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/' + lmid, lm_json,
                               current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        elif lmid is not None and enforcement_name_version is not None:
            self.patch_request(
                url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + lmid,
                lm_json, current_api_name(),
                expected_return_code, out_parameter_list, out_json_path_list)
        elif license_model_id is not None and enforcement_name_version is not None:
            self.patch_request(
                url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + license_model_id,
                lm_json,
                current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if license_model_id is not None and enforcement_id is not None:
            self.patch_request(
                url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/' + license_model_id,
                lm_json,
                current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif license_model_id is not None and enforcement_name_version is not None:
            self.patch_request(
                url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + license_model_id,
                lm_json,
                current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif lm_name is not None and enforcement_id is not None:
            self.patch_request(url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/name=' + lm_name,
                               lm_json,
                               current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif lm_name is not None and enforcement_name_version is not None:
            self.patch_request(
                url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/name=' + lm_name,
                lm_json,
                current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.patchApiResponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self
