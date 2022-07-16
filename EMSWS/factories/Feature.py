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
        self.ems_api_request_wrapper(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
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
        self.ems_api_request_wrapper(url + '/ems/api/v5/features', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_feature_json(self, feature_json, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_request_wrapper(url + '/ems/api/v5/features', feature_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)

        return self

    def get_feature(self, expected_return_code, out_parameter_list, out_json_path_list, feature_id=None,
                    name_version=None,
                    identifier_namespace=None, identifier=None, external_id=None, id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if feature_id is not None:
            request_url=url + '/ems/api/v5/features/' + feature_id
        elif id is not None:
            request_url=url + '/ems/api/v5/features/' + id
        elif name_version is not None:
            request_url=url + '/ems/api/v5/features/nameVersion=' + name_version
        elif identifier_namespace is not None:
            request_url=url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace
        elif identifier is not None:
            request_url=url + '/ems/api/v5/features/identifier=' + identifier
        elif external_id is not None:
            request_url=url + '/ems/api/v5/features/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def partial_update_feature(self, feature_json, expected_return_code, out_parameter_list, out_json_path_list,
                               id=None,
                               name_version=None, identifier_namespace=None, identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            request_url=url + '/ems/api/v5/features/' + id
        elif name_version is not None:
            request_url=url + '/ems/api/v5/features/nameVersion=' + name_version
        elif identifier is not None:
            request_url=url + '/ems/api/v5/features/identifier=' + identifier
        elif external_id is not None:
            request_url=url + '/ems/api/v5/features/externalId=' + external_id
        elif identifier_namespace is not None:
            request_url=url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace
        self.ems_api_request_wrapper(request_url,feature_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def search_feature(self, out_parameter_list, out_json_path_list, expected_return_code, id=None, identifier=None,
                       license_model_name=None, license_model_id=None, namespace_id=None,
                       namespace_name=None, name=None, description=None, version=None, external_id=None, ref_id1=None,
                       ref_id2=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if identifier is not None:
            request_url += "identifier=" + identifier + "&"
        if license_model_name is not None:
            request_url += "licenseModelName=" + license_model_name + "&"
        if license_model_id is not None:
            request_url += "licenseModelId=" + license_model_id + "&"
        if namespace_id is not None:
            request_url += "namespaceId=" + namespace_id + "&"
        if namespace_name is not None:
            request_url += "namespaceName=" + namespace_name + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if description is not None:
            request_url += "description=" + description + "&"
        if version is not None:
            request_url += "version=" + version + "&"
        if external_id is not None:
            request_url += "externalId=" + external_id + "&"
        if ref_id1 is not None:
            request_url += "refId1=" + ref_id1 + "&"
        if ref_id2 is not None:
            request_url += "refId2=" + ref_id2 + "&"
        request_url = url + "/ems/api/v5/features?" + request_url[0:-1]
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def delete_feature(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                       name_version=None,
                       identifier_namespace=None, identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url =url + '/ems/api/v5/features/' + id
        elif name_version is not None:
            request_url =url + '/ems/api/v5/features/nameVersion=' + name_version
        elif identifier_namespace is not None:
            request_url =url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace
        elif identifier is not None:
            request_url =url + '/ems/api/v5/features/identifier=' + identifier
        elif external_id is not None:
            request_url =url + '/ems/api/v5/features/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_feature(self, feature_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                        name_version=None,
                        identifier_namespace=None, identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url =""
        if id is not None:
            request_url =url + '/ems/api/v5/features/' + id
        elif name_version is not None:
            request_url =url + '/ems/api/v5/features/nameVersion=' + name_version
        elif identifier is not None:
            request_url =url + '/ems/api/v5/features/identifier=' + identifier
        elif external_id is not None:
            request_url =url + '/ems/api/v5/features/externalId=' + external_id
        elif identifier_namespace is not None:
            request_url =url + '/ems/api/v5/features/identifierNamespace=' + identifier_namespace
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self
