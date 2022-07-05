from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class FeatureFactory(object):

    def add_feature(self, namespace_name, lm_name, expected_return_code, out_parameter_list=None,
                    out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.featureJsonPath,
                            ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                             '$..featureLicenseModel[0].licenseModel.name'],
                            ["Ftr" + self.RandomString(9), "1.0", namespace_name, lm_name], ["featureRes"], ['$'])
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, ["feature_name", "feature_version", "featureRes"],
                             ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, out_parameter_list, out_json_path_list)
        return self

    def add_feature_json_file_path(self, feature_file_path, feature_name, feature_version, namespace_name, lm_name,
                                   expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(feature_file_path,
                            ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$..namespace.name',
                             '$..featureLicenseModel[0].licenseModel.name'],
                            [feature_name, feature_version, namespace_name, lm_name], ["featureRes"], ['$'])
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, ["feature_name", "feature_version", "featureRes"],
                             ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code, out_parameter_list, out_json_path_list)
        return self

    def add_feature_json(self, feature_json, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/features', feature_json, current_api_name(), expected_return_code,
                             ["feature_name", "feature_version", "featureRes"],
                             ['$.feature.nameVersion.name', '$.feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["feature_name"])
            LOGGER.info(self.out_param_List["feature_version"])
            LOGGER.info(self.out_param_List["featureRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/features', feature_json, current_api_name(), expected_return_code,
                             out_parameter_list, out_json_path_list)

        return self

    def get_feature(self, out_parameter_list, out_json_path_list, expected_return_code, feature_id=None,
                    name_version=None,
                    identifier_namespace=None, identifier=None, external_id=None, id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if feature_id is not None:
            self.getRequest(url + '/ems/api/v5/features/' + feature_id, "", current_api_name(), expected_return_code,
                            out_parameter_list, out_json_path_list)
        elif id is not None:
            self.getRequest(url + '/ems/api/v5/features/' + id, "", current_api_name(), expected_return_code,
                            out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.getRequest(url + '/ems/api/v5/features/nameVersion=' + name_version, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier_namespace is not None:
            self.getRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace, "",
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.getRequest(url + '/ems/api/v5/features/identifier=' + identifier, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.getRequest(url + '/ems/api/v5/features/externalId=' + external_id, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def partial_update_feature(self, feature_json, expected_return_code, out_parameter_list, out_json_path_list,
                               id=None,
                               name_version=None, identifier_namespace=None, identifier=None, external_id=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.patchRequest(url + '/ems/api/v5/features/' + id, feature_json, current_api_name(),
                              expected_return_code, out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.patchRequest(url + '/ems/api/v5/features/nameVersion=' + name_version, feature_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.patchRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.patchRequest(url + '/ems/api/v5/features/externalId=' + external_id, feature_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier_namespace is not None:
            self.patchRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace, feature_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.patchApiResponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def search_feature(self, out_parameter_list, out_json_path_list, expected_return_code, id=None, identifier=None,
                       license_model_name=None, license_model_id=None, namespace_id=None,
                       namespace_name=None, name=None, description=None, version=None, external_id=None, ref_id1=None,
                       ref_id2=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        responeurl = ""
        if id is not None:
            responeurl += "id=" + id + "&"
        if identifier is not None:
            responeurl += "identifier=" + identifier + "&"
        if license_model_name is not None:
            responeurl += "licenseModelName=" + license_model_name + "&"
        if license_model_id is not None:
            responeurl += "licenseModelId=" + license_model_id + "&"
        if namespace_id is not None:
            responeurl += "namespaceId=" + namespace_id + "&"
        if namespace_name is not None:
            responeurl += "namespaceName=" + namespace_name + "&"
        if name is not None:
            responeurl += "name=" + name + "&"
        if description is not None:
            responeurl += "description=" + description + "&"
        if version is not None:
            responeurl += "version=" + version + "&"
        if external_id is not None:
            responeurl += "externalId=" + external_id + "&"
        if ref_id1 is not None:
            responeurl += "refId1=" + ref_id1 + "&"
        if ref_id2 is not None:
            responeurl += "refId2=" + ref_id2 + "&"
        LOGGER.info(url + "/ems/api/v5/features?" + responeurl[0:-1])
        self.getRequest(url + "/ems/api/v5/features?" + responeurl[0:-1], "", current_api_name(),
                        expected_return_code,
                        out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def delete_feature(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                       name_version=None,
                       identifier_namespace=None, identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.deleteRequest(url + '/ems/api/v5/features/' + id, "", current_api_name(), expected_return_code,
                               out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.deleteRequest(url + '/ems/api/v5/features/nameVersion=' + name_version, "", current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier_namespace is not None:
            self.deleteRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace, "",
                               current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.deleteRequest(url + '/ems/api/v5/features/identifier=' + identifier, "", current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.deleteRequest(url + '/ems/api/v5/features/externalId=' + external_id, "", current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        if self.deleteApiresponse[0] == expected_return_code:
            if self.deleteApiresponse[0] == ErrorCode.HTTP204:
                LOGGER.info("Feature deleted successfully")
            else:
                for i, resvar in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def replace_feature(self, feature_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                        name_version=None,
                        identifier_namespace=None, identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.putRequest(url + '/ems/api/v5/features/' + id, feature_json, current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.putRequest(url + '/ems/api/v5/features/nameVersion=' + name_version, feature_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.putRequest(url + '/ems/api/v5/features/identifier=' + identifier, feature_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.putRequest(url + '/ems/api/v5/features/externalId=' + external_id, feature_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier_namespace is not None:
            self.putRequest(url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace,
                            feature_json, current_api_name(), expected_return_code, out_parameter_list,
                            out_json_path_list)
        if self.putApiResponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self
