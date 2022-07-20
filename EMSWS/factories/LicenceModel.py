import json
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
        u = UtilityClass()
        current_api_name = u.currentApiName()
        assertions_report = {}
        assertions_report["Api_Name"] = current_api_name()
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
            assertions_report["Act_Response"] = "Type Error occurred during updating of LM json"
            assertions_report["Response_time"] = ""
            LOGGER.error("Type Error occurred during updating of LM json")
            self.report_data.append(assertions_report)
            pytest.fail("Type Error occurred during updating of LM json")
        self.report_data.append(assertions_report)
        return self

    def get_licence_model_attribute_tag_value(self, lm_attr_name, json_tag, out_parameter, response_lm_dictionary):
        u = UtilityClass()
        current_api_name = u.currentApiName()
        assertions_report = {}
        assertions_report["Api_Name"] = current_api_name()
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
        u = UtilityClass()
        current_api_name = u.currentApiName()
        assertions_report = {}
        assertions_report["Api_Name"] = current_api_name()
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
        u = UtilityClass()
        current_api_name = u.currentApiName()
        assertions_report = {}
        assertions_report["Api_Name"] = current_api_name()
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

        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        for i, attr in enumerate(LM_ATTR_NameList):
            for match in jsonpath_expression.find(response_LM_dictionry):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                    LOGGER.info(attr[i])
                    LOGGER.info(getvalueList[i])
                    self.out_param_List[getvalueList[i]] = match.value[tagsList[i]]
        return self

    def get_enforcement(self,expected_return_code, out_parameter_list=None, out_json_path_list=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0'
        self.ems_api_auth_request_wrapper("GET", request_url, "" , "",
                                          current_api_name(), username, password,expected_return_code,
                                          out_parameter_list, out_json_path_list,output_res_xml_parameter, bearerAuth=None)
        return self

    def search_enforcement(self,expected_return_code, out_parameter_list=None, out_json_path_list=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url=url + '/ems/api/v5/enforcements?name=Sentinel RMS'
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                         current_api_name(), username, password, expected_return_code,
                                         out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                         bearerAuth=None)
        return self

    def search_flexible_license_model(self, expected_return_code, out_parameter_list=None,
                                      out_json_path_list=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.search_enforcement(ErrorCode.HTTP200,["enforcement_id"],["$..enforcements.enforcement[0].id"])
        request_url=url + '/ems/api/v5/enforcements/' + self.out_param_List["enforcement_id"] + '/licenseModels/name=Flexible License Model'
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def search_cloud_connected_licence_model(self, expected_return_code, out_parameter_list=None,
                                             out_json_path_list=None ,output_res_xml_parameter =None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.search_enforcement(ErrorCode.HTTP200,["enforcement_id"],["$..enforcements.enforcement[0].id"]);
        request_url=url + '/ems/api/v5/enforcements/' + self.out_param_List["enforcement_id"] + '/licenseModels/name=Connected License Model'
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def add_flexible_licence_model_standalone(self, lm_name, response_lm_dict, expected_return_code,
                                              out_parameter_list=None, out_json_path_list=None ,output_res_xml_parameter=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "1", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "1", response_lm_dict)
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = utility.convertDictinarytoJson(response_lm_dict)
        request_url = url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels'
        self.ems_api_auth_request_wrapper("POST", request_url, response_LM_json1, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def add_flexible_licence_model_network(self, lm_name, response_lm_dict, expected_return_code,
                                           out_parameter_list=None, out_json_path_list=None, output_res_xml_parameter=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "0", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "1", response_lm_dict)
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = utility.convertDictinarytoJson(response_lm_dict)
        request_url = url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels'
        self.ems_api_auth_request_wrapper("POST", request_url, response_LM_json1, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def add_on_premise_lm_network(self, lm_name, response_lm_dict, expected_return_code, out_parameter_list=None,
                                  out_json_path_list=None ,output_res_xml_parameter=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "0", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "0", response_lm_dict)
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = utility.convertDictinarytoJson(response_lm_dict)
        request_url=url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels'
        self.ems_api_auth_request_wrapper("POST", request_url, response_LM_json1, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def add_on_premise_lm_standalone(self, lm_name, response_lm_dict, expected_return_code, out_parameter_list=None,
                                     out_json_path_list=None ,output_res_xml_parameter=None):
        self.update_licence_model_attribute_by_tag("ENFORCE_CLOCK_TAMPERED", "value", "FALSE", response_lm_dict)
        self.update_licence_model_attribute_by_tag("LICENSE_TYPE", "value", "1", response_lm_dict)
        self.update_licence_model_attribute_by_tag("DEPLOYMENT_TYPE", "value", "0", response_lm_dict)
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = utility.convertDictinarytoJson(response_lm_dict)
        request_url=url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels'
        self.ems_api_auth_request_wrapper("POST", request_url, response_LM_json1, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def add_cloud_connected_licence_model(self, lm_name, response_lm_dict, expected_return_code,
                                          out_parameter_list=None,
                                          out_json_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        response_lm_dict["licenseModel"]["name"] = lm_name
        response_LM_json1 = utility.convertDictinarytoJson(response_lm_dict)
        request_url=url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels'
        self.ems_api_auth_request_wrapper("POST", request_url, response_LM_json1, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self

    def partial_update_lm(self, lm_json, expected_return_code, out_parameter_list, out_json_path_list,
                          enforcement_id=None,
                          enforcement_name_version=None, license_model_id=None, lmid=None, lm_name=None
                          ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if lmid is not None and enforcement_id is not None:
            request_url = url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/' + lmid
        elif lmid is not None and enforcement_name_version is not None:
            request_url = url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + lmid
        elif license_model_id is not None and enforcement_name_version is not None:
            request_url = url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + license_model_id
        if license_model_id is not None and enforcement_id is not None:
            request_url = url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/' + license_model_id
        elif license_model_id is not None and enforcement_name_version is not None:
            request_url = url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/' + license_model_id
        elif lm_name is not None and enforcement_id is not None:
            request_url = url + '/ems/api/v5/enforcements/' + enforcement_id + '/licenseModels/name=' + lm_name
        elif lm_name is not None and enforcement_name_version is not None:
            request_url =url + '/ems/api/v5/enforcements/nameVersion=' + enforcement_name_version + '/licenseModels/name=' + lm_name
        self.ems_api_auth_request_wrapper("PATCH", request_url, lm_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list, output_res_xml_parameter,
                                          bearerAuth=None)
        return self
